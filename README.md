# Cybersecurity Threat Brief Generator

Cybersecurity Threat Brief Generator is a lightweight web app designed to simplify security analysis by automatically summarizing long CVE/NVD/vendor advisories into concise, plain-English briefs. It helps security analysts and students quickly understand vulnerabilities, their impact, and recommended mitigations without reading lengthy technical documents.

## Key Features:
• Advisory Summarization: Converts long CVE or vendor advisories into short, actionable summaries.
• Impact & Mitigation Extraction: Highlights affected systems, severity, and recommended fixes.
• PDF Export: Allows downloading structured briefs for documentation or sharing.
• Local, Privacy-Friendly Execution: Runs using small Hugging Face or Ollama models without external API calls.

## Installation
1. Clone or unzip the project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open in browser: http://127.0.0.1:5000
