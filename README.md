# DS2002 Final Project: Rate of Inflation vs. Annual Median Income
Final Project for Data Science Systems, exploring link between education among different countries and their associated life expectancies.

## Contributors
- Angad Brar, zqq4hx
- Rohan Singh, psw2uw
- Varun Togaru, wbz9mn

### Depedencies

to install packages neccesary to run project run `pip install -r requirements.txt`.

### To Setup MySQL database
- Start a locally hosted mysql server and run `mysql -u root`.
- Run SQL query `CREATE DATABASE etl_project;`.
- Then run `USE etl_project;` to use the database you just created.
- Run `python ETL_script.py` to create the cpi and income tables.

## Project Breakdown
### Data Selection and Exploration
- Obtained annual Consumer Price Index (CPI) data from [US Annual CPI Data](https://www.minneapolisfed.org/about-us/monetary-policy/inflation-calculator/consumer-price-index-1913-).
- Obtained average annual median income data from [Median U.S. Household Income](https://fred.stlouisfed.org/series/MEHOINUSA646N).
- These datasets were chosen to analyze whether the change in average annual median income is proportional to the rate of inflation. This is a relevant issue as it is often stressed how changes in inflation are outpacing changes in income, affecting cost of living, purchasing power, etc.

### ETL Setup
- Extraction: Loaded CSV files into a Python environment.
- Transformation: Data cleaning (ensured consistency, normalized values), derived new metrics (e.g., real income, normalized trends).
- Loading: Data stored in MySQL with upsert logic to avoid duplication.

### Data Analysis
- Key Visualizations: Normalized trends (CPI vs. Income), Real income projections, Annual income growth vs. CPI growth.
- Income and CPI trends are closely aligned, indicating economic interdependence.

### Cloud Storage
- Google Cloud Storage (GCS) used for scalable data storage.
- Secure credentials managed with environment variables.

### Reflection Paper
- [Reflection](https://docs.google.com/document/d/1_V8ahrtEmrL1XhUhNlQpnsXA15N-FZq1gd_eoBC5kYU/edit?usp=sharing)

### Presentation
- [Presentation](https://docs.google.com/presentation/d/1P1pE2rCYhFRfa_BVIRr5M8UMTz75ea58vaKP6P82JfQ/edit?usp=sharing)
