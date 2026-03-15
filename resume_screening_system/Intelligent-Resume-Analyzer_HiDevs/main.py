from resume_parser import ResumeParser
from matcher import JobMatcher
from report_generator import ReportGenerator
from file_handler import FileHandler

def load_resume(path):

    with open(path,"r") as f:
        return f.read()

def main():

    job_requirements = {
        "skills": ["python","sql","machine learning"],
        "experience": 2
    }

    resume_text = load_resume("resume/resume.txt")

    parser = ResumeParser(resume_text)
    candidate = parser.parse()

    matcher = JobMatcher(job_requirements)
    score = matcher.calculate_score(candidate)

    report = ReportGenerator(candidate,score)

    print(report.generate())

    data = FileHandler.load_json("data/candidates.json")

    data.append({
        "name": candidate["name"],
        "email": candidate["email"],
        "score": score
    })

    FileHandler.save_json(data,"data/candidates.json")


if __name__ == "__main__":
    main()