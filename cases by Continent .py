import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("covid_19_final_no_day_with_year_2020_2023.xlsx")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

continent_data = df.groupby("continent")["cases"].sum()
continent_data.plot(kind='pie', autopct='%1.1f%%')
plt.title("Cases by Continent")
plt.ylabel("")
plt.show()