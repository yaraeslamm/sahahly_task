from langchain_community.llms import Ollama
from llm_config import llm

def grade_question(student_answer, mark_scheme):
    prompt = f"""
You are an AI grading assistant.

Grade the student's answer based ONLY on the provided mark scheme.

Marking Rules:
- Each matching point = 1 mark
- Do not award marks for unrelated content
- Be strict but fair

Return ONLY valid JSON in this exact format:
{{
  "score": int,
  "max_score": int,
  "feedback": "string",
  "missing_points": ["string"]
}}

Mark Scheme:
{mark_scheme}

Student Answer:
{student_answer}
"""

    response = llm.invoke(prompt)

    if hasattr(response, "content"):
        return response.content

    return response