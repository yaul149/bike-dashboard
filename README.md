# Proyek Analisis Data: [Bike-sharing-dataset]
- **Nama:** [naufal dhiyaul ikhsan]
- **Email:** [naufalhayyu146@gmail.com]
- **ID Dicoding:** [53XEKN5NVXRN]

## Menentukan Pertanyaan Bisnis
- bagaimana pengaruh musim pada bisnis penyewaan sepeda?
- hasil dari pengguna mana yang menunjukan anggka lebih besar apakah pengguna tetap(registered) atau non tetap(casual)?
## Import Semua Packages/Library yang Digunakan
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


## Data Wrangling
### Gathering Data
from google.colab import files
uploaded = files.upload()

import zipfile

with zipfile.ZipFile("Bike-sharing-dataset.zip", "r") as zip_ref:
    zip_ref.extractall("Bike-sharing-dataset")

df = pd.read_csv("Bike-sharing-dataset/day.csv")
print(df.head(100))

pd.options.display.float_format = '{:.2f}'.format
print(df.describe())

from google.colab import files
uploaded = files.upload()

import zipfile

with zipfile.ZipFile("Bike-sharing-dataset.zip", "r") as zip_ref:
    zip_ref.extractall("Bike-sharing-dataset")

df = pd.read_csv("Bike-sharing-dataset/day.csv")
print(df.head(100))

pd.options.display.float_format = '{:.2f}'.format
print(df.describe())


# Baca data hour.csv
df_hour = pd.read_csv("Bike-sharing-dataset/hour.csv")
print("\nDataset hour.csv")
print(df_hour.head(100))
print(df_hour.shape)

# Membaca hour dan day csv
import pandas as pd

# Membaca file day.csv
df_day = pd.read_csv("Bike-sharing-dataset/day.csv")
print("Preview data harian (day.csv):")
print(df_day.head(100))
print("Ukuran data harian:", df_day.shape)

# Membaca file hour.csv
df_hour = pd.read_csv("Bike-sharing-dataset/hour.csv")
print("\nPreview data per jam (hour.csv):")
print(df_hour.head(100))
print("Ukuran data per jam:", df_hour.shape)

df_day['data_type'] = 'day'
df_hour['data_type'] = 'hour'

if 'hr' not in df_day.columns:
    df_day['hr'] = None


df_day = df_day[df_hour.columns]

# Gabungkan keduanya
df_all = pd.concat([df_day, df_hour], ignore_index=True)

print("\nPreview data gabungan:")
print(df_all.head(100))
print("Ukuran data gabungan:", df_all.shape)

**Insight:**
- sebelum menjalankan/membaca file saya harus mengestraknya terlebih dahulu meskipun mencari dari sumber lain saya menjadi tau cara untuk membaca file zip di goole colab

 **insight bisnis:**
 - terdapat 731 hari dalam data namun mengambil 100 hari pertama
 - pada data tersebut musim, cuaca, dan suhu serta beberapa hal lain yang berperngaruh terhadap faktor menigkatnya bisnis.
### Assessing Data
print(df.isnull().sum())
print("Duplicated:", df.duplicated().sum())
**Insight:**
- tidak ada missing data yang terjadi pada 100 baris teratas
- tidak ada duplicate data

# Membaca file hour.csv
import pandas as pd


df_hour = pd.read_csv("Bike-sharing-dataset/hour.csv")


print("Preview data per jam (hour.csv):")
print(df_hour.head(100))
print("\nUkuran data:", df_hour.shape)


print("\nInformasi dataset:")
print(df_hour.info())


print("\nStatistik deskriptif:")
print(df_hour.describe())

### Cleaning Data
mengecek duplikasi pada data
print("Jumlah duplikasi sebelum:", df.duplicated().sum())
df = df.drop_duplicates()
print("Jumlah duplikasi sesudah:", df.duplicated().sum())
print(df.isnull().sum())
df = df.dropna()


**Insight:**
-  tidak terdapat duplikasi pada data yang di olah
- hasil dari data bertype integer
# clening data hour csv

Cek missing values → lihat apakah ada kolom yang kosong.

Cek duplikasi → data jam bisa saja tercatat lebih dari sekali.

Cleaning:

drop_duplicates() → hapus duplikat

fillna() → isi missing values dengan median (aman untuk numerik)

to_datetime() → konversi kolom tanggal ke format datetime

Validasi ulang → pastikan data sudah bersih.
import pandas as pd


df_hour = pd.read_csv("Bike-sharing-dataset/hour.csv")

