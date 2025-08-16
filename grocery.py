import sys
def main():
    a = {}
    counter = 0
    try:
        while True:
            counter += 1
            item =  input("").upper()
            if item in a:
                a[item] += 1
            else:
                a[item] = 1

    except EOFError:

        for item, count in sorted(a.items()):
            print(f"{count} {item}")
main()