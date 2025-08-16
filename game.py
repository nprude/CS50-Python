#Test
import random
def check_input(prompt):
     while True:
        try:
            b = int(input(prompt))
            if b > 0: 
                return b
            else:
                pass
        except ValueError:
            pass
def play_game(a):
    randomint = random.randint(1,a)

    while True:
        b = check_input("Guess: ")
        if b < randomint:
            print(randomint)
            print("Too small!")

        elif b > randomint:
            print(randomint)
            print("Too large!")

        else:
            print("Just right!")
            break
    
def main():
    a = 0
    b = 0
    a = check_input("Level: ")
    play_game(a)
        

if __name__ == "__main__": 
    main()
    
