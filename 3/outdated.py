def main():
    # List of month names for conversion
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    while True:
        try:
            # Prompt user for input
            date_input = input("Date: ").strip()

            # Try to parse the date and convert it to ISO 8601 format
            converted_date = convert_date(date_input, months)
            if converted_date:
                print(converted_date)
                break
            else:
                continue
        except EOFError:
            break

def convert_date(date_str, months):
    try:
        # Check if date is in numerical format
        if '/' in date_str:
            month, day, year = map(int, date_str.split('/'))
        # Check if date is in full month name format
        elif ',' in date_str:
            parts = date_str.split()
            if len(parts) == 3 and parts[1].replace(',', '').isdigit() and parts[2].isdigit():
                month_str = parts[0]
                day = int(parts[1].replace(',', ''))
                year = int(parts[2])

                if month_str in months:
                    month = months.index(month_str) + 1
                else:
                    return None
            else:
                return None
        else:
            return None

        # Validate month and day ranges
        if 1 <= month <= 12 and 1 <= day <= 31:
            return f"date: {year:04d}-{month:02d}-{day:02d}"
        else:
            return None
    except ValueError:
        return None

# Execute the program
main()
