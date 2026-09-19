# Panduan Power BI Desktop

## 1. Instalasi
Unduh Power BI Desktop dari Microsoft Store atau halaman resmi Microsoft. Gunakan versi 64-bit.

## 2. Siapkan data
Jalankan lebih dulu:
```powershell
python scripts/download_data.py
python scripts/clean_data.py
```
Pastikan folder `data/processed/` sudah berisi CSV hasil cleaning.

## 3. Import
Power BI Desktop -> Get Data -> Text/CSV. Import `machines_clean.csv`, `maintenance_clean.csv`, `failures_clean.csv`, `errors_clean.csv`, dan `telemetry_clean.csv`.

## 4. Model
Di Model View buat relasi:
- machines[machineID] 1 -> * maintenance[machineID]
- machines[machineID] 1 -> * failures[machineID]
- machines[machineID] 1 -> * errors[machineID]
- machines[machineID] 1 -> * telemetry[machineID]

Cross-filter direction: Single.

## 5. Measures
Modeling -> New measure. Salin satu per satu isi `dashboard/power_bi_measures.dax`. Format `Reactive Rate` dan `Proactive Rate` sebagai Percentage.

## 6. Halaman 1 - Executive Overview
Buat 5 Card: Total Maintenance, Total Failures, Unique Assets, Reactive Rate, Proactive Rate. Tambahkan line chart dengan `maintenance[month]` di X-axis dan Total Maintenance; buat line chart kedua untuk `failures[month]` dan Total Failures atau gunakan date table jika ingin satu visual. Tambahkan bar chart model vs Total Failures.

## 7. Halaman 2 - Asset Performance
Bar chart: machineID vs Total Failures, filter Top N = 10. Matrix: model -> component dengan maintenance/failure measures. Scatter: age vs failure count, Details = machineID. Tambahkan slicer model dan machineID.

## 8. Halaman 3 - Operational Signals
Line chart untuk average volt/rotate/pressure/vibration terhadap month. Bar chart errorID vs Total Errors. Tambahkan table machineID, model, age, Total Failures, Total Maintenance, Total Errors.

## 9. Simpan
Simpan sebagai `dashboard/maintenance_dashboard.pbix`. Export 3 halaman ke PDF/PNG untuk preview portofolio, dan taruh screenshot terbaik di `images/dashboard-preview.png`.

## Catatan integritas
Jangan tambahkan maintenance cost atau downtime buatan. Dataset sumber tidak menyediakan kedua field itu. Di README jelaskan bahwa scope KPI disesuaikan dengan data yang benar-benar tersedia.
