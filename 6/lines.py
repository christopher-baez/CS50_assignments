import sys
import os


def count_lines_of_code(filename):
    """ Count the number of lines of code in a Python file, excluding comments and blank lines. """
    with open(filename, 'r') as file:
        lines = file.readlines()

    code_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
    return len(code_lines)


# Check the number of command line arguments
arg_count = len(sys.argv)

if arg_count < 2:
    print("Error: Too few command-line arguments.")
    sys.exit(1)
elif arg_count > 2:
    print("Error: Too many command-line arguments.")
    sys.exit(1)

filename = sys.argv[1]

# Check if the file ends with .py
if not filename.endswith('.py'):
    print("Error: Too few command-line arguments.")
    sys.exit(1)

# Check if the file exists
if not os.path.exists(filename):
    print(f"Error: The file {filename} does not exist.")
    sys.exit(1)

# Count the lines of code
line_count = count_lines_of_code(filename)
print(f"The file {filename} contains {line_count} lines of Python code.")
