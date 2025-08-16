from fuel import gauge, convert

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            continue
if __name__ == '__main__':
    main()


if __name__ == "__main__":
    main()