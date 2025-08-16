def main():
    expression = calculateExpression("Please, enter an math expression: ")
def calculateExpression(prompt):
    expression = input(prompt)
    #expression = expression.split(' ') 
    a, b, c = expression.split(' ')
    newexpression = f"{a} {b} {c}"
    #a = float(a)
    #c = float(c)
    answer = eval(newexpression)
    print(float(answer))

main()