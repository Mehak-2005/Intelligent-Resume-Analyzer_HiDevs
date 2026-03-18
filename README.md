# Intelligent Resume Analyzer

## Overview

The **Intelligent Resume Analyzer** is a Python-based application designed to automate the initial stage of the hiring process. Instead of manually reviewing resumes, this system reads resume data, extracts important information, compares it with job requirements, and generates a detailed analysis report.

This project demonstrates how Python can be used to build a simple but effective **resume screening system** that helps recruiters identify suitable candidates quickly.

---

## Problem Statement

Recruiters often receive hundreds of resumes for a single job opening. Manually reviewing each resume can be time-consuming and inefficient.

This project aims to solve that problem by creating a system that:

* Parses resume information
* Extracts candidate details
* Matches candidate skills with job requirements
* Calculates a match score
* Generates hiring recommendations automatically

---

## Key Features

* **Resume Parsing**
  Extracts candidate name, email, skills, experience, and education from resume text.

* **Skill Matching Algorithm**
  Compares candidate skills with job requirements and calculates a match score (0–100).

* **Automated Recommendation System**
  Generates hiring recommendations such as:

  * Strongly Recommend
  * Recommend
  * Maybe
  * Not Recommended

* **Structured Report Generation**
  Produces a clean and readable analysis report for recruiters.

* **JSON Data Handling**
  Saves analysis results in JSON format for easy storage and reuse.

* **Modular Python Architecture**
  The system is divided into separate modules for parsing, matching, reporting, and file management.

---

## Project Structure

smart_hiring_assistant/
│
├── main.py                # Main program execution
├── parser.py              # Resume parsing logic
├── matcher.py             # Candidate-job matching algorithm
├── reporter.py            # Report generation
├── models.py              # Data models (Candidate, JobRequirement)
├── file_manager.py        # JSON file operations
├── errors.py              # Custom error handling
├── sample_resume.txt      # Sample resume input
├── job_requirements.json  # Job requirement data
├── results.json           # Generated analysis output
├── requirements.txt       # Required Python packages
└── README.md              # Project documentation
---

## Evaluation Criteria Covered

This project meets the following evaluation goals:

* Clean and modular Python code
* Accurate resume parsing
* Skill-based matching algorithm
* JSON file operations for input/output
* Automated report generation
* Error handling for invalid data

---

## Demo Video

Demo Link: *Paste your YouTube video link*

---

## Author

Mehak

This project was created as part of a practical exercise to demonstrate Python programming, software architecture, and problem-solving in the hiring automation domain.
