#In a file called lines.py, implement a program that expects
# exactly one command-line argument, the name (or path) of a Python file,
# and outputs the number of lines of code in that file, excluding comments and blank lines.
# If the user does not specify exactly one command-line argument, or if the
# specified file’s name does not end in .py, or if the specified file does not exist,
# the program should instead exit via sys.exit.
# Assume that any line that starts with #, optionally preceded by whitespace,
# is a comment. (A docstring should not be considered a comment.) Assume that any
# line that only contains whitespace is blank.
import os
import sys
def main():
    count = 0
    filename = ""
    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit(1)
    else:
       pass
    if not os.path.exists(filename):
        sys.exit(0)
    try:

        with open(filename, "r") as f:
                for line in f:
                    stripped = line.strip()
                    if stripped.startswith("#") or stripped == "":
                        continue
                    count +=1

        print (f"Total Lines: {count}")


    except FileNotFoundError:
        sys.exit(0)



if __name__ == "__main__":
    main()