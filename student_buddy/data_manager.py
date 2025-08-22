import json
import os

DATA_FILE = "student_buddy.json"

def load_data():
    """Loads data from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"tasks": [], "notes": [], "timetable": {}, "study_hours": []}

def save_data(data):
    """Saves data to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
