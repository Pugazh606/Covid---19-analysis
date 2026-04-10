import pandas as pd

df = pd.read_excel("covid_19_final_no_day_with_year_2020_2023.xlsx")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

total_vaccinated = df["vaccinated"].sum()

print("Total Vaccinated:", total_vaccinated)