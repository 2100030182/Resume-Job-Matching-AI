import pdfplumber


def extract_text_from_pdf(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    return text


if __name__ == "__main__":
    pdf_path = "data/sample_resume.pdf"

    resume_text = extract_text_from_pdf(pdf_path)

    print("\n===== RESUME TEXT =====\n")
    with open("data/resume_text.txt", "w", encoding="utf-8") as f:
        f.write(resume_text)

    print("Resume text saved to resume_text.txt")