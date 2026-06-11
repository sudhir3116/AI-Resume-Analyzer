from pypdf import PdfReader
from dotenv import load_dotenv
import google.generativeai as genai
import os
pdf_path=input("Upload the PDF...")
reader=PdfReader(pdf_path)
test=""
for page in reader.pages:
    extracted=page.extract_text()
    if extracted:
        test+=extracted
print("Resume text extracted successfully.")

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")
prompt = f"""
Analyze this resume.

Give:
1. Strengths
2. Weaknesses
3. Missing Skills
4. Suggestions for Improvement

Resume:

{test}
"""
try:
    response = model.generate_content(prompt)
    print(response.text)

except Exception as e:
    print(f"Error: {e}")