import json
import os

DATA_FILE = "student_buddy.json"

# Load data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"tasks": [], "notes": [], "timetable": {}, "study_hours": []}

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Menu functions
def add_task(data):
    task = input("Enter new task: ")
    data["tasks"].append(task)
    save_data(data)
    print("✅ Task added!")

def view_tasks(data):
    if not data["tasks"]:
        print("No tasks yet.")
    else:
        for i, task in enumerate(data["tasks"], 1):
            print(f"{i}. {task}")

def add_note(data):
    note = input("Write your note: ")
    data["notes"].append(note)
    save_data(data)
    print("✅ Note saved!")

def view_notes(data):
    if not data["notes"]:
        print("No notes yet.")
    else:
        for i, note in enumerate(data["notes"], 1):
            print(f"{i}. {note}")

def add_timetable(data):
    day = input("Enter day (e.g. Monday): ")
    subject = input("Enter subject: ")
    data["timetable"].setdefault(day, []).append(subject)
    save_data(data)
    print("✅ Timetable updated!")

def view_timetable(data):
    if not data["timetable"]:
        print("No timetable yet.")
    else:
        for day, subjects in data["timetable"].items():
            print(f"{day}: {', '.join(subjects)}")

def log_study_hours(data):
    hours = float(input("Enter study hours: "))
    data["study_hours"].append(hours)
    save_data(data)
    print("✅ Study hours logged!")

def view_study_hours(data):
    if not data["study_hours"]:
        print("No study hours logged yet.")
    else:
        total = sum(data["study_hours"])
        print(f"Total study hours: {total}")
        print("Logs:", data["study_hours"])

# Main menu
def main():
    data = load_data()
    while True:
        print("\n===== Student Buddy =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Add Note")
        print("4. View Notes")
        print("5. Add Timetable Entry")
        print("6. View Timetable")
        print("7. Log Study Hours")
        print("8. View Study Hours")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1": add_task(data)
        elif choice == "2": view_tasks(data)
        elif choice == "3": add_note(data)
        elif choice == "4": view_notes(data)
        elif choice == "5": add_timetable(data)
        elif choice == "6": view_timetable(data)
        elif choice == "7": log_study_hours(data)
        elif choice == "8": view_study_hours(data)
        elif choice == "9": break
        else: print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
