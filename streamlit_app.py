import streamlit as st
from groq import Groq

st.set_page_config(page_title="AI Study Buddy", page_icon="📚")

st.title("📚 AI Study Buddy")
st.caption("Your AI-powered study assistant")

# Get API key from Streamlit secrets
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
    st.error("GROQ_API_KEY not found. Please add it in Streamlit Cloud's Secrets settings.")
    st.stop()

mode = st.selectbox("Choose a mode", ["Explain", "Summarize", "Quiz"])

if mode == "Explain":
    user_input = st.text_area("What topic or question do you want explained?", height=150)
    prompt_template = "Explain the following topic clearly and simply, as if teaching a student:\n\n{input}"

elif mode == "Summarize":
    user_input = st.text_area("Paste the text you want summarized:", height=200)
    prompt_template = "Summarize the following text into clear, concise key points:\n\n{input}"

else:  # Quiz
    user_input = st.text_area("Paste notes or a topic to generate quiz questions from:", height=200)
    prompt_template = (
        "Based on the following content, generate 5 quiz questions with answers, "
        "covering key concepts:\n\n{input}"
    )

if st.button("✨ Generate"):
    if not user_input.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "user", "content": prompt_template.format(input=user_input)}
                    ],
                )
                result = response.choices[0].message.content
                st.markdown("### Result")
                st.write(result)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
