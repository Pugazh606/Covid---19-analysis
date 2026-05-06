import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("covid_19_final_no_day_with_year_2020_2023.xlsx")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

plt.scatter(df["tests"], df["cases"], alpha=0.6)

plt.title("Tests vs Cases")
plt.xlabel("Tests")
plt.ylabel("Cases")

plt.show()