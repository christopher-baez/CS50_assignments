import tabulate
import csv
import sys
import os

if len(sys.argv) <= 1:
    print('Too few command-line arguments')
    sys.exit(1)
elif len(sys.argv) > 2:
    print('Too many commands-line arguments')
    sys.exit(1)
elif sys.argv[1].endswith('.csv') == False:
    print('Not a CSV file')
    sys.exit(1)
if not os.path.exists(sys.argv[1]):
    print("The file does not exist.")
    sys.exit(1)
else:
    file_name = sys.argv[1]

menu = []
try:
    with open(file_name) as file:
        reader = csv.reader(file)
        for row in reader:
            menu.append({"Pizza": row[0], "Small": row[1], "Large": row[2]})
except FileNotFoundError:
    sys.exit(1)

print(tabulate.tabulate(menu, headers="firstrow", tablefmt="grid"))