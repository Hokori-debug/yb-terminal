"""
=============================================================================
YB QUEST TERMINAL - OPENCV BLUR TOOL
=============================================================================
Skrip bantu untuk menghasilkan gambar terdistorsi / blur bergaya ARG
untuk teka-teki Tahap 2 buku tahunan.

Kebutuhan:
pip install opencv-python numpy

Cara Penggunaan:
1. Siapkan foto asli (misal: labkom_asli.jpg, kantin_asli.jpg, rooftop_asli.jpg)
2. Jalankan: python blur_tool.py labkom_asli.jpg clue_labkom.jpg
=============================================================================
"""

import sys
import os

try:
    import cv2
    import numpy as np
except ImportError:
    print("[ERROR] OpenCV / NumPy belum terpasang.")
    print("Silakan pasang dengan menjalankan: pip install opencv-python numpy")
    sys.exit(1)


def generate_arg_blur(input_path, output_path, blur_strength=55, add_noise=True):
    """
    Menerapkan Gaussian Blur intensif dan efek noise retro pada foto.
    """
    if not os.path.exists(input_path):
        print(f"[ERROR] File input tidak ditemukan: {input_path}")
        return False

    # Baca gambar
    img = cv2.imread(input_path)
    if img is None:
        print(f"[ERROR] Gagal membaca gambar: {input_path}")
        return False

    # Resize gambar agar optimal untuk web (lebar 800px, aspect ratio dijaga)
    h, w = img.shape[:2]
    max_w = 800
    if w > max_w:
        ratio = max_w / float(w)
        new_dim = (max_w, int(h * ratio))
        img = cv2.resize(img, new_dim, interpolation=cv2.INTER_AREA)

    # Pastikan kernel size ganjil
    ksize = blur_strength if blur_strength % 2 == 1 else blur_strength + 1
    
    # 1. Terapkan Gaussian Blur
    blurred = cv2.GaussianBlur(img, (ksize, ksize), 0)

    # 2. Opsional: Tambahkan grain/noise retro
    if add_noise:
        row, col, ch = blurred.shape
        mean = 0
        sigma = 12
        gauss = np.random.normal(mean, sigma, (row, col, ch)).astype('uint8')
        blurred = cv2.addWeighted(blurred, 0.9, gauss, 0.1, 0)

    # Simpan hasil render
    cv2.imwrite(output_path, blurred, [cv2.IMWRITE_JPEG_QUALITY, 85])
    print(f"[SUKSES] Gambar blur berhasil disimpan ke: {output_path}")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Penggunaan:")
        print("  python blur_tool.py <foto_input.jpg> <foto_output.jpg> [blur_level]")
        print("Contoh:")
        print("  python blur_tool.py foto_asli.jpg clue_labkom.jpg 55")
    else:
        in_file = sys.argv[1]
        out_file = sys.argv[2]
        strength = int(sys.argv[3]) if len(sys.argv) > 3 else 55
        generate_arg_blur(in_file, out_file, blur_strength=strength)
