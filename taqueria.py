import sys
def main():
    
    total = 0.00
    menu = {"baja taco": 4.25,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.50,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00}
    while True:  # Continue prompting user until they press Ctrl + D
        try:
            a = input("Item: ").strip().lower()
            if a in menu:
                total += menu[a]
                print(f"\nTotal ${total:.2f}")
            
        except EOFError:# Exit when user enters Ctrl + D
            print("\nExiting program.")
            break # Gracefully exit instead of sys.exit() 

main()