import json


def save_results(results, filename):

    with open(filename, "w") as f:
        json.dump(results, f, indent=4)


def load_job_requirements(filename):

    with open(filename, "r") as f:
        data = json.load(f)

    return data