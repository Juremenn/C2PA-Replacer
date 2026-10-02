# C2PA-Replacer (Image Metadata Cleaner)

A simple, effective Python tool to completely strip all hidden metadata (EXIF, IPTC, C2PA, XMP) from your images. By reading only the raw pixel data and discarding the rest, this script ensures your privacy is protected before sharing images online.

## Features
- **Total Metadata Removal:** Cleans all traces of EXIF, C2PA, IPTC, and XMP data.
- **Smart Saving:** Automatically optimizes JPEG and PNG outputs to maintain visual quality (JPEG saved at 95% quality).
- **Safe Processing:** Creates a new `_clean` file instead of overwriting your original image.
- **Before/After Metrics:** Displays the exact file size reduction after the metadata is stripped.

## Prerequisites

You need Python installed on your system along with the **Pillow** (PIL) library to handle image processing.

Install the required library using pip:
```bash
pip install Pillow

🚀 How to Use
Place the Python script in your desired folder.

Open your terminal or command prompt.

Run the script by passing the path of the image you want to clean as an argument:

python main.py path/to/your/image.jpg

Example Output
----------------------------------------
SUKSES Metadata berhasil diubah
Input  : profile_pic.jpg (150.50 KB)
Output : profile_pic_clean.jpg (142.20 KB)
----------------------------------------
