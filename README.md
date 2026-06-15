# 📚 AI Study Buddy

An AI-powered study tool that helps students understand complex concepts, summarize notes, generate quizzes, and create flashcards instantly — powered by **Groq API** and **LLaMA 3.3**.

---

## 🚀 Features

- 💡 **Explain** — Simplifies any topic in easy language with real-world analogies
- 📄 **Summarize** — Converts long notes into clear bullet points
- ❓ **Quiz Me** — Generates multiple choice questions with auto-scoring
- 🃏 **Flashcards** — Creates flip cards for quick revision

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | React.js, Axios |
| Backend | FastAPI (Python) |
| AI Model | LLaMA 3.3 70B via Groq API |
| Styling | CSS-in-JS |

---

## 📁 Project Structure

```
study-buddy/
├── backend/
│   ├── main.py          ← FastAPI server
│   ├── .env             ← API keys (never upload this!)
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.js       ← Main React component
│   │   └── api.js       ← Axios API calls
│   └── package.json
└── README.md
```

---

## ⚙️ How to Run Locally

### Step 1 — Clone the repository
```bash
git clone https://github.com/YOURNAME/ai-study-buddy.git
cd ai-study-buddy
```

### Step 2 — Setup Backend
```bash
cd backend
pip install -r requirements.txt
```

Create a `.env` file inside the backend folder:
```
GROQ_API_KEY=your_groq_api_key_here
```

Run the backend:
```bash
python -m uvicorn main:app --reload
```

### Step 3 — Setup Frontend
Open a new terminal:
```bash
cd frontend
npm install
npm start
```

### Step 4 — Open the app
Go to **http://localhost:3000** in your browser 🎉

---

## 🔑 Getting a Groq API Key (Free)

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Click **API Keys** → **Create API Key**
4. Copy and paste it into your `.env` file

---

## 📸 Screenshots

> Add your screenshots here after taking them!

---

## 👨‍💻 Author

Made with ❤️ by **Your Name**  
GitHub: [github.com/yourname](https://github.com/yourname)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).