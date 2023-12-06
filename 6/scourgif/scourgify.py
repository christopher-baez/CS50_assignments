import os
import sys
import csv

if len(sys.argv) <= 2:
    print('Too few command-line arguments')
    sys.exit(1)
elif len(sys.argv) > 3:
    print('Too many commands-line arguments')
    sys.exit(1)
elif sys.argv[1].endswith('.csv') == False:
    print('Not a CSV file')
    sys.exit(1)
if not os.path.exists(sys.argv[1]):
    print("Could not read invalid_file.csv")
    sys.exit(1)
else:
    input_file = sys.argv[1]
    output_file = sys.argv[2]

# Process the input CSV and write to output CSV
# ... [previous code remains unchanged]

try:
    with open(input_file, newline='') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Write headers for the output CSV
        writer.writerow(['First', 'Last', 'House'])

        # Read each row from the input CSV, process, and write to output CSV
        for row in reader:
            if len(row) != 2 or len(row[0].split()) != 2:
                print(f"Skipping malformed row: {row}")
                continue  # Skip rows that don't have 2 elements or names that can't be split into two parts

            name, house = row
            first, last = name.split()
            writer.writerow([first, last, house])

except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)