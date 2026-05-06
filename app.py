import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("covid_19_final_no_day_with_year_2020_2023.xlsx")

# Clean columns
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Metrics
total_cases = df['cases'].sum()
total_deaths = df['deaths'].sum()
death_rate = (total_deaths / total_cases) * 100

# Title
st.title("COVID-19 Dashboard")

# KPI Metrics
st.metric("Total Cases", total_cases)
st.metric("Total Deaths", total_deaths)
st.metric("Death Rate (%)", round(death_rate, 2))

# Cases by Continent
st.subheader("Cases by Continent")
cases_continent = df.groupby('continent')['cases'].sum()
st.bar_chart(cases_continent)

# Deaths by Continent
st.subheader("Deaths by Continent")
deaths_continent = df.groupby('continent')['deaths'].sum()
st.bar_chart(deaths_continent)

# Year-wise trend
st.subheader("Year-wise Cases Trend")
year_cases = df.groupby('year')['cases'].sum()
st.line_chart(year_cases)