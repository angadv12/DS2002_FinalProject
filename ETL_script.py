import pandas as pd
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# create database connection string
engine = create_engine(
    "mysql+pymysql://root@localhost:3306/etl_project"
)

# load data from csv
df_income = pd.read_csv('cleaned_data/cleaned_average_annual_income.csv')
df_cpi = pd.read_csv('cleaned_data/cleaned_average_annual_CPI.csv')

# ensure year column is integer
df_income['year'] = df_income['year'].astype(int)
df_cpi['year'] = df_cpi['year'].astype(int)

def upsert_to_mysql(df, table_name, engine, index_column):
    with engine.begin() as conn:
        # create table if it doesn't exist
        df.head(0).to_sql(table_name, conn, if_exists='append', index=False)

        # write data to a temporary table
        temp_table = f"{table_name}_temp"
        df.to_sql(temp_table, conn, if_exists='replace', index=False)

        # upsert logic
        columns = df.columns.tolist()
        update_columns = [f"{col}=VALUES({col})" for col in columns if col != index_column]
        upsert_query = f"""
            INSERT INTO {table_name} ({', '.join(columns)})
            SELECT * FROM {temp_table}
            ON DUPLICATE KEY UPDATE {', '.join(update_columns)};
        """
        conn.execute(text(upsert_query))

        # drop the temporary table
        conn.execute(text(f"DROP TABLE {temp_table}"))
        print(f"Upserted data into table '{table_name}'.")

# upsert data into median_income and cpi tables
upsert_to_mysql(df_income, 'median_income', engine, 'year')
upsert_to_mysql(df_cpi, 'cpi', engine, 'year')