# AI Grading Tool (MVP)

## Overview

This project is a simple AI-powered grading system that processes a student’s answer from a PDF file and evaluates it based on a predefined mark scheme.

The system extracts text from the PDF, identifies the student’s answer, and uses an LLM to assign a score, feedback, and missing points in a structured JSON format.

---

## Features

* Extract text from PDF files
* Identify and process student answers
* AI-based grading using a predefined mark scheme
* Structured JSON output (score, feedback, missing points)
* FastAPI endpoint for easy testing and integration

---

## Tech Stack

* Python
* FastAPI
* pdfplumber (PDF text extraction)
* LangChain + Groq (LLM inference)
* Model: llama-3.1-8b-instant (via Groq API)

---

## Project Structure

```
├── app.py              # FastAPI application
├── grading.py         # AI grading logic
├── llm_config.py      # LLM configuration
├── pdf_extractor.py   # PDF text extraction
├── README.md
```

---

## Setup Instructions

1. Clone the repository:

```
git clone https://github.com/yaraeslamm/sahahly_task.git


cd sahahly_task
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Set environment variable:

```
GROQ_API_KEY=your_api_key_here
```

4. Run the server:

```
uvicorn app:app --reload
```

---

## API Usage

### Endpoint
POST /grade/pdf

### Input
- Upload a PDF file using the `file` field (multipart/form-data)

---

### Testing

#### Option 1 — Postman
- Set method to `POST`
- URL: `http://127.0.0.1:8000/grade/pdf`
- Go to **Body → form-data**
- Add key: `file` (type: File)
- Upload a PDF from the `examples` folder
- Send request

---

#### Option 2 — cURL

```bash
curl -X POST "http://127.0.0.1:8000/grade/pdf" \
  -F "file=@examples/student_answer.pdf"


---

## Example Inputs & Outputs

### Example 1 — Incorrect Answer
[View PDF](./examples/student_answer2.pdf)

Output:
```json
{
    "score": 5,
    "max_score": 5,
    "feedback": "All points matched",
    "missing_points": []
}
```
### Example 2 — Incorrect Answer
[View PDF](./examples/student_answer.pdf)

Output:
```json
{
    "score": 0,
    "max_score": 5,
    "feedback": "The student's answer does not match any of the points in the mark scheme.",
    "missing_points": [
        "Uses sunlight as energy",
        "Occurs in chloroplasts",
        "Uses carbon dioxide and water",
        "Produces glucose",
        "Releases oxygen"
    ]
}
```

### Example 3 — Mixed Answer
[View PDF](./examples/student_answer3.pdf)

Output:
```json
{
    "score": 4,
    "max_score": 5,
    "feedback": "Most points are covered, but 'Occurs in chloroplasts' is not explicitly stated.",
    "missing_points": [
        "Occurs in chloroplasts"
    ]
}
```

---

## Notes

* The mark scheme is currently hardcoded for simplicity.
* The system currently extracts the student answer by locating the "Student Answer:" section in the PDF (simplified assumption for MVP).

---
