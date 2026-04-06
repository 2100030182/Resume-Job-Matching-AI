from skill_extractor import extract_skills


def load_job_description(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":

    job_file = "data/job_description.txt"

    job_text = load_job_description(job_file)

    job_skills = extract_skills(job_text)

    print("\n===== JOB SKILLS =====\n")

    for skill in job_skills:
        print(skill)

    # Save extracted skills
    with open("data/job_skills.txt", "w") as f:
        for skill in job_skills:
            f.write(skill + "\n")

    print("\nJob skills saved to job_skills.txt")