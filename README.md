# PDF Handwritten Notes to Markdown

Convert handwritten PDF notes into markdown using Apple's Preview OCR.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
brew install poppler
```

Ensure your IDE/terminal has Automation permissions for Preview (`System Preferences → Security & Privacy → Privacy → Automation`).

## Usage

1. Put PDFs into `input_notes/`.
2. Run:

```bash
python extract_notes.py
```

3. Markdown notes appear in `output_notes/`.

Refined images and PDFs are saved in `refined_images/`.
