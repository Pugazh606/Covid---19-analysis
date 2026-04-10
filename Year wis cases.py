import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("covid_19_final_no_day_with_year_2020_2023.xlsx")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

year_data = df.groupby("year")["cases"].sum()
year_data.plot(kind='line')
plt.title("Year-wise COVID Cases")
plt.xlabel("Year")
plt.ylabel("Total Cases")
plt.show() 