from parser import parse_resume
from matcher import match_candidate
from reporter import generate_analysis_report
from file_manager import save_results
from models import JobRequirement


def load_resume_from_file(filename):

    with open(filename, "r") as f:
        text = f.read()

    return parse_resume(text)


def main():

    # Load Resume
    candidate = load_resume_from_file("sample_resume.txt")

    # Job Requirements
    job = JobRequirement(
        title="Python Developer",
        required_skills=["Python", "SQL", "Machine Learning", "Git"],
        min_experience=2,
        education_required="B.Tech"
    )

    # Match Candidate
    score, matched_skills, missing_skills = match_candidate(candidate, job)

    # Generate Report
    report = generate_analysis_report(
        candidate,
        job,
        score,
        matched_skills,
        missing_skills
    )

    print(report)

    # Save results
    result_data = {
        "candidate": candidate.name,
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }

    save_results(result_data, "results.json")


if __name__ == "__main__":
    main()