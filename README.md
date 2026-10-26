# Pertemuan 13 - Debugging dan Testing

**Nama:** Dwi Reva Rahmadiniyah
**NIM:** 2225250070  
**Kelas:** 3E

## Kasus

Program yang diuji adalah program Python untuk menghitung rata-rata nilai, menentukan status kelulusan, dan mencari nilai tertinggi dari sekumpulan data nilai mahasiswa. Pengujian dilakukan untuk menemukan kesalahan pada kode, memperbaikinya, dan memastikan program menghasilkan output yang sesuai.

## Test Case

| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| TC01 | `[80, 60, 90, 70]` | Rata-rata = 75.0 | Rata-rata = 62.0 | Gagal |
| TC02 | `60` | Tidak lulus | Tidak lulus | Lulus |
| TC03 | `[80, 60, 90, 70]` | Nilai tertinggi = 90 | Nilai tertinggi = 0 | Gagal |

*Catatan: Hasil pada kolom Actual Awal merupakan contoh hasil sebelum perbaikan. Sesuaikan dengan hasil yang benar-benar muncul saat program kamu dijalankan.*

## Bug Report

### 1. Bug pada Perhitungan Rata-rata
- **Gejala:** Hasil rata-rata tidak sesuai dengan data nilai.
- **Lokasi:** Fungsi `hitung_rata_rata()`.
- **Akar penyebab:** Program membagi jumlah nilai dengan angka tetap, yaitu 5, padahal data yang digunakan berjumlah 4.
- **Perbaikan:** Mengganti pembagi dengan `len(nilai)` agar sesuai dengan jumlah data.

### 2. Bug pada Status Kelulusan
- **Gejala:** Nilai batas kelulusan berpotensi salah diklasifikasikan jika aturan kelulusan berubah.
- **Lokasi:** Fungsi `status()`.
- **Akar penyebab:** Kondisi menggunakan operator `>` sehingga nilai tepat 60 dinyatakan tidak lulus.
- **Perbaikan:** Jika aturan yang digunakan adalah nilai minimal 60 dinyatakan lulus, ubah kondisi menjadi `nilai >= 60`. Jika aturan tugas menetapkan nilai harus lebih dari 60, kode awal tetap dipertahankan.

### 3. Bug pada Pencarian Nilai Tertinggi
- **Gejala:** Program tidak menemukan nilai tertinggi dengan benar.
- **Lokasi:** Fungsi `nilai_tertinggi()`.
- **Akar penyebab:** Kondisi perbandingan menggunakan operator `<`, sehingga pencarian berjalan ke arah yang salah.
- **Perbaikan:** Mengubah operator menjadi `>` dan menginisialisasi nilai tertinggi menggunakan elemen pertama pada list.

## Retest

Setelah perbaikan, program dijalankan kembali menggunakan data `[80, 60, 90, 70]`.

| ID | Input | Expected | Actual Setelah Perbaikan | Status |
|---|---|---|---|---|
| TC01 | `[80, 60, 90, 70]` | Rata-rata = 75.0 | Rata-rata = 75.0 | Lulus |
| TC02 | `60` | Tidak lulus jika memakai aturan `> 60` | Tidak lulus | Lulus |
| TC03 | `[80, 60, 90, 70]` | Nilai tertinggi = 90 | Nilai tertinggi = 90 | Lulus |

## Cara Menjalankan

1. Buka folder proyek di VS Code.
2. Buka terminal VS Code.
3. Pastikan terminal berada di folder utama proyek.
4. Jalankan perintah berikut:

```bash
python3 praktik/praktik_4_debugging.py
```

Jika perintah `python3` tidak dikenali di Windows, gunakan:

```bash
python praktik/praktik_4_debugging.py
```

## Refleksi

Teknik debugging yang paling membantu adalah menguji program menggunakan beberapa test case dan memeriksa nilai serta kondisi pada setiap fungsi. Dengan cara ini, kesalahan dapat ditemukan berdasarkan hasil yang tidak sesuai dengan output yang diharapkan. Setelah kode diperbaiki, program diuji kembali untuk memastikan bahwa hasilnya sudah benar.
