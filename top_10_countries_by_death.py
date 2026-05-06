import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("covid_19_final_no_day_with_year_2020_2023.xlsx")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

top_deaths = df.groupby("country")["deaths"].sum().sort_values(ascending=False).head(10)

top_deaths.plot(kind='bar', color='red', figsize=(8,5))
plt.title("Top 10 Countries by Deaths")
plt.xlabel("Country")
plt.ylabel("Deaths")
plt.xticks(rotation=45)
plt.show()