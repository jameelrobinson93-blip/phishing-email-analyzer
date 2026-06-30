# Phishing Email Analyzer

## Description

The Phishing Email Analyzer is a Python application that scans suspicious emails and identifies common phishing indicators such as urgent language, suspicious URLs, executable attachments, and risky sender information.

This project demonstrates basic phishing analysis techniques commonly used by Security Operations Center (SOC) Analysts when investigating suspicious emails.

---

## Features

- Detects urgent phishing language
- Identifies suspicious hyperlinks
- Detects executable (.exe) attachments
- Displays sender information
- Calculates a phishing risk score
- Classifies emails as Low, Medium, or High Risk

---

## Tech Stack

- Python
- Regular Expressions (re)
- Git
- GitHub

---

## Project Structure

```
phishing-email-analyzer/
│
├── analyzer.py
├── sample_email.txt
├── requirements.txt
├── README.md
├── screenshots/
└── reports/
```

---

## How to Run

Clone the repository

```bash
git clone https://github.com/jameelrobinson93-blip/phishing-email-analyzer.git
```

Open the project folder

```bash
cd phishing-email-analyzer
```

Run the analyzer

```bash
python analyzer.py
```

---

## Sample Output

The analyzer checks for:

- Urgent language
- Suspicious links
- Executable attachments
- Sender information
- Overall phishing risk score

---

## Future Improvements

- SPF validation
- DKIM validation
- DMARC validation
- VirusTotal API integration
- GUI interface
- PDF report generation
- Email header analysis

---

## Skills Demonstrated

- Python Programming
- Cybersecurity Fundamentals
- Phishing Detection
- Regular Expressions
- Git Version Control
- GitHub Repository Management
- Technical Documentation

---

## Author

**Jameel Robinson**

Aspiring SOC Analyst | Cybersecurity Enthusiast
