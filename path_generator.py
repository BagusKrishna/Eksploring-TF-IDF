import json
from pathlib import Path

# CARA RUN : python3 path_generator.py
# ================== JANGAN ASAL RUN CHECK DULU PATH NYA BIAR GA ERROR ==================

# 1. Definisikan path dasar LAMA. Kita buat dua versi (backslash dan forward slash).
old_base_path_windows_bs = r'E:\$7th\TA\Multimodal_Process_Exploration'
old_base_path_windows_fs = r'E:/$7th/TA/Multimodal_Process_Exploration' 

# 2. Definisikan path dasar BARU di Ubuntu.
new_base_path_ubuntu = r'/home/spil/1Bagus/BACKUP/TA/Multimodal_Process_Exploration'

# ===================================================================

# -- Logika Skrip (Tidak perlu diubah) --
project_folder = Path('.')

print("="*50)
print("Memulai Skrip Konversi Path Notebook (Versi Final)")
print(f"Mencari path Windows (kedua format / dan \\)...")
print(f"--> Akan diubah menjadi: '{new_base_path_ubuntu}'")
print("="*50)

notebook_files = list(project_folder.rglob('*.ipynb'))

if not notebook_files:
    print("\nTidak ada file .ipynb yang ditemukan.")
else:
    print(f"\nDitemukan {len(notebook_files)} file notebook. Memproses...")

for notebook_file in notebook_files:
    print(f"\n--> Memproses file: {notebook_file}")
    
    try:
        with open(notebook_file, 'r', encoding='utf-8') as f:
            notebook_data = json.load(f)

        content_str = json.dumps(notebook_data)
        original_content = content_str
        
        # --- PERUBAHAN UTAMA DI SINI ---
        # 1. Ganti path Windows yang pakai backslash (\)
        modified_content = original_content.replace(old_base_path_windows_bs, new_base_path_ubuntu)
        
        # 2. Ganti path Windows yang pakai forward slash (/)
        modified_content = modified_content.replace(old_base_path_windows_fs, new_base_path_ubuntu)
        
        # 3. Bersihkan sisa backslash lain yang mungkin ada (untuk path relatif)
        modified_content = modified_content.replace('\\\\', '/')
        # --------------------------------

        if original_content != modified_content:
            new_notebook_data = json.loads(modified_content)
            
            with open(notebook_file, 'w', encoding='utf-8') as f:
                json.dump(new_notebook_data, f, indent=2)
            
            print(f"    [OK] Path berhasil dikonversi dan file disimpan.")
        else:
            print(f"    [INFO] Tidak ada path yang cocok untuk diubah.")

    except json.JSONDecodeError:
        print(f"    [ERROR] File ini tampaknya rusak (bukan JSON valid). Dilewati.")
    except Exception as e:
        print(f"    [ERROR] Gagal memproses file. Kesalahan: {e}")

print("\n" + "="*50)
print("Skrip Selesai.")
print("="*50)