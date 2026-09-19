# Setup project di Windows

## Software yang perlu diinstal
1. **Git** - untuk version control dan push ke GitHub.
2. **Python 3.11+** - centang `Add Python to PATH` saat instalasi.
3. **Visual Studio Code** - editor utama; install extension Python dan Jupyter.
4. **PostgreSQL + pgAdmin 4** - untuk bagian SQL. MySQL boleh, tetapi file SQL project ini disiapkan untuk PostgreSQL.
5. **Power BI Desktop 64-bit** - untuk dashboard `.pbix`.
6. **Microsoft Excel** - untuk membuka `excel/maintenance_data_audit.xlsx` dan melakukan audit awal.

## Letakkan folder di mana?
Saran: `C:\Users\<nama-kamu>\Documents\Portfolio\building-maintenance-analysis`

Jangan taruh di folder Python atau PostgreSQL. Project cukup menjadi folder biasa di Documents/Portfolio.

## Langkah pertama
Buka PowerShell di folder project:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts\download_data.py
python scripts\clean_data.py
python scripts\run_eda.py
jupyter notebook
```
Lalu buka `notebooks/exploratory_analysis.ipynb`.

Jika PowerShell memblokir aktivasi venv, jalankan sekali:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## PostgreSQL
Buat database `maintenance_portfolio`. Buka Query Tool pgAdmin dan jalankan `sql/01_schema_postgresql.sql`. Untuk load CSV paling mudah gunakan psql dan file `sql/02_load_postgresql.sql`; ganti `<ABSOLUTE_PROJECT_PATH>` dengan path folder project. Setelah itu jalankan `sql/03_analysis_queries.sql`.

## Power BI
Ikuti `docs/POWER_BI_GUIDE_ID.md`. File PBIX dibuat dan disimpan oleh Power BI Desktop di folder `dashboard/`.

## GitHub
Di terminal:
```powershell
git init
git add .
git commit -m "Initial maintenance analytics portfolio project"
git branch -M main
git remote add origin https://github.com/USERNAME/building-maintenance-analysis.git
git push -u origin main
```
Ganti `USERNAME` dengan username GitHub kamu.

## Urutan demo saat interview
1. Tunjukkan README dan business question.
2. Buka Excel audit workbook untuk data-quality plan.
3. Buka notebook untuk cleaning + EDA.
4. Tunjukkan SQL dari basic aggregation sampai CTE/window function.
5. Buka Power BI untuk insight dan storytelling.
6. Jelaskan limitation: cost dan downtime tidak dibuat-buat karena source tidak menyediakannya.
