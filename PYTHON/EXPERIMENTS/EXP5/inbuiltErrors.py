import math

def catchArithmeticError():
    try:
        value = int("abc")  # Attempting to convert a non-numeric string to an integer
    except ArithmeticError as e:
        print(f"Arithmetic Error: {e}")


def catchKeyboardInterrupt():
    try:
        a = input("Enter input\n")
    except KeyboardInterrupt as e:
        print(f"KeyboardInterrupt Error ")
    else:
        print("success")

def catchKLookupError():
    try:
        a = [1,2,3]
        print(a[10])
    except LookupError:
        print(f"Index out of bound error.")
    else:
        print("success")

def catchOverflowError():
    try:    
        math.exp(1000)

    except OverflowError:
        print(f"OverflowError error aa rha bhai ")
    else:
        print("success")

def catchKeyError():
    print("\nKey Error implemenation")
    try:
        dic = {'1':'params','2':'query'}
        print(dic['3'])
    except KeyError as ke:
        print('Key error exception : ',ke)
 
def catchImportError():
    print("\nimport error implemenation")   
    try:
        import nonexistent_module
    except ImportError:
        print("Import error: The module does not exist or cannot be imported.")
    
def catchZeroDivError():
    print("\nzero Division Error implemenation")   
    try:
        print(9/0)
    except ZeroDivisionError as e:
        print(e)


    

# create a custom exception

catchArithmeticError()
catchZeroDivError()
catchKeyboardInterrupt()
catchKLookupError()
catchOverflowError()
catchKeyError()
catchImportError()

