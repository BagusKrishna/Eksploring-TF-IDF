# MultiModal Process Exploration

1. NLP with TF-IDF and GloVe Expansion
2. Image Extraction with MobileNetV1
3. Classification Model CNN-BiGRU

Including : 
- Corpus Crawler (News Site)

---

## Prerequisites

* Python 3.8+
* Git

---

## Setup Instructions

Ikuti langkah-langkah berikut untuk menyiapkan lingkungan kerja.

### 1. Clone the Repository

Buka terminal Anda, lalu clone dan masuk ke direktori proyek.
```bash
git clone https://github.com/BagusKrishna/Extracting-Feature-Multimodal.git
cd Extracting-Feature-Multimodal
```

### 2a. Setup environment (for Windows)
```bash
# Create environtment
python -m venv venv
```
```bash
# Activate environment
.\venv\Scripts\activate
```

### 2b. Setup environment (for Ubuntu)
```bash
# Create environtment
python3 -m venv venv
```
```bash
# Activate environment
source venv/bin/activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Adjust File Paths (Crucial Step)
Path file dalam notebook perlu disesuaikan dengan struktur direktori di mesin Anda.

1. Buka dan edit file path_generator.py.

2. Ubah nilai variabel old_base_path dan new_base_path agar sesuai.

3. Jalankan skrip dari terminal:

```bash
python3 path_generator.py
```
