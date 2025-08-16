
def is_valid(x):
    a = x
    if a.isalnum():
        
        if len(a) == 2:
            if a[:2].isalpha():
                return True
            else:
                return False
        elif len(a) == 3:
            if a[:2].isalpha():
                if a[2].isnumeric() and a[2] != "0" or a[2].isalpha() :
                    return True
                else:
                    return False
            else:
                return False
        elif len(a) == 4:
            if a[:2].isalpha():
                if a[2].isalpha() and a[3].isalpha():
                    return True
                elif a[2].isalpha() and a[3].isnumeric() and a[3] != "0":
                    return True
                elif a[2].isnumeric() and a[3].isnumeric() and a[2] != "0":
                    return True
                else:
                    return False
            else:
                return False
        elif len(a) == 5:
            if a[:2].isalpha():
                if all(char.isalpha() for char in a[2:]):
                    return True
                elif all(char.isnumeric() for char in a[2:]):
                    return True
                elif a[2].isalpha() and a[3].isalpha() and a[4].isnumeric() and a[4] != "0":
                    return True
                elif a[2].isalpha() and a[3].isnumeric() and a[4].isnumeric() and a[3] != "0":
                    return True
                elif a[2].isnumeric() and a[3].isnumeric() and a[4].isnumeric() and a[2] != "0":
                    return True
                else:
                    return False
            else:
                return False
        elif len(a) == 6:
            
            if a[:2].isalpha():
                if all(char.isalpha() for char in a[2:]):
                    return True
                elif a[2].isalpha() and a[3].isalpha() and a[4].isalpha() and a[5].isnumeric() and a[5] != "0":
                    return True
                elif a[2].isalpha() and a[3].isalpha() and a[4].isnumeric() and a[5].isnumeric() and a[4] != "0":
                    return True
                elif a[2].isalpha() and a[3].isnumeric() and a[4].isnumeric() and a[5].isnumeric() and a[3] != "0":
                    return True
                elif a[2].isnumeric() and a[3].isnumeric() and a[4].isnumeric() and a[5].isnumeric() and a[2] != "0":
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
