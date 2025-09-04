Inconsistency Detector 🔍  
**Tech Stack:** Python • python-pptx • Pillow • Tesseract OCR (pytesseract) • Google GenAI SDK (Gemini 2.5 Flash LLM)

📌 Overview
The **Inconsistency Detector** is an AI-powered tool that analyzes PowerPoint (`.pptx`) decks for **cross-slide inconsistencies** in metrics, timelines, and terminology.  
It extracts both **native text** and **embedded image text (via OCR)**, then leverages **Gemini 2.5 Flash LLM** to generate a structured, slide-wise inconsistency report.

---

🚀 Features
- Extracts text from PPTX slides using **python-pptx**.  
- Saves and processes embedded images with **Pillow**.  
- Runs **Tesseract OCR** to capture text from images (charts, screenshots, tables).  
- Integrates with **Gemini 2.5 Flash LLM** to identify inconsistencies across slides.  
- Outputs a **clean, slide-referenced report** highlighting contradictions.  
- Robust handling for missing images or OCR errors.  

---

📂 Project Structure
inconsistency-detector/
│── data/
│ ├── sample_deck.pptx # Example input file
│ └── images/ # Extracted images from slides
│── src/
│ ├── main.py # Entry point / orchestrator
│ ├── extract.py # PPTX text & image extraction
│ ├── ocr.py # OCR wrapper for images
│ ├── analyze.py # Builds prompt & analyzes with LLM
│ └── llm_client.py # Google GenAI client wrapper
│── requirements.txt
│── README.md

yaml
Copy code
