from pypdf import PdfReader
pdf_path=input("Upload the PDF...")
reader=PdfReader(pdf_path)
test=""
for page in reader.pages:
    extracted=page.extract_text()
    if extracted:
        test+=extracted
print(test)