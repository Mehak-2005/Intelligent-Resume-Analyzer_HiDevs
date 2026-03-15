import re

class ResumeParser:

    def __init__(self, text):
        self.text = text

    def extract_name(self):
        lines = self.text.split("\n")
        return lines[0].strip()

    def extract_email(self):
        match = re.search(r'\S+@\S+', self.text)
        return match.group() if match else "Not Found"

    def extract_skills(self):

        skills_db = [
            "python","java","sql","machine learning",
            "data analysis","html","css","javascript"
        ]

        found = []

        for skill in skills_db:
            if skill.lower() in self.text.lower():
                found.append(skill)

        return found

    def extract_experience(self):

        exp = re.findall(r'(\d+)\s+years', self.text.lower())

        if exp:
            return int(exp[0])

        return 0

    def parse(self):

        return {
            "name": self.extract_name(),
            "email": self.extract_email(),
            "skills": self.extract_skills(),
            "experience": self.extract_experience()
        }