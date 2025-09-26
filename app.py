
import streamlit as st
import pandas as pd

st.title("🚴 Bike Sharing Dashboard")

# load dataset
df = pd.read_csv("day.csv")

st.subheader("Preview Data")
st.write(df.head())

st.subheader("Statistik Data")
st.write(df.describe())

# contoh grafik
st.subheader("Tren Penyewaan Sepeda Harian")
st.line_chart(df['cnt'])
