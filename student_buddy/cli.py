from .data_manager import load_data
from . import operations

def start_cli():
    """Starts the command-line interface for Student Buddy."""
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

        if choice == "1": operations.add_task(data)
        elif choice == "2": operations.view_tasks(data)
        elif choice == "3": operations.add_note(data)
        elif choice == "4": operations.view_notes(data)
        elif choice == "5": operations.add_timetable(data)
        elif choice == "6": operations.view_timetable(data)
        elif choice == "7": operations.log_study_hours(data)
        elif choice == "8": operations.view_study_hours(data)
        elif choice == "9": break
        else: print("❌ Invalid choice!")
