def main():
    x = getReponse("What is the answer to the great Question of Life?  ")

def getReponse(prompt):
    x = input(prompt)
    if x == "42" or x.casefold() == "forty two":
        print("Yes")
    if x.casefold() =="forty-two":
        print("Yes")
    else:
        print("No")
main()