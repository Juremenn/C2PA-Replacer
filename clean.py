import os
import sys
from PIL import Image

def clean_image_metadata(input_path: str, output_path: str = None):
    """
    Membersihkan seluruh metadata (EXIF, IPTC, C2PA, XMP) dari gambar
    """
    if not os.path.exists(input_path):
        print(f"ERROR File '{input_path}' tidak ditemukan.")
        return

    if output_path is None:
        name, ext = os.path.splitext(input_path)
        output_path = f"{name}_clean{ext}"

    try:
        with Image.open(input_path) as img:
            mode = img.mode
            size = img.size
            data = list(img.getdata())

            clean_img = Image.new(mode, size)
            clean_img.putdata(data)

            if img.format == 'JPEG' or ext.lower() in ['.jpg', '.jpeg']:
                clean_img.save(output_path, "JPEG", quality=95, optimize=True)
            elif img.format == 'PNG' or ext.lower() == '.png':
                clean_img.save(output_path, "PNG", optimize=True)
            else:
                clean_img.save(output_path)

        original_size = os.path.getsize(input_path) / 1024
        cleaned_size = os.path.getsize(output_path) / 1024

        print("-" * 40)
        print(f"SUKSES Metadata berhasil diubah")
        print(f"Input  : {input_path} ({original_size:.2f} KB)")
        print(f"Output : {output_path} ({cleaned_size:.2f} KB)")
        print("-" * 40)

    except Exception as e:
        print(f"ERROR Terjadi kesalahan: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
    else:
        target_file = "sample.jpg"

    clean_image_metadata(target_file)
