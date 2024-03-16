import datetime

# Placeholder data for demostration purposes
calendar_data = {
    "2024-03-15": [
        {"title": "Meeting with Client", "start_time": "09:00 AM", "end_time": "10:00 AM"},
        {"title": "Presentation", "start_time": "04:00 PM", "end_time": "05:00 PM"},
    ],
    "2024-03-16": [
        {"title": "Project Deadline", "start_time": "02:00 PM", "end_time": "03:00 PM"},
    ],
}

def display_main_menu():
    """Display the main menu options."""
    print("Main Menu:")
    print("1. View Calendar")
    print("2. Add Task/Event")
    print("3. Edit Task/Event")
    print("4. Delete Task/Event")
    print("5. Exit")

def get_user_choice():
    """Prompt the user to enter their choice and return it."""
    while True:
        choice = input("Enter Your Choice: ")
        if choice.isdigit() and 1 <= int(choice) <= 5:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def main_menu():
    """Main function to display the main menu and handle user input."""
    while True:
        display_main_menu()
        choice = get_user_choice()

        if choice == 1:
            view_calendar()
        elif choice == 2:
            add_task_event()
        elif choice == 3:
            edit_task_event()
        elif choice == 4:
            delete_task_event()
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break

def view_calendar():
    """Display the calendar with scheduled tasks/events"""

    # Prompt the user to select a date
    while True:
        selected_date = input("Enter the date (YYYY-MM-DD) to view (or 'exit' to return to the main menu): ").strip()
        if selected_date.lower() == "exit":
            return
        elif selected_date in calendar_data:
            break
        else:
            print("No tasks or events scheduled for the selected date. Please try again.")

    # Display tasks/events for the selected date
    print(f"\nTasks/Events for {selected_date}:")
    if calendar_data[selected_date]:
        for task in calendar_data[selected_date]:
            print(f"Title: {task['title']}")
            print(f"Start Time: {task['start_time']}")
            print(f"End Time: {task['end_time']}")
            print()
    else:
        print("No tasks/events scheduled for this date.")

def add_task_event(calendar_data):
    """Add a new task/event to the calendar"""
    print("Add Task/Event:")
    date = input("Enter the date (YYYY-MM-DD): ")

    # Validate the date format
    if not validate_date_format(date):
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return
    
    title = input("Enter the title: ").strip()
    start_time = input("Enter the start time (HH:MM AM/PM): ").strip()
    end_time = input("Enter the end time (HH:MM AM/PM): ").strip()

    # Validate the time format
    if not validate_time_format(start_time) or not validate_time_format(end_time):
        print("Invalid time format. Please enter the time in HH:MM AM/PM format.")
        return
    
    # Convert time to 24-hour for consistency
    start_time_24h = convert_to_24h_format(start_time)
    end_time_24h = convert_to_24h_format(end_time)

    # Check if the end time is after the start time
    if start_time_24h >= end_time_24h:
        print("End time must be after the start time. Please enter valid times.")
        return
    
    # Create a new task/event dictionary
    new_task_event = {
        "title": title,
        "start_time": start_time,
        "end_time": end_time,
    }

    # Add the new task/event to the calendar data
    if date not in calendar_data:
        calendar_data[date] = [new_task_event]
    else:
        calendar_data[date].append(new_task_event)

    print("Task/Event added successfully!")

    
def validate_date_format(date):
    """Validate the date format"""
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
def validate_time_format(time):
    """Validate the time format"""
    try:
        datetime.datetime.strptime(time, "%I:%M %p")
        return True
    except ValueError:
        return False
    
def convert_to_24h_format(time):
    """Convert time to 24-hour format"""
    return datetime.datetime.strptime(time, "%I:%M %p").strftime("%H:%M")

def edit_task_event(calendar_data):
    """Edit an existing task/event in the calendar."""
    print("Edit Task/Event:")

    # Prompt the user to enter the date and title of the task/event to edit
    date = input("Enter the date (YYYY-MM-DD) of the task/event to edit: ").strip()
    title = input("Enter the title of the Task/Event to edit: ").strip()

    # Check if the date exists in the calendar data
    if date not in calendar_data or not any(task['title'] == title for task in calendar_data[date]):
        print("Task/Event not found in the calendar.")
        return
    
    # Find the task/event to edit
    task_to_edit = None
    for task in calendar_data[date]:
        if task['title'] == title:
            task_to_edit = task
            break
    
    # Prompt the user to enter new details for the task/event
    new_title = input("Enter the new title (or leave empty to keep current title): ").strip()
    new_start_time = input("Enter the start time (HH:MM AM/PM) (leave empty to keep current time): ").strip()
    new_end_time = input("Enter the new end time (HH:MM AM/PM) (leave empty to keep current end time): ").strip()

    # Update task/event details if new values are provided
    if new_title:
        task_to_edit['title'] = new_title
    if new_start_time:
        # Validate the new start time format
        if not validate_time_format(new_start_time):
            print("Invalid start time format. Please enter the time in HH:MM AM/PM format.")
            return
        task_to_edit['start_time'] = new_start_time
    if new_end_time:
        # Validate the new end time format
        if not validate_time_format(new_end_time):
            print("Invalid end time format. Please enter the time in HH:MM AM/PM format.")
            return
        # Check if the new end time is after the start time
        if convert_to_24h_format(new_end_time) <= convert_to_24h_format(task_to_edit['start_time']):
            print("End time must be after start time. Please enter a valid end time.")
            return
        task_to_edit['end_time'] = new_end_time

    print("Task/Event edited successfully!")

def delete_task_event(calendar_data):
    """Delete an existing task/event from the calendar."""
    print("Delete Task/Event:")

    # Prompt the user to enter the date and title of the task/event to delete
    date = input("Enter the date (YYYY-MM-DD) of the task/event to delete: ").strip()
    title = input("Enter the title of the Task/Event to delete: ").strip()

    # Check if the date exists in the calendar data
    if date not in calendar_data or not any(task['title'] == title for task in calendar_data[date]):
        print("Task/Event not found in the calendar.")
        return
    
    # Find the task/event to delete
    task_to_delete = None
    for task in calendar_data[date]:
        if task['title'] == title:
            task_to_delete = task
            break
    
    # Confirm deletion with the user
    confirmation = input(f"Are you sure you want to delete '{title}' scheduled for {date}? (yes/no): ").strip().lower()
    if confirmation != "yes":
        print("Deletion canceled.")
        return
    
    # Remove the task/event from the calendar data
    calendar_data[date].remove(task_to_delete)
    print("Task/Event deleted successfully!")

while True:
    display_main_menu()
    choice = get_user_choice()
    if choice == 5:
        print("Exiting the program. Goodbye!")
        break
    elif choice == 1:
        view_calendar()
    elif choice == 2:
        add_task_event(calendar_data)
    elif choice == 3:
        edit_task_event(calendar_data)
    elif choice == 4:
        delete_task_event(calendar_data)
