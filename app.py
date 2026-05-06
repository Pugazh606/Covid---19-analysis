import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="COVID-19 Dashboard",
    page_icon="🦠",   # 👈 THIS changes the tab icon
    layout="wide"
)

# Background styling
st.markdown("""
    <style>
    .main {
        background-color: #F5F7FA;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>🦠 COVID-19 Analytics Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

# Load data
file_path = os.path.join(os.getcwd(), "covid_19_final_no_day_with_year_2020_2023.xlsx")
df = pd.read_excel(file_path)

# Clean columns
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Sidebar Filters
st.sidebar.header("🔍 Filters")

selected_continent = st.sidebar.multiselect(
    "Select Continent",
    options=df['continent'].unique(),
    default=df['continent'].unique()
)

selected_year = st.sidebar.multiselect(
    "Select Year",
    options=df['year'].unique(),
    default=df['year'].unique()
)

# Apply filters
df_filtered = df[
    (df['continent'].isin(selected_continent)) &
    (df['year'].isin(selected_year))
]

# KPIs
total_cases = int(df_filtered['cases'].sum())
total_deaths = int(df_filtered['deaths'].sum())
death_rate = (total_deaths / total_cases) * 100 if total_cases != 0 else 0

# KPI Cards (FINAL FIXED)
col1, col2, col3 = st.columns(3)

col1.markdown(f"""
<div style="
    background: linear-gradient(135deg, #E3F2FD, #BBDEFB);
    padding:20px;
    border-radius:12px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
">
    <h4 style="color:#0D47A1;">📊 Total Cases</h4>
    <h1 style="color:#000000;">{total_cases:,}</h1>
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div style="
    background: linear-gradient(135deg, #FFEBEE, #FFCDD2);
    padding:20px;
    border-radius:12px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
">
    <h4 style="color:#B71C1C;">💀 Total Deaths</h4>
    <h1 style="color:#000000;">{total_deaths:,}</h1>
</div>
""", unsafe_allow_html=True)

col3.markdown(f"""
<div style="
    background: linear-gradient(135deg, #FFF3E0, #FFE0B2);
    padding:20px;
    border-radius:12px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
">
    <h4 style="color:#E65100;">⚠️ Death Rate</h4>
    <h1 style="color:#000000;">{death_rate:.2f}%</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Charts Row 1
col1, col2 = st.columns(2)

with col1:
    st.subheader("🌍 Cases by Continent")
    cases_continent = df_filtered.groupby('continent')['cases'].sum().reset_index()

    fig = px.bar(
        cases_continent,
        x='continent',
        y='cases',
        color='continent',
        title="Cases Distribution",
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("💀 Deaths by Continent")
    deaths_continent = df_filtered.groupby('continent')['deaths'].sum().reset_index()

    fig = px.pie(
        deaths_continent,
        names='continent',
        values='deaths',
        title="Deaths Share",
        hole=0.4
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Charts Row 2
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Year-wise Cases Trend")
    year_cases = df_filtered.groupby('year')['cases'].sum().reset_index()

    fig = px.line(
        year_cases,
        x='year',
        y='cases',
        markers=True,
        title="Growth Trend",
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📊 Cases vs Deaths")
    fig = px.scatter(
        df_filtered,
        x='cases',
        y='deaths',
        color='continent',
        title="Cases vs Deaths Correlation",
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Footer
st.markdown(
    "<center>✨ Developed by Pugazh | Power BI Style Dashboard</center>",
    unsafe_allow_html=True
)
