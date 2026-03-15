class JobMatcher:

    def __init__(self, job_requirements):
        self.job = job_requirements

    def calculate_score(self, candidate):

        required_skills = set(self.job["skills"])
        candidate_skills = set(candidate["skills"])

        matched = required_skills.intersection(candidate_skills)

        skill_score = (len(matched) / len(required_skills)) * 70

        required_exp = self.job["experience"]
        candidate_exp = candidate["experience"]

        if candidate_exp >= required_exp:
            exp_score = 30
        else:
            exp_score = (candidate_exp / required_exp) * 30

        total = skill_score + exp_score

        return round(total,2)