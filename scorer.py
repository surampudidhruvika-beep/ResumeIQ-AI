def calculate_score(resume_text):

    score = 0
    feedback = []

    resume = resume_text.lower()

    category_scores = {
        "ATS Compatibility": 0,
        "Education": 0,
        "Technical Skills": 0,
        "Projects": 0,
        "Certifications": 0,
        "Achievements": 0
    }

    # ATS Compatibility
    category_scores["ATS Compatibility"] = 18
    score += 18

    # Education
    if "b.tech" in resume or "bachelor" in resume:
        category_scores["Education"] = 9
        score += 9
    else:
        feedback.append("Add your education details.")

    # Technical Skills
    skills = [
        "python", "java", "sql", "html", "css",
        "javascript", "flask", "machine learning"
    ]

    found = sum(skill in resume for skill in skills)

    tech_score = min(found * 2, 20)
    category_scores["Technical Skills"] = tech_score
    score += tech_score

    if tech_score < 12:
        feedback.append("Add more technical skills.")

    # Projects
    if "project" in resume:
        category_scores["Projects"] = 15
        score += 15
    else:
        feedback.append("Add academic or personal projects.")

    # Certifications
    if "certification" in resume or "oracle" in resume:
        category_scores["Certifications"] = 9
        score += 9
    else:
        feedback.append("Add certifications.")

    # Achievements
    if "achievement" in resume or "award" in resume:
        category_scores["Achievements"] = 8
        score += 8
    else:
        feedback.append("Mention your achievements.")

    if score > 100:
        score = 100

    return score, feedback, category_scores
    text = text.lower()

    # Skills
    skills = [
        "python", "java", "c++", "sql", "html", "css",
        "javascript", "flask", "machine learning",
        "data science", "power bi", "excel"
    ]

    found_skills = [skill for skill in skills if skill in text]

    score += min(len(found_skills) * 5, 30)

    if len(found_skills) < 5:
        feedback.append("Add more technical skills.")

    # Education
    if "b.tech" in text or "bachelor" in text or "degree" in text:
        score += 20
    else:
        feedback.append("Mention your education clearly.")

    # Projects
    if "project" in text:
        score += 20
    else:
        feedback.append("Add academic or personal projects.")

    # Certifications
    if "certificate" in text or "certification" in text:
        score += 15
    else:
        feedback.append("Include certifications.")

    # Experience
    if "experience" in text or "internship" in text:
        score += 15
    else:
        feedback.append("Mention internships or work experience.")

    return score, feedback