print("Preview awal:")
print(df_hour.head())


print("\nCek missing values:")
print(df_hour.isnull().sum())
print("\nJumlah duplikasi:", df_hour.duplicated().sum())

df_hour = df_hour.drop_duplicates()
df_hour = df_hour.fillna(df_hour.median(numeric_only=True))
df_hour['dteday'] = pd.to_datetime(df_hour['dteday'])


print("\nCek ulang missing values:")
print(df_hour.isnull().sum())

print("\nJumlah duplikasi setelah dibersihkan:", df_hour.duplicated().sum())

print("\nInfo dataset setelah cleaning:")
print(df_hour.info())

## Exploratory Data Analysis (EDA)
### Explore ...

print(df['season'].value_counts())

print(df['yr'].value_counts())

print(df['mnth'].value_counts())

print(df['holiday'].value_counts())

print(df['weekday'].value_counts())

print(df['workingday'].value_counts())

print(df['weathersit'].value_counts())

print(df['casual'].value_counts())

print(df['registered'].value_counts())

**Insight:**
- Mayoritas pengguna adalah registered.

- Faktor musim, cuaca, hari kerja/libur kemungkinan besar memengaruhi jumlah peminjam.

## Visualization & Explanatory Analysis
### Pertanyaan 1:
***apakah musim memperngaruhhi pengunjung?:***

plt.figure(figsize=(7,5))

sns.boxplot(x='season', y='cnt', data=df)

plt.title("Distribusi Jumlah Pengguna per Musim")

plt.xlabel("Musim (1:Spring, 2:Summer, 3:Fall, 4:Winter)")

plt.ylabel("Jumlah Pengguna")

plt.show()

lebih banyak mana antara pengguna tetap dengan pengguna non tetap?
plt.figure(figsize=(7,5))
sns.barplot(
    x=['Casual', 'Registered'],
    y=[df['casual'].mean(), df['registered'].mean()],
    palette="Set2"
)
plt.title("Rata-rata Jumlah Pengguna: Casual vs Registered")
plt.ylabel("Jumlah Pengguna (rata-rata)")
plt.show()

**Insight:**
- dari visual data pertama terlihat bahwa musim memperngaruhi pengunjung dari musim gugur, disusul musim panas, musim dingin, dan musim semi
- pendapatan terbesar datang dari pengunjung tetap.
import matplotlib.pyplot as plt
import seaborn as sns

print("Shape dataset:", df_hour.shape)

print("\nStatistik deskriptif:")

print(df_hour.describe())


plt.figure(figsize=(8,5))

sns.lineplot(data=df_hour, x="hr", y="cnt", ci=None)

plt.title("Rata-rata Jumlah Peminjaman Sepeda per Jam", fontsize=14)

plt.xlabel("Jam (0-23)")

plt.ylabel("Jumlah peminjaman")

plt.grid(True)

plt.show()

daily_trend = df_hour.groupby("dteday")["cnt"].sum()

plt.figure(figsize=(8,5))

daily_trend.plot()

plt.title("Tren Jumlah Peminjaman Sepeda Harian", fontsize=14)

plt.xlabel("Tanggal")

plt.ylabel("Jumlah peminjaman")

plt.grid(True)

plt.show()

plt.figure(figsize=(8,5))

sns.boxplot(data=df_hour, x="season", y="cnt")

plt.title("Distribusi Peminjaman Sepeda Berdasarkan Musim", fontsize=14)

plt.xlabel("Musim (1=semi, 2=panas, 3=gugur, 4=dingin)")

plt.ylabel("Jumlah peminjaman")

plt.show()

plt.figure(figsize=(8,5))

sns.barplot(data=df_hour, x="workingday", y="cnt", estimator="mean")

plt.title("Rata-rata Peminjaman: Hari Kerja vs Libur", fontsize=14)

plt.xlabel("Workingday (0=libur, 1=hari kerja)")

plt.ylabel("Rata-rata peminjaman")

plt.show()

plt.figure(figsize=(8,5))

