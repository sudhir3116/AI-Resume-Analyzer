import streamlit as st
from pypdf import PdfReader
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load Environment Variables
load_dotenv()

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

# UI
st.title("AI Resume Analyzer")
st.divider()

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    # Extract Text from PDF
    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted

    st.success("Resume Uploaded Successfully")
    st.success("Text Extracted Successfully")

    # Analyze Button
    if st.button("Analyze Resume"):

        prompt = f"""
        You are an ATS Resume Reviewer.

        Analyze the resume and provide:

        1. Resume Score out of 100
        2. Strengths
        3. Weaknesses
        4. Missing Skills
        5. Suggestions for Improvement

        Resume:

        {text}
        """

        try:

            with st.spinner("Analyzing Resume..."):

                response = model.generate_content(prompt)

            st.subheader("Resume Analysis")

            st.write(response.text)

        except Exception as e:

            st.error(f"Error: {e}")