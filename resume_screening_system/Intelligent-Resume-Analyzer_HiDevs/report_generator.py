class ReportGenerator:

    def __init__(self, candidate, score):
        self.candidate = candidate
        self.score = score

    def recommendation(self):

        if self.score >= 75:
            return "Strong Hire"
        elif self.score >= 50:
            return "Consider"
        else:
            return "Reject"

    def generate(self):

        report = f"""
----- Candidate Report -----

Name: {self.candidate['name']}
Email: {self.candidate['email']}
Skills: {', '.join(self.candidate['skills'])}
Experience: {self.candidate['experience']} years

Match Score: {self.score}/100
Recommendation: {self.recommendation()}

----------------------------
"""

        return report