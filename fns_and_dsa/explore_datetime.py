from datetime import datetime, timedelta


def display_current_datetime():
    """Displays the current date and time."""
    current_date = datetime.now()
    # Format: YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

def calculate_future_date(days_to_add):
    """Calculates the date after adding a certain number of days to the current date."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Date after {days_to_add} days will be:", formatted_future_date)

def main():
    # Display current date and time
    display_current_datetime()

    #ask user for number of days to add
    try:
        days = int(input("Enter number of days to add to current date: "))
        result = calculate_future_date(days)
        print(f"Future Date: {result}")

    except ValueError:
        print("Please enter a valid integer for days.")

if __name__ == "__main__":
    main()
    
