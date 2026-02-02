# LLM 🧠

**Repositori ini berisi kumpulan proyek pembelajaran mesin dan eksperimen LLM/RNN/LSTM/ANN serta beberapa notebook untuk data ingestion dan percobaan.**

---

## 📚 Ringkasan
Repositori "LLM" adalah kumpulan proyek dan notebook eksperimen terkait deep learning (RNN, LSTM, ANN) dan beberapa contoh penggunaan LangChain. Folder-folder di repo ini berisi model terlatih, data contoh, dan notebook yang dapat dijalankan untuk reproduksi eksperimen.

---

## 📁 Struktur Repository (ringkas)
- `Analisis-Sentimen-Tokopedia/` — Notebook preprocessing, scraping, dan dataset Tokopedia (CSV) untuk analisis sentimen.
- `ANN-RNN/` — Model ANN/RNN, notebook `test.ipynb`, file `ann_model.h5`, dataset `Churn_Modelling.csv`.
- `Langchain/` — Contoh notebook LangChain, data ingestion, dan pengaturan lingkungan untuk eksperimen LLM.
- `LSTM-Project/` — Model LSTM untuk tugas prediksi teks (`hamlet_*_model.h5`), `app.py` sebagai contoh aplikasi.
- `SImple-RNN-Project/` — Contoh proyek RNN (notebook dan `main.py`, model `.h5`).
- `Teori/` — (Opsional) materi dan catatan teoretis.

> Perhatikan: Beberapa folder memiliki `requirments.txt` / `requirements.txt` — pastikan menginstall dependensi di dalam folder yang relevan.

---

## 🚀 Quick start
Jika Anda ingin meng-clone repo:

```bash
git clone https://github.com/Npppss/LLM.git
```

---

## ⚙️ Lingkungan & Instalasi
Disarankan menggunakan virtual environment (`venv`/`conda`) untuk setiap sub-proyek.

Contoh singkat (virtualenv + pip):

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# atau cmd
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Jika setiap subfolder memiliki `requirements.txt`, jalankan `pip install -r path/to/requirements.txt` di folder tersebut.

---

## ▶️ Menjalankan Notebook & Skrip
- Notebook: buka dengan Jupyter / JupyterLab / VS Code (ekstensi Jupyter).
- `LSTM-Project/app.py` — contoh aplikasi; jalankan dengan `python app.py`.
- `SImple-RNN-Project/main.py` — script utama untuk demo model RNN.
- Beberapa model (`*.h5`) sudah tersedia untuk inference (`ann_model.h5`, `sentiment_lstm_model.h5`, `hamlet_*_model.h5`).

Catatan: Pastikan dependensi terinstall dan kernel notebook sesuai versi Python yang direkomendasikan (3.8+ / 3.10/3.11 tergantung environment).

---

## 🤝 Kontribusi
- Silakan buka issue untuk bug atau fitur.
- Buat branch baru untuk perubahan: `git checkout -b feat/your-feature`.
- Tambahkan unit tests atau notebook demo ketika relevan.

---

## 📄 Lisensi
Tambahkan file `LICENSE` (misalnya MIT) jika Anda ingin menjaga repositori ini open-source.

Contoh singkat (MIT):
```
MIT License
Copyright (c) 2026 Novandra Aria Budi Raspati
```

---

## 💬 Kontak
Untuk pertanyaan lebih lanjut, tambahkan issue atau hubungi pemilik repo.

---

Terima kasih! ✅
