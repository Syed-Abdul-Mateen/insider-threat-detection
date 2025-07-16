# Behavior-Based Insider Threat Detection System

This project monitors a local folder and detects suspicious file behaviors that might indicate insider threats. It observes activities such as:

- Unauthorized file creations, deletions, or modifications
- Script file handling (e.g., .bat, .sh, .py)
- Renaming or moving sensitive files

When such actions are detected, it prints alerts to the console and saves them in a log file.

---

## Project Structure

Behavior-Based Insider Threat Detection System/
│
├── analyzer/
│   └── behavior_analyzer.py         # Analyzes behavior and assigns threat levels
│
├── logger/
│   └── activity_logger.py           # Saves alerts to a JSON log file
│
├── monitor/
│   └── file_watcher.py              # Monitors filesystem for suspicious changes
│
├── sample_watch_dir/                # Folder to be monitored
│   └── (add test files here)
│
├── activity_log.json                # Log of all suspicious activity
├── requirements.txt                 # Python dependencies
├── main.py                          # Entry point to run the system
└── README.md                        # Project documentation

---

## Requirements

- Python 3.11 or higher  
- pip (Python package installer)  

---

## Setup Instructions

### 1. Install Python

Download Python 3.11+ from:  
https://www.python.org/downloads/

Make sure to check "Add Python to PATH" during installation.

---

### 2. Clone or Download the Project

If downloaded as ZIP, extract it.  
Then open Command Prompt and go to the project folder:

cd "D:\Projects\Behavior-Based Insider Threat Detection System"

---

### 3. (Optional) Create Virtual Environment

python -m venv insider-env  
insider-env\Scripts\activate

---

### 4. Install Required Packages

pip install -r requirements.txt

---

### 5. Create Log File (if not exists)

Make sure the following file exists in the root:

[]

Save this as activity_log.json if not already present.

---

### 6. Run the Program

python main.py

Expected output:

=== Behavior-Based Insider Threat Detection System ===  
[+] Watching directory: D:\Projects\Behavior-Based Insider Threat Detection System\sample_watch_dir  
[+] Monitoring directory: ...

---

### 7. Test It

Inside sample_watch_dir, try:

- Creating a file (e.g., notes.txt)
- Deleting a .bat or .py file
- Modifying any file's content
- Renaming files

These actions will generate alerts.

---

### 8. View Activity Log

Suspicious activity is saved to:

activity_log.json

Open it in any text editor or with VS Code.

---

## Real-World Use Cases

- Simulating file monitoring in restricted environments
- Educating about behavioral monitoring techniques
- Prototype for insider threat detection systems
- Integrating with SIEM pipelines or security labs

---

## License

This project is open-source and available under the MIT License.
