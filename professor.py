from random import randint
import sys

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    elif level == 3:
        return randint(100, 999)
    else:
        raise ValueError("Invalid level")

def main():
    score = 0
    problems = 10
    level = get_level()

    for _ in range(problems):
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y
        attempts = 0

        while attempts < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1

        if attempts == 3:
            print(f"{x} + {y} = {correct}")

    print(f"Score: {score}")

if __name__ == "__main__":
    main()

