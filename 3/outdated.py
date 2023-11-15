def main():
    # List of month names for conversion
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    while True:
        try:
            # Prompt user for input
            date_input = input("Enter a date (MM/DD/YYYY or Month DD, YYYY): ").strip()

            # Try to parse the date and convert it to ISO 8601 format
            converted_date = convert_date(date_input, months)
            if converted_date:
                print(converted_date)
                break
            else:
                print("Invalid date. Please try again.")
        except EOFError:
            break

def convert_date(date_str, months):
    try:
        # Check if date is in numerical format
        if '/' in date_str:
            month, day, year = map(int, date_str.split('/'))
        # Check if date is in full month name format
        elif ',' in date_str and any(month_name in date_str for month_name in months):
            month_str, rest = date_str.split(' ', 1)
            day, year = map(int, rest.replace(',', '').split())
            month = months.index(month_str) + 1
        else:
            return None

        # Validate month and day ranges
        if 1 <= month <= 12 and 1 <= day <= 31:
            return f"{year:04d}-{month:02d}-{day:02d}"
        else:
            return None
    except ValueError:
        return None

# Execute the program
main()
