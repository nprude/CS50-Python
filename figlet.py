import sys
import random
import pyfiglet

def main():
    fonts = pyfiglet.FigletFont.getFonts()

    
    if len(sys.argv) == 1:
        font_choice = random.choice(fonts)

    elif len(sys.argv) == 3:
        flag, font_name = sys.argv[1], sys.argv[2]
        if flag not in ['-f', '--font'] or font_name not in fonts:
            sys.exit("Invalid usage")
        font_choice = font_name

   
    else:
        sys.exit("Invalid usage")

   
    user_input = input("Input: ")
    figlet = pyfiglet.Figlet(font=font_choice)
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()
