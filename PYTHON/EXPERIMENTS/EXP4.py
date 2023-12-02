import math

def catchArithmeticError():
    try:
        a = 10/0
    except ArithmeticError as e:
        print(f"{e} cannot divide by zero")
    else:
        print("success")

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

# create a custom exception


# catchArithmeticError()
# catchKeyboardInterrupt()
# catchKLookupError()
# catchKAttributeError()
# catchOverflowError()

