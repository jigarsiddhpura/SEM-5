import math
import time

# def catchArithmeticError():
#     try:
#         a = 10/0
#     except ArithmeticError as e:
#         print(f"{e} cannot divide by zero")
#     else:
#         print("success")

# def catchKeyboardInterrupt():
#     try:
#         a = input("Enter input\n")
#     except KeyboardInterrupt as e:
#         print(f"KeyboardInterrupt Error ")
#     else:
#         print("success")

# def catchKLookupError():
#     try:
#         a = [1,2,3]
#         print(a[10])
#     except LookupError:
#         print(f"Index out of bound error.")
#     else:
#         print("success")

# def catchOverflowError():
#     try:    
#         math.exp(1000)

#     except OverflowError:
#         print(f"OverflowError error aa rha bhai ")
#     else:
#         print("success")

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


def catchRangeError():
    print("\nout range error handling implemenation")
    try:
        l = []
        print(l[1])
    except Exception as e:
        print(e)
    
def catchKeyboardInterrupt():
    print('\nkeyboard interrupt ')
    try:
        print(input("Enter something : "))
        while True:
            print('print')
            time.sleep(1)
    except Exception as kbe:
        print(kbe)
# create a custom exception

# catchArithmeticError()
# catchKeyboardInterrupt()
# catchKLookupError()
# catchOverflowError()
catchKeyError()
catchImportError()
catchZeroDivError()
catchRangeError()
catchKeyboardInterrupt()

