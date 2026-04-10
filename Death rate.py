import pandas as pd

df = pd.read_excel("covid_19_final_no_day_with_year_2020_2023.xlsx")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

death_rate = (df["deaths"].sum() / df["cases"].sum()) * 100

print("Overall Death Rate (%):", death_rate)