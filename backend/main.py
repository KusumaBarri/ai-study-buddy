from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

class StudyRequest(BaseModel):
    text: str
    mode: str

PROMPTS = {
    "explain":    lambda t: f"Explain this concept simply for a student with a real-world analogy (under 200 words):\n{t}",
    "summarize":  lambda t: f"Summarize these notes into clear bullet points:\n{t}",
    "quiz":       lambda t: f"Generate 4 MCQ questions as JSON only, no extra text:\n[{{\"q\":\"...\",\"options\":[\"A\",\"B\",\"C\",\"D\"],\"answer\":\"A\"}}]\nTopic: {t}",
    "flashcards": lambda t: f"Create 5 flashcards as JSON only, no extra text:\n[{{\"term\":\"...\",\"definition\":\"...\"}}]\nContent: {t}"
}

@app.post("/study")
def study(req: StudyRequest):
    prompt = PROMPTS[req.mode](req.text)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=0.7
    )
    return {"result": response.choices[0].message.content}

@app.get("/")
def root():
    return {"message": "Study Buddy API is running!"}