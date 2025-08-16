def main():
    a = input("Greetings: ")
    b = value(a)
    print (f"${b}")
def value(a):
    #greetings = input(prompt)
    greetings = a

    if not greetings.casefold().lstrip().startswith("hello") and greetings.casefold().strip().startswith('h'):
    #print("$20")
        return int(20)
        
    elif greetings.casefold().strip().startswith("hello"):
        return int(0)
    #print("$0")
    else:
        return int(100)
    #print('$100')
if __name__ == "__main__":
    main()