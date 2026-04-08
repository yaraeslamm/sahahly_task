from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from grading import grade_question
from pdf_extractor import extract_text_from_pdf, extract_student_answer
from fastapi.responses import JSONResponse
import json

app = FastAPI(title="AI Grading API")
class GradeResponse(BaseModel):
    score: int
    max_score: int
    feedback: str
    missing_points: list[str]

# Hardcoded mark scheme example
MARK_SCHEME = {
    "max_score": 5,
    "points": [
        "Uses sunlight as energy",
        "Occurs in chloroplasts",
        "Uses carbon dioxide and water",
        "Produces glucose",
        "Releases oxygen"
    ]
}

#check if API is running
@app.get("/")
def root():
    return {"message": "AI Grading API is running"}

# Main grading endpoint
@app.post("/grade/pdf")
async def grade_pdf(file: UploadFile = File(...)):
    try:
        # Read PDF bytes
        pdf_bytes = await file.read()

        # Extract text
        full_text = extract_text_from_pdf(pdf_bytes)
        student_answer = extract_student_answer(full_text)

        # Grade
        result = grade_question(student_answer, MARK_SCHEME)

        # Return JSON response
        return JSONResponse(content=json.loads(result))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))