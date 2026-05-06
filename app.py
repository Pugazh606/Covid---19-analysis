import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")

# Title
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🦠 COVID-19 Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

# Load data
df = pd.read_excel("covid_19_final_no_day_with_year_2020_2023.xlsx")

# Clean columns
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Metrics
total_cases = int(df['cases'].sum())
total_deaths = int(df['deaths'].sum())
death_rate = (total_deaths / total_cases) * 100

# KPI Section
col1, col2, col3 = st.columns(3)

col1.metric("📊 Total Cases", f"{total_cases:,}")
col2.metric("💀 Total Deaths", f"{total_deaths:,}")
col3.metric("⚠️ Death Rate (%)", f"{death_rate:.2f}%")

st.markdown("---")

# Charts Section
col1, col2 = st.columns(2)

# Cases by Continent
with col1:
    st.subheader("🌍 Cases by Continent")
    cases_continent = df.groupby('continent')['cases'].sum()

    fig, ax = plt.subplots()
    ax.bar(cases_continent.index, cases_continent.values)
    ax.set_xlabel("Continent")
    ax.set_ylabel("Cases")
    ax.set_title("Cases Distribution")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Deaths by Continent
with col2:
    st.subheader("💀 Deaths by Continent")
    deaths_continent = df.groupby('continent')['deaths'].sum()

    fig, ax = plt.subplots()
    ax.bar(deaths_continent.index, deaths_continent.values)
    ax.set_xlabel("Continent")
    ax.set_ylabel("Deaths")
    ax.set_title("Deaths Distribution")
    plt.xticks(rotation=45)
    st.pyplot(fig)

st.markdown("---")

# Year-wise trend
st.subheader("📈 Year-wise Cases Trend")

year_cases = df.groupby('year')['cases'].sum()

fig, ax = plt.subplots()
ax.plot(year_cases.index, year_cases.values, marker='o')
ax.set_xlabel("Year")
ax.set_ylabel("Cases")
ax.set_title("Yearly Growth of Cases")

st.pyplot(fig)

st.markdown("---")

# Footer
st.markdown(
    "<center>✨ Developed by Pugazh | COVID-19 Data Analysis Project</center>",
    unsafe_allow_html=True
)
