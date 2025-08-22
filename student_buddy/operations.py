from .data_manager import save_data

def add_task(data):
    """Adds a new task."""
    task = input("Enter new task: ")
    data["tasks"].append(task)
    save_data(data)
    print("✅ Task added!")

def view_tasks(data):
    """Displays all tasks."""
    if not data["tasks"]:
        print("No tasks yet.")
    else:
        for i, task in enumerate(data["tasks"], 1):
            print(f"{i}. {task}")

def add_note(data):
    """Adds a new note."""
    note = input("Write your note: ")
    data["notes"].append(note)
    save_data(data)
    print("✅ Note saved!")

def view_notes(data):
    """Displays all notes."""
    if not data["notes"]:
        print("No notes yet.")
    else:
        for i, note in enumerate(data["notes"], 1):
            print(f"{i}. {note}")

def add_timetable(data):
    """Adds a new entry to the timetable."""
    day = input("Enter day (e.g. Monday): ")
    subject = input("Enter subject: ")
    data["timetable"].setdefault(day, []).append(subject)
    save_data(data)
    print("✅ Timetable updated!")

def view_timetable(data):
    """Displays the timetable."""
    if not data["timetable"]:
        print("No timetable yet.")
    else:
        for day, subjects in data["timetable"].items():
            print(f"{day}: {', '.join(subjects)}")

def log_study_hours(data):
    """Logs study hours."""
    try:
        hours = float(input("Enter study hours: "))
        data["study_hours"].append(hours)
        save_data(data)
        print("✅ Study hours logged!")
    except ValueError:
        print("❌ Invalid input! Please enter a number.")

def view_study_hours(data):
    """Displays total study hours."""
    if not data["study_hours"]:
        print("No study hours logged yet.")
    else:
        total = sum(data["study_hours"])
        print(f"Total study hours: {total}")
        print("Logs:", data["study_hours"])
