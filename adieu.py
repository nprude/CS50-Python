import sys
def main():
    names=[]
    while True:
        try:
            userinput = input("Name: ")
            names.append(userinput)

        except (EOFError, KeyboardInterrupt):
           
            break

    if len(names) == 1:
        formatted = f"Adieu, adieu, to {names[-1]}"
        print(formatted) 
    elif len(names) == 2:
        formatted = f"Adieu, adieu, to {names[0]} and {names[1]}"
        print(formatted)
    else:
        formatted = ", ".join(names[:-1]) + f", and {names[-1]}"
        sentence = f"Adieu, adieu, to {formatted}"
        print(sentence)
    
     
if __name__ == "__main__":
  main()





