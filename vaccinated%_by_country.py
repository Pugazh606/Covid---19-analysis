import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("covid_19_final_no_day_with_year_2020_2023.xlsx")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

top_vax = df.sort_values(by="vaccination_%", ascending=False).head(10)

top_vax.plot(x="country", y="vaccination_%", kind="bar", color="green", figsize=(8,5))

plt.title("Top 10 Vaccination % Countries")
plt.xlabel("Country")
plt.ylabel("Vaccination %")
plt.xticks(rotation=45)

plt.show()