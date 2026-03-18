import re
from models import Candidate
from errors import ParseError


def parse_resume(text: str) -> Candidate:
    try:
        name_match = re.search(r"Name:\s*(.*)", text)
        email_match = re.search(r"Email:\s*(.*)", text)
        skills_match = re.search(r"Skills:\s*(.*)", text)
        exp_match = re.search(r"Experience:\s*(\d+)", text)
        edu_match = re.search(r"Education:\s*(.*)", text)

        name = name_match.group(1).strip()
        email = email_match.group(1).strip()
        skills = [s.strip() for s in skills_match.group(1).split(",")]
        experience = int(exp_match.group(1))
        education = edu_match.group(1).strip()

        return Candidate(
            name=name,
            email=email,
            skills=skills,
            experience=experience,
            education=education
        )

    except Exception as e:
        raise ParseError(f"Failed to parse resume: {e}")