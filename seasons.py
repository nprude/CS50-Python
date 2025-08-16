import inflect
from datetime import date
import sys

p = inflect.engine()

def calculate_minutes(birthdate: str, today: date) -> str:
    birth = date.fromisoformat(birthdate)
    delta = today - birth
    minutes = int(delta.total_seconds() / 60)
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"

def main():
    birthdate = input("Date of Birth: ").strip()
    try:
        print(calculate_minutes(birthdate, date.today()))
        sys.exit(0)  
    except ValueError:
        sys.exit(1)  

if __name__ == "__main__":
    main()

