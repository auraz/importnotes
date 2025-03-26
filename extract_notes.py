import os, subprocess
from image_utils import pdf_to_images, refine_image, save_images_and_pdf

def perform_ocr(pdf_path):
    script = 'ocr_preview_pdf.scpt'
    result = subprocess.run(['osascript', script, os.path.abspath(pdf_path)], capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else ''

def process_pdf(pdf_path, images_dir='refined_images', notes_dir='output_notes'):
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    images = [refine_image(img) for img in pdf_to_images(pdf_path)]
    pdf_filename = f'{base_name}_refined.pdf'
    save_images_and_pdf(images, images_dir, pdf_filename)

    extracted_text = perform_ocr(os.path.join(images_dir, pdf_filename))

    os.makedirs(notes_dir, exist_ok=True)
    with open(os.path.join(notes_dir, f'{base_name}.md'), 'w') as f:
        f.write(f"# Notes from {base_name}\n\n{extracted_text}")

def process_all_pdfs(input_dir='input_notes', images_dir='refined_images', notes_dir='output_notes'):
    """Process all PDFs from input_notes folder into markdown notes."""
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(input_dir, filename)
            process_pdf(pdf_path, images_dir, notes_dir)

if __name__ == "__main__":
    process_all_pdfs()
