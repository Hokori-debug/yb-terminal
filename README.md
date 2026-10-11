# YB Quest Terminal 📟

Aplikasi web statis bergaya **Alternate Reality Game (ARG)** untuk teka-teki buku tahunan (Yearbook / YB).
Aplikasi ini berjalan murni di sisi klien (*Client-Side*), sangat ringan, tanpa dependensi server atau database eksternal, sehingga **dijamin tahan lama hingga 10+ tahun ke depan tanpa biaya pemeliharaan** (cocok untuk GitHub Pages).

---

## 🎯 Alur Pengguna (User Flow)

```
[Buku Tahunan Cetak] 
         │ (Teks Base64 / QR Code)
         ▼
[Dekripsi Base64 -> URL Terminal] 
         │
         ▼
[Tahap 1: Autentikasi Awal] ──(Sandi Instagram)──► [Validasi Uppercase]
         │
         ▼ (Jika Benar)
[Tahap 2: Galeri Clue Blur] ──(Tebak Objek)──────► [Pencocokan Object Mapping]
         │                                               │
         ├──────────────┬──────────────┤                 │
      [LABKOM]       [KANTIN]      [ROOFTOP]             ▼
         │              │              │          (Jika Benar)
         ▼              ▼              ▼                 │
[Tahap 3: Pemutaran Video YouTube Unlisted Sesuai Jalur Objek]
```

---

## 🚀 Cara Menjalankan

### 1. Menjalankan Secara Lokal (Offline / Komputer Anda)
Cukup **klik dua kali** file `index.html` untuk langsung membukanya di browser apa pun (Google Chrome, Edge, Firefox, Safari). Tidak perlu instalasi server atau NodeJS.

### 2. Publikasi ke GitHub Pages (Gratis & Tahan 10+ Tahun)
1. Buat repositori baru di GitHub (misal: `yb-terminal`).
2. Unggah file-file berikut ke branch `main`:
   - `index.html`
   - `clue_labkom.jpg`
   - `clue_kantin.jpg`
   - `clue_rooftop.jpg`
3. Masuk ke **Settings** > **Pages** di repositori GitHub Anda.
4. Pada **Branch**, pilih `main` dan folder `/ (root)`, lalu klik **Save**.
5. Situs Anda akan aktif di URL seperti:
   `https://username.github.io/yb-terminal/`

---

## 🛠️ Panel Admin Visual (Tanpa Perlu Koding!)

Aplikasi ini sudah dilengkapi dengan **Panel Admin Interaktif** langsung di halaman web. Anda tidak perlu mengedit baris kode secara manual!

### Cara Mengakses Panel Admin:
1. Buka `index.html` di browser Anda.
2. Klik tombol **`[ 🛠 PANEL ADMIN ]`** di bar navigasi kanan atas (atau ketik kata `ADMIN` di form input Tahap 1 lalu tekan Enter).
3. Masukkan PIN Admin: **`ADMIN123`** *(PIN ini juga bisa diganti di dalam panel)*.

### Fitur yang Bisa Diatur di Panel Admin:
* **🔐 Kata Sandi Tahap 1:** Ubah kata sandi tebakan Instagram dan petunjuk teksnya.
* **🖼️ Gambar Clue Tahap 2:**
  - Ketik nama file lokal (misal `clue_labkom.jpg`) atau link gambar.
  - Atau klik tombol **`[ 📁 PILIH FOTO DARI KOMPUTER ]`** untuk memilih gambar langsung dari laptop/HP Anda (gambar otomatis dipratinjau dan disimpan).
* **🎬 Target Video YouTube Tahap 3:**
  - Masukkan 11 digit ID video YouTube (misal `dQw4w9WgXcQ`), ATAU langsung paste link YouTube lengkap (misal `https://youtu.be/dQw4w9WgXcQ`). Sistem akan otomatis memfilter ID-nya!
  - Ada tombol **`[ ▶ TEST ]`** untuk memastikan video YouTube bisa diputar.
* **➕ Tambah / Hapus Sektor:** Anda bisa menambah sektor ke-4, ke-5, atau menghapus sektor yang tidak terpakai secara bebas.
* **📥 Download File `index.html` Baru:**
  - Setelah selesai mengatur di Panel Admin, cukup klik **`[ 📥 DOWNLOAD FILE INDEX.HTML BARU ]`**.
  - File `index.html` baru yang diunduh sudah otomatis tertanam seluruh konfigurasi Anda.
  - Tinggal ganti file `index.html` di komputer Anda, lalu unggah ke GitHub Pages! Sangat mudah dan praktis.
* **💾 Simpan di Browser Ini:** Menyimpan konfigurasi ke `localStorage` untuk langsung menguji teka-teki di browser saat ini.

---

## 🖨️ Panduan Cetak Buku Tahunan: Enkripsi URL Base64

Agar pengalaman ARG terasa misterius, cetak string **Base64** di halaman buku tahunan Anda:

### Contoh:
Jika URL website Anda adalah:
`https://angkatan2026.github.io/yb-terminal/`

String Base64-nya adalah:
`aHR0cHM6Ly9hbmdrYXRhbjIwMjYuZ2l0aHViLmlvL3liLXRlcm1pbmFsLw==`

### Cara Generate String Base64:
1. Buka `index.html` di browser Anda.
2. Klik tombol **`[ ⚙ BASE64 TOOLKIT ]`** di pojok kanan atas terminal.
3. Masukkan link website Anda dan klik tombol **ENCODE KE BASE64**.
4. Salin string hasilnya untuk dicetak di buku tahunan dengan instruksi:
   > *"Dekode string berikut di base64decode.org untuk mengakses arsip rahasia kelas kita."*

---

## 🖼️ Mengubah Gambar Clue (Blur OpenCV)

File gambar yang disertakan di repositori ini:
* `clue_labkom.jpg` (Artefak #01)
* `clue_kantin.jpg` (Artefak #02)
* `clue_rooftop.jpg` (Artefak #03)

Jika Anda ingin membuat gambar blur sendiri dari foto sekolah asli menggunakan OpenCV:
1. Pasang dependensi Python:
   ```bash
   pip install opencv-python numpy
   ```
2. Jalankan skrip bantu:
   ```bash
   python blur_tool.py foto_asli.jpg clue_labkom.jpg 55
   ```
   *(Angka 55 adalah tingkat keburaman Gaussian blur)*.

---

## ⚙️ Fitur Unggulan

- **Retro CRT Aesthetic:** Dilengkapi scanlines murni CSS, phosphor glow, dan typography monospace.
- **Audio Synthesizer Mandiri:** Menggunakan *HTML5 Web Audio API* untuk menghasilkan efek suara tombol ketik, sukses arpeggio, dan alert denied secara sintetis tanpa memerlukan file `.mp3` atau `.wav` eksternal.
- **Mobile Responsive:** Layout fleksibel yang nyaman dibuka di smartphone maupun laptop.
- **Satu File Portabel:** Dapat didistribusikan hanya dalam satu file `index.html`.
