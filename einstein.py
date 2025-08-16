# Student: Noel Prude

def main():
    m = input("Please enter the mass you wish to convert: ")
    castM = int(m)
    print(conversion(castM))
    
def conversion(x):
    E = x * pow(300000000 , 2)
    castE = int(E)
    return castE
main()