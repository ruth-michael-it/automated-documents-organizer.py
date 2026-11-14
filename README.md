# automated-documents-organizer.py
# Automated Document Organizer & Audit Logger

A lightweight, cross-platform Python automation utility designed to eliminate manual file sorting by monitoring a user's `Downloads` directory, classifying PDF and Word documents using rule-based keyword matching, and maintaining a timestamped audit log.

## Everyday Problem Solved
Managing job applications, employment reference letters, tax forms, and onboarding contracts often leads to a cluttered `Downloads` folder and misplaced files. This script automates routine file housekeeping while enforcing defensive file-handling rules to prevent accidental data overwrites.

## Key Features & Engineering Practices
* **Cross-Platform Path Resolution:** Uses Python's built-in `os.path.expanduser` and `os.path.join` so the script runs seamlessly across Windows, Linux, and macOS without hardcoded paths.
* **Rule-Based Keyword Classification:** Dynamically routes documents into structured subfolders (`Job_Applications`, `Amazon_Onboarding`, `Certificates`, `Government_Visa`, and `Other_Documents`) based on case-insensitive filename matching.
* **Zero Data-Loss Protection:** Checks destination directories with `os.path.exists()` before moving files and appends a unique timestamp (`HHMMSS`) if a filename collision occurs.
* **Persistent Audit Trail:** Records every file movement with an ISO-style timestamp in `organizer_log.txt` for administrative traceability and troubleshooting.

## Project Structure
```text
automated-document-organizer/
├── document_organizer.py   # Main Python automation script
├── README.md               # Project documentation
└── screenshots/
    └── demo_output.png     # Terminal execution and log sample
```

## Prerequisites
* **Python 3.8+** (Uses only Python standard libraries: `os`, `shutil`, `datetime` — no external `pip` installations required).

## How to Run
1. Clone this repository or download `document_organizer.py`:
   ```bash
   git clone https://github.com
   cd automated-document-organizer
   ```
2. Run the script from your terminal:
   ```bash
   python document_organizer.py
   ```
3. Check `~/Documents/Organized_Files/` to view your sorted subfolders and inspect `organizer_log.txt`.

## Sample Output
```text
Moved: Lebenslauf_Michael_Ruth_Onyinyechi.pdf -> Job_Applications/
Moved: Arbeitszeugnisse_Referenzen_Michael_Ruth.pdf -> Job_Applications/
Moved: Amazon_Contract_Dresden.pdf -> Amazon_Onboarding/

Done! Organized 3 document(s). Check ~/Documents/Organized_Files/organizer_log.txt for audit logs.
```

## Future Enhancements
* Add a `--dry-run` command-line flag using `argparse` to preview file movements safely before execution.
* Configure automated daily execution via **Windows Task Scheduler** or a Linux **cron** job.

