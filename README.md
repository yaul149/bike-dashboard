#  Bike Sharing Dataset Analysis

## 1. Data Gathering
- Dataset terdiri dari 4 tabel utama:
  - **Orders DF** → `hour.csv`
  - **Products DF** → `day.csv`
  - **Customers DF** → kolom `casual`, `registered`
  - **Sales DF** → kolom `cnt_sales`
- Sumber data: Bike Sharing Dataset (UCI Repository)

---

## 2. Data Assessing
- **Missing Values**: Tidak ditemukan nilai kosong.
- **Duplicates**: Tidak ditemukan duplikasi signifikan.
- **Data Types**: Sudah sesuai (tanggal → datetime, angka → numerik).

---

## 3. Data Cleaning
- Rename kolom untuk konsistensi (`cnt` → `cnt_sales`).
- Pastikan format tanggal (`dteday`) sudah dalam `datetime`.
- Dataset siap dipakai untuk analisis.

---

## 4. Exploratory Data Analysis (EDA)

### Customers DF
- Rata-rata pelanggan **casual** meningkat tajam di musim panas.
- Pelanggan **registered** cenderung stabil sepanjang tahun.

### Sales DF
- Penjualan (total rental) tertinggi di musim panas.
- Musim dingin menunjukkan penurunan signifikan.

### Orders & Products DF
- Pola peminjaman sepeda meningkat pada jam sibuk (pagi & sore).
- Hari kerja → pengguna terdaftar (registered).
- Akhir pekan → pengguna casual lebih dominan.

---

## 5. Visualisasi
- Tren musiman (musim panas vs musim dingin).
- Tren harian (weekday vs weekend).
- Perbandingan casual vs registered.
- Distribusi peminjaman per jam.

---

## 6. RFM Analysis
- **Recency**: Mayoritas pelanggan baru saja menggunakan layanan.
- **Frequency**: Sebagian besar menggunakan layanan dengan frekuensi sedang.
- **Monetary**: Ada segmen kecil dengan nilai transaksi tinggi.
- Segmentasi: Best Customers, Loyal Customers, Potential Loyalist, At Risk.

---

