#Filename: Extensions.py
#Student: Noel Prude
def main():
    fileName = processFileName("Please, enter a file name: ")
def processFileName(prompt):
    images = (".jpg" ,".jpeg")
    fileName = input(prompt)
    if fileName.casefold().strip().endswith(".gif"): 
        print("image/png")
    elif fileName.casefold().strip().endswith(images): 
        print("image/jpeg")
    elif fileName.casefold().strip().endswith(images): 
        print("image/jpeg")  
    elif fileName.casefold().strip().endswith(".png"): 
        print("image/png")
    elif fileName.casefold().strip().endswith(".pdf"): 
        print("application/pdf")
    elif fileName.casefold().strip().endswith(".txt"): 
        print("text/plain")
    elif fileName.casefold().strip().endswith(".zip"): 
        print("application/zip")
    else:
        print("application/octet-stream")

main()