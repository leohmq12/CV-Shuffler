# CV Shuffler and Candidate Selector

A desktop application built with Python and PyQt5 for HR professionals to efficiently filter through CVs based on keyword matching.

## Features

- Load and shuffle multiple CV files (PDF, DOCX, TXT)
- Keyword-based filtering with customizable categories
- Database-driven keyword management
- Original format CV preview with QtWebEngine
- Automatic candidate selection based on match thresholds
- Export selected candidates to CSV or text files

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/cv-shuffler.git
cd cv-shuffler

## Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate

## Install dependencies
pip install -r requirements.txt

## Setup Database
python setup_database.py

## Run the application
python cv_shuffler.py

## USAGE
    Click "Load CVs" to select CV files

    Use the keyword manager to add relevant keywords for different job categories

    Apply keyword filters and set match thresholds

    Preview CVs in their original format

    Select candidates manually or use auto-selection

    Export your shortlist for further review

## Requirements
    Python 3.6+

    PyQt5

    PyQtWebEngine

    pandas

    python-docx

    PyPDF2

## LICENSE
This project is under the MIT License


