def load_missing_skills(file_path):

    missing_skills = []

    with open(file_path, "r") as f:
        lines = f.readlines()

    start_reading = False

    for line in lines:

        line = line.strip().lower()

        if "missing skills" in line:
            start_reading = True
            continue

        if start_reading and line != "":
            missing_skills.append(line)

    return missing_skills


# Learning suggestions database
SKILL_RESOURCES = {

    "react": "Learn frontend development using React",

    "kubernetes": "Learn container orchestration using Kubernetes",

    "node.js": "Learn backend JavaScript using Node.js",

    "redis": "Learn caching systems using Redis",

    "graphql": "Learn modern API design using GraphQL",

    "docker": "Learn containerization using Docker",

    "tensorflow": "Learn deep learning using TensorFlow",

    "mongodb": "Learn NoSQL database concepts",

    "aws": "Learn cloud deployment using AWS"

}


def recommend_learning(missing_skills):

    recommendations = {}

    for skill in missing_skills:

        if skill in SKILL_RESOURCES:
            recommendations[skill] = SKILL_RESOURCES[skill]

        else:
            recommendations[skill] = "Search tutorials online"

    return recommendations


if __name__ == "__main__":

    match_file = "data/match_results.txt"

    missing_skills = load_missing_skills(match_file)

    recommendations = recommend_learning(missing_skills)

    print("\n===== SKILL GAP RECOMMENDATIONS =====\n")

    with open("data/recommendations.txt", "w", encoding="utf-8") as f:

        f.write("Skill Gap Recommendations:\n\n")

        for skill, suggestion in recommendations.items():

            line = f"{skill} -> {suggestion}"

            print(line)

            f.write(line + "\n")

    print("\nRecommendations saved to recommendations.txt")