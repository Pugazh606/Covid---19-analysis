import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="COVID-19 Dashboard",
    page_icon="🦠",   # 👈 THIS changes the tab icon
    layout="wide"
)

st.title("🦠 COVID-19 Global Analytics Dashboard")

# =========================
# LOAD DATA
# =========================
df = pd.read_excel("covid_19_final_no_day_with_year_2020_2023.xlsx")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# =========================
# KPI CALCULATION
# =========================
total_cases = df["cases"].sum()
total_recovered = df["recovered"].sum()
total_deaths = df["deaths"].sum()
total_vaccinated = df["vaccinated"].sum()
total_tests = df["tests"].sum()

recovery_rate = (total_recovered / total_cases) * 100
death_rate = (total_deaths / total_cases) * 100

# =========================
# KPI CARDS (STYLED DASHBOARD)
# =========================

col1, col2, col3, col4, col5 = st.columns(5)

# -------------------------
col1.markdown(f"""
<div style="
    background: linear-gradient(135deg, #E3F2FD, #BBDEFB);
    padding:18px;
    border-radius:12px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    text-align:center;
">
    <h4 style="color:#0D47A1;">📊 Total Cases</h4>
    <h2 style="color:#000;">{total_cases:,.0f}</h2>
</div>
""", unsafe_allow_html=True)

# -------------------------
col2.markdown(f"""
<div style="
    background: linear-gradient(135deg, #E8F5E9, #C8E6C9);
    padding:18px;
    border-radius:12px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    text-align:center;
">
    <h4 style="color:#1B5E20;">💚 Recovered</h4>
    <h2 style="color:#000;">{total_recovered:,.0f}</h2>
</div>
""", unsafe_allow_html=True)

# -------------------------
col3.markdown(f"""
<div style="
    background: linear-gradient(135deg, #FFEBEE, #FFCDD2);
    padding:18px;
    border-radius:12px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    text-align:center;
">
    <h4 style="color:#B71C1C;">💀 Deaths</h4>
    <h2 style="color:#000;">{total_deaths:,.0f}</h2>
</div>
""", unsafe_allow_html=True)

# -------------------------
col4.markdown(f"""
<div style="
    background: linear-gradient(135deg, #FFF8E1, #FFECB3);
    padding:18px;
    border-radius:12px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    text-align:center;
">
    <h4 style="color:#FF6F00;">📈 Recovery %</h4>
    <h2 style="color:#000;">{recovery_rate:.2f}%</h2>
</div>
""", unsafe_allow_html=True)

# -------------------------
col5.markdown(f"""
<div style="
    background: linear-gradient(135deg, #F3E5F5, #E1BEE7);
    padding:18px;
    border-radius:12px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    text-align:center;
">
    <h4 style="color:#6A1B9A;">⚠️ Death %</h4>
    <h2 style="color:#000;">{death_rate:.2f}%</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================
# FILTERS
# =========================

col1, col2, col3 = st.columns(3)

with col1:
    continent = st.selectbox(
        "🌍 Select Continent",
        ["All"] + sorted(df["continent"].dropna().unique())
    )

with col2:
    country = st.selectbox(
        "🏳️ Select Country",
        ["All"] + sorted(df["country"].dropna().unique())
    )

with col3:
    year = st.selectbox(
        "📅 Select Year",
        ["All"] + sorted(df["year"].dropna().unique())
    )

# =========================
# FILTER LOGIC (SAFE)
# =========================
data = df.copy()

if continent != "All":
    data = data[data["continent"] == continent]

if country != "All":
    data = data[data["country"] == country]

if year != "All":
    data = data[data["year"] == year]

# =========================
# ROW 1 - WORLD + CONTINENT
# =========================
col1, col2 = st.columns(2)

with col1:
    fig1 = px.choropleth(
        df,
        locations="country",
        locationmode="country names",
        color="cases",
        title="🌍 Global COVID-19 Cases Map",
        color_continuous_scale="Reds"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    continent_data = df.groupby("continent")["cases"].sum().reset_index()

    fig2 = px.pie(
        continent_data,
        values="cases",
        names="continent",
        title="🌎 Cases by Continent",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    st.plotly_chart(fig2, use_container_width=True)

# =========================
# ROW 2 - CASES & DEATHS
# =========================
col3, col4 = st.columns(2)

with col3:
    top_cases = df.groupby("country")["cases"].sum().sort_values(ascending=False).head(10).reset_index()

    fig3 = px.bar(
        top_cases,
        x="country",
        y="cases",
        title="📊 Top 10 Countries by Cases",
        color="cases",
        color_continuous_scale="Blues"
    )
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    top_deaths = df.groupby("country")["deaths"].sum().sort_values(ascending=False).head(10).reset_index()

    fig4 = px.bar(
        top_deaths,
        x="country",
        y="deaths",
        title="💀 Top 10 Countries by Deaths",
        color="deaths",
        color_continuous_scale="Reds"
    )
    st.plotly_chart(fig4, use_container_width=True)

# =========================
# ROW 3 - ANALYTICS
# =========================
col5, col6 = st.columns(2)

with col5:
    fig5 = px.scatter(
        data,
        x="recovered",
        y="deaths",
        size="cases",
        color="continent",
        hover_name="country",
        title="📈 Recovery vs Death Analysis"
    )
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    top_vax = df.sort_values(by="vaccination_%", ascending=False).head(10)

    fig6 = px.bar(
        top_vax,
        x="country",
        y="vaccination_%",
        title="💉 Top Vaccinated Countries",
        color="vaccination_%",
        color_continuous_scale="Greens"
    )
    st.plotly_chart(fig6, use_container_width=True)

# =========================
# ROW 4 - TESTING ANALYSIS
# =========================
fig7 = px.scatter(
    data,
    x="tests",
    y="cases",
    color="continent",
    hover_name="country",
    title="🧪 Tests vs Cases Relationship"
)

st.plotly_chart(fig7, use_container_width=True)

# =========================
# TABLE VIEW
# =========================
st.markdown("### 📋 Dataset Preview")
st.dataframe(data)