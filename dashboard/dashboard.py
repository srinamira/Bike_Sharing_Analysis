import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
day_data = pd.read_csv("day.csv")
hour_data = pd.read_csv("hour.csv")

# Dashboard title
st.title("Bike Sharing Dashboard")

# 1. Performa Pengguna Berdasarkan Hari Kerja dan Akhir Pekan
st.header("Performa Pengguna Berdasarkan Hari Kerja dan Akhir Pekan")
fig1, ax1 = plt.subplots(figsize=(8, 6))
sns.barplot(data=day_data, x="workingday", y="cnt", ci=None, palette=["#1f77b4", "#ff7f0e"], ax=ax1)
ax1.set_title("Performa Pengguna Berdasarkan Hari Kerja dan Akhir Pekan")
ax1.set_xlabel("Hari Kerja (1 = Ya, 0 = Tidak)")
ax1.set_ylabel("Jumlah Pengguna")
st.pyplot(fig1)

# 2. Pengaruh Cuaca terhadap Pengguna Sepeda
st.header("Pengaruh Cuaca terhadap Pengguna Sepeda")
fig2, ax2 = plt.subplots(figsize=(8, 6))
sns.boxplot(data=day_data, x="weathersit", y="cnt", palette="Set2", ax=ax2)
ax2.set_title("Pengaruh Cuaca terhadap Pengguna Sepeda")
ax2.set_xlabel("Kondisi Cuaca (1 = Baik, 2 = Sedang, 3 = Buruk)")
ax2.set_ylabel("Jumlah Pengguna")
st.pyplot(fig2)

# 3. Rata-rata Penggunaan Sepeda per Jam
st.header("Rata-rata Penggunaan Sepeda per Jam")
hourly_usage = hour_data.groupby('hr')['cnt'].mean().reset_index()
fig3, ax3 = plt.subplots(figsize=(12, 5))
sns.barplot(data=hourly_usage, x='hr', y='cnt', palette='viridis', ax=ax3)
ax3.set_title("Rata-rata Penggunaan Sepeda per Jam")
ax3.set_xlabel("Jam")
ax3.set_ylabel("Rata-rata Jumlah Pengguna")
st.pyplot(fig3)
