import pandas as pd

# load data
edu_path = 'datasets/world-education-data.csv'
life_expectancy_path = 'datasets/life-expectancy.csv'
edu_df = pd.read_csv(edu_path)
life_df = pd.read_csv(life_expectancy_path)

# clean life expectancy data
life_df.rename(columns={'Entity': 'country', 'Year': 'year', 'Life expectancy': 'life_expectancy'}, inplace=True)
life_df = life_df.loc[life_df['year'] >= 1999]

# clean education data
edu_df.drop(columns=['country_code'], inplace=True)
edu_df = edu_df.loc[edu_df['year'] <= 2016]
edu_df.loc[edu_df['country'] == 'Russian Federation', 'country'] = 'Russia'
edu_df = edu_df.loc[edu_df['country'].isin(life_df['country'].unique())]


# print(life_df.head())
# print(edu_df)

print(life_df['country'].unique())