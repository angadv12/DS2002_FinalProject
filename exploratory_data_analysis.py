import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the data
df_income = pd.read_csv("cleaned_data/cleaned_average_annual_income.csv")
df_cpi = pd.read_csv("cleaned_data/cleaned_average_annual_CPI.csv")

# Merge the datasets on the 'year' column
df_merged = pd.merge(df_income, df_cpi, on="year")

# Normalize both columns to their values in the year 2000
df_merged["income_normalized"] = df_merged["average_annual_median_income"] / df_merged["average_annual_median_income"].iloc[0]
df_merged["cpi_normalized"] = df_merged["average_annual_cpi"] / df_merged["average_annual_cpi"].iloc[0]

# Calculate real income (adjusted for inflation)
df_merged["real_income"] = df_merged["average_annual_median_income"] / (df_merged["average_annual_cpi"] / 100)

# Save the merged and transformed data for documentation or further analysis
df_merged.to_csv("cleaned_data/merged_income_cpi_data.csv", index=False)

# Plot 1: Normalized Trends
plt.figure(figsize=(12, 6))
sns.lineplot(x="year", y="income_normalized", data=df_merged, label="Median Income (Normalized)")
sns.lineplot(x="year", y="cpi_normalized", data=df_merged, label="CPI (Normalized)")
plt.title("Normalized Trends: Median Income vs CPI (2000 = 1.0)")
plt.xlabel("Year")
plt.ylabel("Normalized Value (2000 = 1.0)")
plt.legend()
plt.savefig("normalized_trends.png")
plt.show()

# Plot 2: Real Income Over Time
plt.figure(figsize=(12, 6))
sns.lineplot(x="year", y="real_income", data=df_merged, label="Real Income (Adjusted for Inflation)")
plt.title("Real Income (Adjusted for Inflation) Over Years")
plt.xlabel("Year")
plt.ylabel("Real Income ($)")
plt.legend()
plt.savefig("real_income_trend.png")
plt.show()

# Plot 3: Cumulative Growth of Median Income vs CPI
df_merged["income_cumulative_growth"] = (df_merged["average_annual_median_income"] - df_merged["average_annual_median_income"].iloc[0])
df_merged["cpi_cumulative_growth"] = (df_merged["average_annual_cpi"] - df_merged["average_annual_cpi"].iloc[0])

plt.figure(figsize=(12, 6))
sns.lineplot(x="year", y="income_cumulative_growth", data=df_merged, label="Cumulative Growth: Median Income", color="blue")
sns.lineplot(x="year", y="cpi_cumulative_growth", data=df_merged, label="Cumulative Growth: CPI", color="orange")
plt.title("Cumulative Growth of Median Income vs CPI Over Time")
plt.xlabel("Year")
plt.ylabel("Cumulative Growth")
plt.legend()
plt.savefig("cumulative_growth.png")
plt.show()

# Plot 4: Income-to-CPI Ratio
df_merged["income_to_cpi_ratio"] = df_merged["average_annual_median_income"] / df_merged["average_annual_cpi"]

plt.figure(figsize=(12, 6))
sns.lineplot(x="year", y="income_to_cpi_ratio", data=df_merged, label="Income-to-CPI Ratio", color="green")
plt.title("Income-to-CPI Ratio Over Time")
plt.xlabel("Year")
plt.ylabel("Income-to-CPI Ratio")
plt.axhline(df_merged["income_to_cpi_ratio"].mean(), color="red", linestyle="--", label="Average Ratio")
plt.legend()
plt.savefig("income_to_cpi_ratio.png")
plt.show()

# Plot 5: Scatter Plot of Income Growth vs CPI Growth
df_merged["income_pct_change"] = df_merged["average_annual_median_income"].pct_change() * 100
df_merged["cpi_pct_change"] = df_merged["average_annual_cpi"].pct_change() * 100

plt.figure(figsize=(12, 6))
sns.scatterplot(x="income_pct_change", y="cpi_pct_change", data=df_merged, color="purple")
plt.title("Annual Percentage Change: Income vs CPI")
plt.xlabel("Income Percentage Change (%)")
plt.ylabel("CPI Percentage Change (%)")
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.savefig("income_vs_cpi_scatter.png")
plt.show()

# Plot 6: Inflation-Adjusted Income vs Nominal Income
plt.figure(figsize=(12, 6))
sns.lineplot(x="year", y="average_annual_median_income", data=df_merged, label="Nominal Income", color="blue")
sns.lineplot(x="year", y="real_income", data=df_merged, label="Inflation-Adjusted Income (Real)", color="green")
plt.title("Nominal vs Inflation-Adjusted Median Income Over Time")
plt.xlabel("Year")
plt.ylabel("Income ($)")
plt.legend()
plt.savefig("nominal_vs_real_income.png")
plt.show()

# Plot 7: Decade Averages
df_merged["decade"] = (df_merged["year"] // 10) * 10
decade_avg = df_merged.groupby("decade")[["average_annual_median_income", "average_annual_cpi"]].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(x="decade", y="average_annual_median_income", data=decade_avg, color="blue", label="Median Income")
sns.barplot(x="decade", y="average_annual_cpi", data=decade_avg, color="orange", alpha=0.6, label="CPI")
plt.title("Average Median Income and CPI by Decade")
plt.xlabel("Decade")
plt.ylabel("Average Value")
plt.legend()
plt.savefig("decade_averages.png")
plt.show()

# Plot 8: Real Income Projections
X = df_merged["year"].values.reshape(-1, 1)
real_income_model = LinearRegression().fit(X, df_merged["real_income"].values.reshape(-1, 1))
future_years = np.arange(2024, 2031).reshape(-1, 1)
predicted_real_income = real_income_model.predict(future_years)

plt.figure(figsize=(12, 6))
sns.lineplot(x="year", y="real_income", data=df_merged, label="Actual Real Income", color="green")
plt.plot(future_years, predicted_real_income, "--", label="Projected Real Income (2024-2030)", color="red")
plt.title("Real Income (Adjusted for Inflation) with Future Projections")
plt.xlabel("Year")
plt.ylabel("Real Income ($)")
plt.legend()
plt.savefig("real_income_projections.png")
plt.show()
