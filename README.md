# Behavior-Based Insider Threat Detection System

This project monitors a local folder and detects suspicious file behaviors that might indicate insider threats. It observes activities such as:

- Unauthorized file creations, deletions, or modifications
- Script file handling (e.g., `.bat`, `.sh`, `.py`)
- Renaming or moving sensitive files

When such actions are detected, it prints alerts to the console and saves them in a log file.

---

## Project Structure

```
Behavior-Based Insider Threat Detection System/
│
├── main.py
├── requirements.txt
├── activity_log.json
│
├── analyzer/
│   └── behavior_analyzer.py
│
├── monitor/
│   └── file_watcher.py
│
├── logger/
│   └── activity_logger.py
│
├── sample_watch_dir/
│   └── (test files to trigger detection)
│
└── README.md
```

---

## Requirements

- Python 3.11 or higher  
- pip (Python package installer)  

---

## Setup Instructions

### 1. Install Python

Download Python 3.11+ from:  
https://www.python.org/downloads/

Make sure to check **"Add Python to PATH"** during installation.

---

### 2. Clone or Download the Project

If downloaded as a ZIP, extract it.  
Then open Command Prompt and go to the project folder:

```bash
cd "[your project folder location]"
```

---

### 3. (Optional) Create Virtual Environment

```bash
python -m venv insider-env
insider-env\Scripts\activate
```

---

### 4. Install Required Packages

```bash
pip install -r requirements.txt
```

---

### 5. Create Log File (if not exists)

Make sure `activity_log.json` exists in the root folder.

If it does not exist, create a new file and paste the following:

```json
[]
```

Save the file as `activity_log.json`.

---

### 6. Run the Program

```bash
python main.py
```

Expected output:

```
=== Behavior-Based Insider Threat Detection System ===
[+] Watching directory: D:\Projects\Behavior-Based Insider Threat Detection System\sample_watch_dir
[+] Monitoring directory: ...
```

---

### 7. Test It

Inside `sample_watch_dir`, try:

- Creating a file (e.g., `notes.txt`)
- Deleting a `.bat` or `.py` file
- Modifying any file's content
- Renaming files

These actions will generate alerts.

---

### 8. View Activity Log

Suspicious activity is saved to:

```
activity_log.json
```

Open it in any text editor or VS Code.

---

## Real-World Use Cases

- Simulating file monitoring in restricted environments
- Educating about behavioral monitoring techniques
- Prototype for insider threat detection systems
- Integrating with SIEM pipelines or security labs

---

## License

This project is open-source and available under the MIT License.
