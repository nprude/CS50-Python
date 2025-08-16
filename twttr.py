import re

def main():
    a = input("Input: ")
    result = shorten(a)
    print(result)

def shorten(a):
    b = a
    vowels = "aeiouAEIOU"
    b = re.sub(r"[AEIOUaeiou]","",b)
    return b
if __name__ == "__main__":
    main()