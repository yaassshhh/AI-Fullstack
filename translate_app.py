import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

st.set_page_config(page_title="English to French Translator", page_icon="🌐", layout="centered")
st.title("English to French Translator")
st.caption("Type English text and translate it into natural French.")

english_text = st.text_area(
    "English text",
    placeholder="Write something in English here...",
    height=180,
)

if st.button("Translate"):
    if not english_text.strip():
        st.warning("Please enter some English text to translate.")
    else:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            st.error("GOOGLE_API_KEY is not set. Please add it to your environment before running the app.")
        else:
            try:
                llm = ChatGoogleGenerativeAI(
                    model="gemini-2.5-flash-lite",
                    google_api_key=api_key,
                )
                messages = [
                    SystemMessage(
                        content="You are a professional translator. Translate the user's English text into natural French. Return only the translated text."
                    ),
                    HumanMessage(content=english_text),
                ]
                response = llm.invoke(messages)
                st.subheader("French translation")
                st.write(response.content)
            except Exception as exc:
                st.error(f"Translation failed: {exc}")
