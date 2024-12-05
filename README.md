# DS2002 Final Project: Rate of Inflation vs. Annual Median Income
Final Project for Data Science Systems, exploring link between education among different countries and their associated life expectancies.

## Contributors
- Angad Brar, zqq4hx
- Rohan Singh, psw2uw
- Varun Togaru, wbz9mn

### Depedencies

to install packages neccesary to run project run,

pip install -r requirements.txt

### To Setup MySQL database
- Start a locally hosted mysql server and run `mysql -u root`.
- Run SQL query `CREATE DATABASE etl_project;`.
- Then run `USE etl_project;` to use the database you just created.
- Run `python ETL_script.py` to create the cpi and income tables.

## Project Breakdown
### Data Selection and Exploration
- Obtained annual Consumer Price Index (CPI) data from [US Annual CPI Data](https://www.minneapolisfed.org/about-us/monetary-policy/inflation-calculator/consumer-price-index-1913-).
- Obtained average annual median income data from [ADD HERE].
- These datasets were chosen to analyze whether the change in average annual median income is proportional to the rate of inflation. This is a relevant issue as it is often stressed how changes in inflation are outpacing changes in income, affecting cost of living, purchasing power, etc.

### ETL Setup
- Define ETL steps: extraction (loading from sources), transformation (cleaning,
filtering, structuring), and loading (MySQL/MongoDB).
- Provide a flowchart or diagram of the ETL pipeline.
- Discuss data storage considerations and any cloud storage requirements.

### Data Analysis
to write/add:
- Create visualizations that effectively communicate insights (e.g., trends, distributions).
- Write a summary of findings, supported by visualizations and statistics

### Cloud Storage and Documentation
to write:
- Document the process, including credentials management and access control

### Reflection Paper
- [Reflection](https://docs.google.com/document/d/1_V8ahrtEmrL1XhUhNlQpnsXA15N-FZq1gd_eoBC5kYU/edit?usp=sharing)

### Presentation
to write:
- Add link to slideshow 
