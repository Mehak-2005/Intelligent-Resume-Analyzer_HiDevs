def generate_analysis_report(candidate, job, score, matched_skills, missing_skills):

    if score >= 80:
        recommendation = "✅ STRONGLY RECOMMEND"
    elif score >= 60:
        recommendation = "✓ RECOMMEND"
    elif score >= 40:
        recommendation = "⚠ MAYBE"
    else:
        recommendation = "✗ NOT RECOMMENDED"

    report = f"""
=======================================
        CANDIDATE ANALYSIS REPORT
=======================================

Candidate Name : {candidate.name}
Email          : {candidate.email}
Job Position   : {job.title}

Match Score    : {score}/100

----- SKILLS ANALYSIS -----

Matched Skills :
{', '.join(matched_skills)}

Missing Skills :
{', '.join(missing_skills)}

Experience     : {candidate.experience} years
Education      : {candidate.education}

----- RECOMMENDATION -----

{recommendation}

=======================================
"""

    return report