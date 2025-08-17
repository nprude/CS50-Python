import csv
import os
import sys
from tabulate import tabulate
#In a file called pizza.py, implement a program that expects exactly one command-line argument,
# the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII
# art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the
# library’s grid format. If the user does not specify exactly one command-line argument, or if
# the specified file’s name does not end in .csv, or if the specified file does not exist,
# the program should instead exit via sys.exit.
def main():
    filename = ""
    testtable = []
    if len(sys.argv) != 2:

        if len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit(1)
        elif len(sys.argv) < 2:
            print("Too few command-line arguments")
            sys.exit(1)
    else:

        filename = sys.argv[1]
        print(filename)
    if not filename.endswith(".csv"):
        print("Not a csv file")
        sys.exit(1)
    else:

        pass
    if not os.path.exists(filename):
        raise FileNotFoundError("File does not exist")
    else:
       try:
           #method open opens filename as f
           with open(filename) as f:
               # Use the csv.reader to parse the file into rows
                reader = csv.reader(f)
               # Convert the reader object into a list of rows (each row is a list)
                rows = list(reader)
           # Separate header and data
           header = rows[0]
           data = rows[1:]

           # Use tabulate to format the table
           print(tabulate(data, headers=header, tablefmt="grid"))
       except Exception as e:
           print("Error reading file {e}")
if __name__ == "__main__":
    main()


