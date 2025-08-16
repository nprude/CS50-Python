import emoji

def main():
    ui = input()
    # Use language='alias' for compatibility with emoji 2.x.x (which check50 likely uses)
    convertedui = emoji.emojize(ui, language='alias')
    print(convertedui)

if __name__ == "__main__":
    main()