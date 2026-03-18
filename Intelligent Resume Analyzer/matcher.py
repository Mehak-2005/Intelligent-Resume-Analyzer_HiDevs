from models import Candidate, JobRequirement


def match_candidate(candidate: Candidate, job: JobRequirement):

    score = 0

    # Skill matching
    matched_skills = set(candidate.skills) & set(job.required_skills)
    missing_skills = set(job.required_skills) - set(candidate.skills)

    skill_score = len(matched_skills) * 10
    score += skill_score

    # Experience check
    if candidate.experience >= job.min_experience:
        score += 30

    # Education check
    if candidate.education.lower() == job.education_required.lower():
        score += 20

    score = min(score, 100)

    return score, list(matched_skills), list(missing_skills)