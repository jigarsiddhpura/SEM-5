class BaseError(Exception):pass
class HighValueError(Exception):pass
class LowValueError(Exception):pass
value = 81
while(1):
    try:
        n=int(input("Enter number:"))
        if n>value:
            raise HighValueError
        elif n < value:
            raise LowValueError
        else:
            print("Nice!Correct answer")
            break
    except LowValueError:
        print("Very Low Value, Give input again")
        print()
    except HighValueError:
        print("Very High value , give input again")
        print()