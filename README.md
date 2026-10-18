# E-CV Faisal Yusuf — Streamlit

Website E-CV untuk tugas individu mata kuliah Digital Kreatif. Desain biru profesional dan responsif, dengan bagian profil, pendidikan, keahlian teknis/nonteknis, pengalaman PKL, proyek, pelatihan/sertifikasi, kontak, dan unduhan PDF.

## File proyek
- `app.py` — aplikasi Streamlit dan pembuat CV PDF.
- `requirements.txt` — dependensi Python.
- `CV_Faisal_Yusuf.pdf` — contoh PDF CV yang bisa ditinjau; tombol di website juga membuat PDF terbaru.

## Menjalankan di laptop
1. Install Python 3.10 atau lebih baru.
2. Ekstrak ZIP proyek.
3. Buka CMD/terminal di folder proyek.
4. Jalankan:
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```
5. Browser akan membuka aplikasi lokal, biasanya di `http://localhost:8501`.

## Menambahkan foto
Di website, buka panel kiri (sidebar) lalu unggah foto JPG atau PNG. Foto yang diunggah tampil untuk sesi tersebut. Untuk foto yang selalu tampil setelah deployment, edit kode agar memakai gambar yang disimpan bersama proyek di repository, atau unggah foto ke repository publik yang memang ingin dibagikan. Jangan mengunggah foto sensitif.

## Memperbarui data CV
Edit bagian `PROFILE` di awal `app.py`. Ganti placeholder dalam tanda kurung siku dengan informasi yang benar. Bagian sertifikat saat ini berupa placeholder karena nama sertifikat, penyelenggara, dan tahun belum diberikan. Jangan menampilkan detail yang belum terverifikasi.

## Publikasi online via Streamlit Community Cloud
1. Buat akun GitHub di https://github.com/.
2. Buat repository baru, misalnya `ecv-faisal-yusuf`.
3. Unggah `app.py` dan `requirements.txt` (opsional sertakan README).
4. Buka https://share.streamlit.io/ dan masuk menggunakan akun GitHub.
5. Pilih **Create app**, pilih repository dan branch, lalu isi file utama dengan `app.py`.
6. Klik **Deploy** dan tunggu sampai selesai.
7. Salin URL publik yang diberikan.
8. Uji URL di jendela privat atau browser HP untuk memastikan dosen dapat mengaksesnya tanpa izin tambahan.
9. Kumpulkan URL publik melalui MyBest.

## Sebelum mengumpulkan
- Lengkapi periode PKL, tahun pendidikan, dan rincian sertifikat.
- Tambahkan foto jika diinginkan.
- Periksa nama, email, ejaan, dan semua informasi.
- Jangan mencantumkan NIK, nomor KK, alamat rumah lengkap, atau data sensitif lainnya.

Catatan: file proyek sudah dibuat, tetapi link publik baru tersedia setelah kamu melakukan deployment di Streamlit Community Cloud.
