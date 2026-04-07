def load_skills(file_path):
    with open(file_path, "r") as f:
        skills = [line.strip() for line in f.readlines()]
    return skills


def calculate_match(resume_skills, job_skills):

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched_skills = resume_set.intersection(job_set)

    missing_skills = job_set - resume_set

    if len(job_set) > 0:
        match_score = len(matched_skills) / len(job_set) * 100
    else:
        match_score = 0

    return match_score, matched_skills, missing_skills


if __name__ == "__main__":

    resume_file = "data/extracted_skills.txt"
    job_file = "data/job_skills.txt"

    resume_skills = load_skills(resume_file)
    job_skills = load_skills(job_file)

    score, matched, missing = calculate_match(
        resume_skills,
        job_skills
    )

    print("\n===== MATCH RESULTS =====\n")

    print(f"Match Score: {score:.2f}%")

    print("\nMatched Skills:")
    for skill in matched:
        print(skill)

    print("\nMissing Skills:")
    for skill in missing:
        print(skill)

    # Save results
    with open("data/match_results.txt", "w") as f:

        f.write(f"Match Score: {score:.2f}%\n\n")

        f.write("Matched Skills:\n")
        for skill in matched:
            f.write(skill + "\n")

        f.write("\nMissing Skills:\n")
        for skill in missing:
            f.write(skill + "\n")

    print("\nMatch results saved to match_results.txt")