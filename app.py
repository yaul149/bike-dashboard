import streamlit as st
import pandas as pd

st.title("🚴 Bike Sharing Dashboard")

url_day = "https://raw.githubusercontent.com/yaul149/bike-dashboard/main/day.csv"
url_hour = "https://raw.githubusercontent.com/yaul149/bike-dashboard/main/hour.csv"

day = pd.read_csv(url_day)
hour = pd.read_csv(url_hour)


st.subheader("Dataset Day")
st.dataframe(day.head())

st.subheader("Dataset Hour")
st.dataframe(hour.head())


st.subheader("Distribusi Penyewaan Sepeda per Musim (Day)")
season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
day["season_name"] = day["season"].map(season_map)
st.bar_chart(day.groupby("season_name")["cnt"].mean())

st.subheader("Penyewaan Sepeda per Jam (Hour)")
st.line_chart(hour.groupby("hr")["cnt"].mean())


*Local URL: http://localhost:8501
  Network URL: http://192.168.43.33:8501*
