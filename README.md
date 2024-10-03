# Proyek Analisis Data dengan Streamlit

Proyek ini bertujuan untuk melakukan analisis dan visualisasi data penggunaan sepeda melalui sebuah dashboard interaktif yang dibangun menggunakan Streamlit.

## Persiapan Lingkungan

### 1. Setup Environment - Menggunakan Anaconda

1. Buat environment baru dengan Python versi 3.9:
    ```bash
    conda create --name main-ds python=3.9
    ```

2. Aktifkan environment yang telah dibuat:
    ```bash
    conda activate main-ds
    ```

3. Install dependencies yang diperlukan menggunakan `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### 2. Setup Environment - Menggunakan Shell/Terminal Biasa

1. Buat direktori baru untuk proyek ini:
    ```bash
    mkdir submision
    cd submision
    ```

2. Gunakan `pipenv` untuk mengelola environment virtual:
    ```bash
    pipenv install
    pipenv shell
    ```

3. Install dependencies yang diperlukan menggunakan `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## Menjalankan Proyek

### 1. Persiapan Data

Pastikan kamu sudah melakukan proses pembuatan data utama (`main_data.csv`) di Jupyter Notebook. File CSV ini akan digunakan untuk analisis pada dashboard Streamlit.

1. Jalankan notebook di Jupyter untuk memproses data, visualisasi, dan ekspor data ke dalam file `main_data.csv`.

2. Simpan file `main_data.csv` di direktori proyek.

### 2. Menjalankan Aplikasi Streamlit

1. Pastikan semua library sudah terinstall dengan benar dan file data sudah tersedia.

2. Untuk menjalankan aplikasi dashboard Streamlit, gunakan perintah berikut:
    ```bash
    streamlit run dashboard.py
    ```

3. Setelah aplikasi dijalankan, kamu bisa mengakses dashboard melalui browser di:
    ```text
    http://localhost:8501
    ```

## File dan Struktur Direktori

- `dashboard.py` - Script utama yang berisi kode untuk menampilkan dashboard dengan Streamlit.
- `main_data.csv` - Data yang diekspor dari Jupyter Notebook dan digunakan untuk analisis di dashboard.
- `requirements.txt` - Berkas yang berisi semua library dan dependencies yang diperlukan untuk menjalankan proyek.
- `README.md` - Berkas ini berisi instruksi untuk menjalankan proyek.

## Library yang Digunakan

- **pandas**: Untuk manipulasi dan analisis data.
- **numpy**: Untuk komputasi numerik.
- **matplotlib**: Untuk visualisasi data dasar.
- **seaborn**: Untuk visualisasi data statistik.
- **streamlit**: Untuk membangun aplikasi web dan dashboard interaktif.
- **scikit-learn**: Untuk analisis tambahan atau machine learning jika diperlukan.
- **plotly**: Untuk visualisasi interaktif di dashboard (opsional).

## Catatan

Pastikan seluruh dependency terinstall sebelum menjalankan aplikasi. Jika ada masalah dengan environment, kamu bisa menghapus environment lama dan membuat yang baru.

Selamat menganalisis dan semoga berhasil!
