import pandas as pd

df = pd.read_excel("covid_19_final_no_day_with_year_2020_2023.xlsx")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

total_cases = df["cases"].sum()
total_deaths = df["deaths"].sum()
total_recovered = df["recovered"].sum()

print("Total Cases:", total_cases)
print("Total Deaths:", total_deaths)
print("Total Recovered:", total_recovered)