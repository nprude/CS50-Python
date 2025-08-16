def main():
    months = ["January", "February","March", "April", "May", "June","July", "August", "September", "October","November","December"]
    
    while True:
        user_date = input("Date: ").strip()
        try:
            if "/" in user_date:
                m, d, y = map(int, user_date.split('/'))
                if not(1 <= m <=12 and 1 <= d <=31 and y >=0):
                    raise ValueError
                month = str(m).zfill(2)
                day = str(d).zfill(2)
                year = str(y)
                print(f"{year}-{month}-{day}")
                break
            elif "," in user_date:
                parts = user_date.replace(',','').split()
                if len(parts) !=3:
                    raise ValueError
                month_name, day_str, year_str = parts
                if month_name not in months:
                    raise ValueError
                m = months.index(month_name) + 1
                d = int(day_str)
                y = int(year_str)
                if not (1 <= m <= 12 and 1 <= d <= 31 and y >= 0):
                    raise ValueError

                month = str(m).zfill(2)
                day = str(d).zfill(2)
                year = str(y)
                print(f"{year}-{month}-{day}")
                break

            else:
                raise ValueError

        except (ValueError, IndexError):
            pass  # Prompt again if input is invalid

if __name__ == "__main__":
    main()


