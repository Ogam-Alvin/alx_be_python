# daily_reminder.py

# Prompt user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to handle priority
match priority:
    case "high":
        reminder_text = f"'{task}' is a high priority task"
    case "medium":
        reminder_text = f"'{task}' is a medium priority task"
    case "low":
        reminder_text = f"'{task}' is a low priority task"
    case _:
        reminder_text = f"'{task}' has an undefined priority"

# Modify reminder based on time sensitivity
if time_bound == "yes":
    reminder_text += " that requires immediate attention today!"
else:
    reminder_text += ". Consider completing it when you have free time."

# Print exactly as expected
print(f"Reminder: {reminder_text}")
