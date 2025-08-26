import os, sys
from PIL import Image, ImageOps
'''
In a file called shirt.py, implement a program that expects exactly two command-line arguments:
in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program should then overlay shirt.png (which has a transparent background) on the input after 
resizing and cropping the input to be the same size, saving the result as its output.
Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, 
resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, 
using default values for method, bleed, and centering, overlay the shirt with Image.paste, 
per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the 
result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.
The program should instead exit via sys.exit:
if the user does not specify exactly two command-line arguments,
if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
if the input’s name does not have the same extension as the output’s name, or
if the specified input does not exist.
Assume that the input will be a photo of someone posing in just the right way, like these demos, so that, 
when they’re resized and cropped, the shirt appears to fit perfectly.
'''
def main():
    input = ""
    shirt = "shirt.png"
    output = ""
    valid_ext = ("jpg", "jpeg", "png")
    if len(sys.argv) != 3:

        if len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit(1)
        elif len(sys.argv) < 2:
            print("Too few command-line arguments")
            sys.exit(1)
    else:

        input = sys.argv[1]
        output = sys.argv[2]
        

    if not input.lower().endswith(valid_ext) or not output.lower().endswith(valid_ext):
        
        print(f"Could not read {input}")
        sys.exit(1)
    else:
        pass
    if os.path.splitext(input)[1].lower() != os.path.splitext(output)[1].lower():
        print("Input and output must have the same file extension")
        sys.exit(1)
    else:
        pass

    if not os.path.exists(input):
        raise FileNotFoundError(f"{input} does not exist")
    else:
       try:
           imgI = Image.open(input)
           imgII = Image.open(shirt)

           adjusted = ImageOps.fit(imgI, imgII.size)
           adjusted.paste(imgII,(0,0), imgII)

           adjusted.save(output)
           

       except Exception as e:
           print(f"{e}")
if __name__ == "__main__":
    main()
