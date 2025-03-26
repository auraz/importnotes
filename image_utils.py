from pdf2image import convert_from_path
from PIL import Image, ImageEnhance, ImageFilter
import os

def pdf_to_images(pdf_path, dpi=500):
    """Convert PDF pages into images for processing."""
    return convert_from_path(pdf_path, dpi=dpi)

def refine_image(img, contrast=1.3, threshold=190, filter_size=1):
    """Enhance image clarity to improve OCR accuracy."""
    img = img.convert('L')
    img = ImageEnhance.Contrast(img).enhance(contrast)
    img = img.point(lambda p: 255 if p > threshold else 0)
    return img.filter(ImageFilter.MedianFilter(filter_size))

def save_images(images, output_dir='refined_images'):
    """Saves a list of PIL Image objects to JPG files."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for idx, img in enumerate(images, start=1):
        img.save(os.path.join(output_dir, f'refined_page_{idx}.jpg'), 'JPEG')

def save_images_and_pdf(images, images_dir, pdf_filename):
    """Save refined images individually and combined as PDF."""
    os.makedirs(images_dir, exist_ok=True)
    paths = [os.path.join(images_dir, f'refined_page_{i+1}.jpg') for i in range(len(images))]
    for img, path in zip(images, paths):
        img.save(path, 'JPEG')
    images[0].save(os.path.join(images_dir, pdf_filename), save_all=True, append_images=images[1:])

if __name__ == "__main__":
    # Standalone execution: Convert and refine PDF, then save images
    pdf_path = './input_notes/Scanned Document.pdf'  # Change this to your PDF file path
    images = pdf_to_images(pdf_path, dpi=500)
    refined_images = [refine_image(img) for img in images]
    save_images(refined_images)
    print("Refined images saved successfully in 'refined_images' directory.")
