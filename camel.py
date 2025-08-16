import re
def main():
    a = convertCamelCase("camelCase: ")

def convertCamelCase(prompt):
    a = input(prompt)
    #the caret (^) is a special metacharacter
    #When placed after a character or group, it means "match zero or one occurrence" of that item.
    b = re.sub(r'(?<!^)(?=[A-Z])', '_', a).lower()
    print ("snake_case: " + b)
main()