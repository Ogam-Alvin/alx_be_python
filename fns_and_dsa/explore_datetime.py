# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format it into "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    # Add the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    # Format into "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date

def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Ask user how many days to add
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days)
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()
