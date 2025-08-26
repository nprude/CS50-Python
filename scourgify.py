import os, sys, csv
'''
In a file called scourgify.py, implement a program that:
Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed 
to be, in order, name and house, and the name of a new CSV to write as output, 
whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. 
Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot 
be read, the program should exit via sys.exit with an error message.
'''
def main():
    before = ""
    after = ""

    if len(sys.argv) != 3:

        if len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit(1)
        elif len(sys.argv) < 2:
            print("Too few command-line arguments")
            sys.exit(1)
    else:

        before = sys.argv[1]
        after = sys.argv[2]

    if not before.endswith(".csv"):
        print(f"Could not read {before}")
        sys.exit(1)
    else:

        pass
    if not os.path.exists(before):
        raise FileNotFoundError(f"{before} does not exist")
    else:
       try:
           #method open opens filename as f
           with open(before) as f:
               # Use the csv.reader to parse the file into rows
                reader = csv.reader(f)
               # Convert the reader object into a list of rows (each row is a list)
                rows = list(reader)
           # Separate header and data
           header = rows[0]
           data = rows[1:]
           transformed = []
           for row in data:
               name = row[0]
               house = row[1]
               last, first = name.split(", ")
               transformed.append([first, last, house])
           with open(after, "w", newline="") as f:
               writer = csv.writer(f)
               writer.writerow(["first", "last", "house"])  # new header
               writer.writerows(transformed)


       except Exception as e:
           print("Cannot read file {e}")
if __name__ == "__main__":
    main()
