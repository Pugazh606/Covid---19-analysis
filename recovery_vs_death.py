import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("covid_19_final_no_day_with_year_2020_2023.xlsx")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

plt.plot(df["recovered"], label="Recovered")
plt.plot(df["deaths"], label="Deaths")

plt.title("Recovered vs Deaths Trend")
plt.legend()
plt.show()