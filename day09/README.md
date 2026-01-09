Day 09 — Assignment Submission Analysis Report
Overview

This project analyzes student assignment submissions based on the file
subjects.txt, which contains submission metadata exported from the course system.

The goal of the program is to automatically generate useful reports for the course staff, including:

Identifying students who did not submit assignments

Detecting late submissions (when deadlines are provided)

Producing summary statistics per assignment

Exporting all results into easy-to-use CSV files

This replaces manual inspection of submission logs and allows quick validation and overview of class progress.

Input Data
subjects.txt

The program expects a plain text file located at:

day09/subjects.txt


Each line represents a submission and is tab-separated, for example:

12345	submitted	Day08 by Alice Smith		2025-01-07T21:13:45Z

Parsing rules:

The assignment name and student name are extracted from titles formatted as:

<Assignment> by <Student Name>


If a submission timestamp is present (ISO 8601 format), it is parsed.

Lines without timestamps are treated as missing submissions.

Optional Input: Deadlines

You may optionally provide a CSV file containing assignment deadlines:

assignment,deadline
Day08,2025-01-07T23:59:59Z
Day07,2025-01-05T23:59:59Z


This allows the program to classify submissions as:

On-time

Late

Run with deadlines:

python day09/report_day09.py --deadlines day09/deadlines.csv

Output

After running the program, the following CSV files are generated in day09/:

File	Description
submissions_parsed.csv	Full parsed table with submission times and status
missing_submissions.csv	Students who did not submit
late_submissions.csv	Submissions after the deadline
submission_summary.csv	Counts of missing / on-time / late per assignment

In addition, concise tables are printed directly to the terminal.

Status Classification Logic
Condition	Status
No submission timestamp	missing
Submission exists, no deadline	submitted (deadline unknown)
Submission ≤ deadline	on-time
Submission > deadline	late
How to Run

From the repository root:

python day09/report_day09.py


Optional flags:

--deadlines <path>   # CSV file with deadlines
--no-save            # Print results only, do not save CSVs

File Structure
day09/
│
├── subjects.txt
├── report_day09.py
├── submissions_parsed.csv
├── missing_submissions.csv
├── late_submissions.csv
├── submission_summary.csv
└── README.md

Technologies Used

Python 3

pandas – data parsing and analysis

argparse – command-line interface

regex – extracting student and assignment names

AI Usage Disclosure

GitHub Copilot was used to assist with:

Initial parsing logic

Structuring the reporting pipeline

All generated code was manually reviewed, adapted, and debugged to correctly handle the provided subjects.txt format and course requirements.