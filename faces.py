from datetime import datetime

def main():
    help(str)
    birthdate = input("Date of Birth: ")  
    year, month, day = birthdate.split("-")
    int(year)
    int(month)
    int(day)
    birth = datetime(year, month, day, 0, 0)
    today = datetime(2025, 7, 19, 0, 0)

    # Calculate time difference
    delta = today - birth

    # Total minutes
    minutes_alive = delta.total_seconds() / 60

    print(f"You've been alive for {int(minutes_alive):,} minutes.")
if __name__ == "__main__":
    main()
