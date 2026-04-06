import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Predefined skill list (can expand later)
SKILLS_DB = [
    "python",
    "java",
    "c++",
    "sql",
    "javascript",
    "machine learning",
    "deep learning",
    "tensorflow",
    "scikit-learn",
    "docker",
    "aws",
    "flask",
    "tableau",
    "mongodb",
    "mysql",
    "postgresql",
    "rest api",
    "data structures",
    "algorithms"
]


def extract_skills(text):
    doc = nlp(text.lower())

    found_skills = set()

    for skill in SKILLS_DB:
        if skill in text.lower():
            found_skills.add(skill)

    return list(found_skills)


if __name__ == "__main__":

    # Load resume text
    with open("data/resume_text.txt", "r", encoding="utf-8") as f:
        resume_text = f.read()

    skills = extract_skills(resume_text)

    print("\n===== EXTRACTED SKILLS =====\n")

    for skill in skills:
        print(skill)

    # Save skills
    with open("data/extracted_skills.txt", "w") as f:
        for skill in skills:
            f.write(skill + "\n")

    print("\nSkills saved to extracted_skills.txt")