sns.heatmap(df_hour.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Heatmap Korelasi Variabel Numerik", fontsize=14)

plt.show()

# insight
- biasanya hari kerja lebih tinggi karena orang pakai sepeda untuk commuting.
- musim panas/gugur biasanya lebih tinggi dibanding musim dingin.
## Analisis Lanjutan (Opsional)

avg_season_day = df_day.groupby("season")["cnt"].mean()

print("Rata-rata peminjaman per musim:")

print(avg_season_day)

avg_workingday_day = df_day.groupby("workingday")["cnt"].mean()

print("\nRata-rata peminjaman hari kerja (1) vs libur (0):")

print(avg_workingday_day)

avg_month_day = df_day.groupby("mnth")["cnt"].mean()

plt.figure(figsize=(12,6))

avg_month_day.plot(kind="bar", color="skyblue")


plt.title("Rata-rata Peminjaman per Bulan", fontsize=14)

plt.xlabel("Bulan (1=Jan, 12=Des)")

plt.ylabel("Rata-rata peminjaman")

plt.xticks(rotation=0)

plt.show()

avg_weather_day = df_day.groupby("weathersit")["cnt"].mean()

print("\nRata-rata peminjaman berdasarkan kondisi cuaca:")

print(avg_weather_day)

plt.figure(figsize=(8,6))

sns.barplot(x="weathersit", y="cnt", data=df_day, estimator="mean")

plt.title("Rata-rata Peminjaman Sepeda Berdasarkan Cuaca", fontsize=14)

plt.xlabel("Kondisi Cuaca (1=baik, 2=berawan, 3=hujan, 4=ekstrem)")

plt.ylabel("Rata-rata peminjaman")

plt.show()



plt.figure(figsize=(10,6))

sns.lineplot(x="dteday", y="cnt", data=df_day)

plt.title("Tren Peminjaman Sepeda dari Waktu ke Waktu", fontsize=14)

plt.xlabel("Tanggal")

plt.ylabel("Jumlah peminjaman")

plt.show()

# hour csv

# 1. Rata-rata peminjaman sepeda per musim

avg_season = df_hour.groupby("season")["cnt"].mean()

print("Rata-rata peminjaman per musim:")

print(avg_season)

# 2. Rata-rata peminjaman sepeda per hari kerja vs libur

avg_workingday = df_hour.groupby("workingday")["cnt"].mean()

print("\nRata-rata peminjaman hari kerja (1) vs libur (0):")

print(avg_workingday)


# 3. Rata-rata peminjaman per jam di hari kerja vs libur

avg_hour_daytype = df_hour.groupby(["workingday","hr"])["cnt"].mean().unstack(0)

plt.figure(figsize=(12,6))

avg_hour_daytype[0].plot(label="Libur")

avg_hour_daytype[1].plot(label="Hari Kerja")

plt.title("Rata-rata Peminjaman per Jam: Libur vs Hari Kerja", fontsize=14)

plt.xlabel("Jam (0-23)")


plt.ylabel("Jumlah Peminjaman")

plt.legend()

plt.grid(True)

plt.show()

# 4. Pengaruh cuaca terhadap peminjaman

avg_weather = df_hour.groupby("weathersit")["cnt"].mean()

print("\nRata-rata peminjaman berdasarkan kondisi cuaca:")

print(avg_weather)

plt.figure(figsize=(8,6))

sns.barplot(x="weathersit", y="cnt", data=df_hour, estimator="mean")

plt.title("Rata-rata Peminjaman Sepeda Berdasarkan Cuaca", fontsize=14)


plt.xlabel("Kondisi Cuaca (1=baik, 2=berawan, 3=hujan, 4=ekstrem)")

plt.ylabel("Rata-rata peminjaman")

plt.show()

# 5. Korelasi suhu dengan jumlah peminjaman
plt.figure(figsize=(8,6))

sns.scatterplot(x="temp", y="cnt", data=df_hour, alpha=0.3)

plt.title("Hubungan Suhu dengan Jumlah Peminjaman", fontsize=14)

plt.xlabel("Suhu (normalized)")

plt.ylabel("Jumlah peminjaman")

plt.show()

# insight

Musim → peminjaman tertinggi biasanya di musim panas/gugur.

Hari kerja vs libur → pola berbeda: hari kerja puncaknya pagi & sore (commuting), libur lebih merata sepanjang hari.

Cuaca → cuaca buruk (hujan/ekstrem) menurunkan jumlah peminjaman drastis.

Suhu → ada korelasi positif: makin hangat → makin banyak orang bersepeda.
# download hasil dari pengolahan data yang dibuat

import os

os.listdir()
# Buat arsip zip dari folder data_unzip

import shutil

from google.colab import files

shutil.make_archive("bike_data", 'zip', "data_unzip")

# Download hasil zip
files.download("bike_data.zip")
[Proyek Analisis Data_ [Bike-sharing-dataset].md](https://github.com/user-attachments/files/22578528/Proyek.Analisis.Data_.Bike-sharing-dataset.md)
