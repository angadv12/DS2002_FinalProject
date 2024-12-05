import pandas as pd
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# Create database connection string
engine = create_engine(
    "mysql+pymysql://root@localhost:3306/etl_project"
)

# Load data from CSV files
df_income = pd.read_csv('cleaned_data/cleaned_average_annual_income.csv')
df_cpi = pd.read_csv('cleaned_data/cleaned_average_annual_CPI.csv')

# Ensure 'year' column is integer
df_income['year'] = df_income['year'].astype(int)
df_cpi['year'] = df_cpi['year'].astype(int)

# Function to upsert data into MySQL
def upsert_to_mysql(df, table_name, engine, index_column):
    with engine.begin() as conn:
        # Ensure the table exists with unique constraints
        create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                {', '.join([f"{col} {dtype}" for col, dtype in zip(df.columns, get_mysql_dtypes(df))])},
                UNIQUE KEY ({index_column})
            );
        """
        conn.execute(text(create_table_query))

        # Write data to a temporary table
        temp_table = f"{table_name}_temp"
        df.to_sql(temp_table, conn, if_exists='replace', index=False)

        # Upsert logic
        columns = df.columns.tolist()
        update_columns = [f"{col}=VALUES({col})" for col in columns if col != index_column]
        upsert_query = f"""
            INSERT INTO {table_name} ({', '.join(columns)})
            SELECT * FROM {temp_table}
            ON DUPLICATE KEY UPDATE {', '.join(update_columns)};
        """
        conn.execute(text(upsert_query))

        # Drop the temporary table
        conn.execute(text(f"DROP TABLE {temp_table}"))
        print(f"Upserted data into table '{table_name}'.")

# Helper function to map pandas dtypes to MySQL dtypes
def get_mysql_dtypes(df):
    dtype_mapping = {
        'int64': 'INT',
        'float64': 'FLOAT',
        'object': 'VARCHAR(255)',
        'datetime64[ns]': 'DATETIME',
        'bool': 'BOOLEAN',
    }
    return [dtype_mapping[str(dtype)] for dtype in df.dtypes]

# Upsert data into median_income and cpi tables
upsert_to_mysql(df_income, 'median_income', engine, 'year')
upsert_to_mysql(df_cpi, 'cpi', engine, 'year')