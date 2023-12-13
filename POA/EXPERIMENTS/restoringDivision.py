def binary_addition(a,b):
    """a,b are binary strings"""
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    # Initialize the result
    result = ''
    
    # Initialize the carry
    carry = 0
    
    # Traverse the string
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
    
        # Compute the carry.
        carry = 0 if r < 2 else 1
    
    if carry != 0:
        result = '1' + result
    
    # result = result.zfill(max_len)

    return result[-max_len:]

def complement(b):
    # 2's complement of binary number
    b_comp = ""
    for i in b:
        if i=="1": b_comp += "0"
        elif i=="0": b_comp += "1"
    b_comp = binary_addition(b_comp,"1")
    return b_comp

def binary_subtraction(a,b):
    """a,b are binary strings"""
    b_complement = complement(b)
    max_len = len(a)
    return binary_addition(a,b_complement.zfill(max_len))

def ALS(a,q):
    """all are binary strings"""
    # x = Q not
    a = a[1:]+q[0]
    q = q[1:]+"_"
    return a,q

def isNegative(bin_number):
    return bin_number[0] == "1"


def restoring_division(dividend,divisor,count,A="00000"):
    binary_dividend  = bin(dividend)[2:].zfill(count) if dividend>0 else bin(dividend)[3:].zfill(count)
    binary_divisor = bin(divisor)[2:].zfill(count+1) if divisor>0 else bin(dividend)[3:].zfill(count+1)
    print(f"Dividend Q = {binary_dividend}, divisor B = {binary_divisor}, A = {A}, count = {count}\n")
    print("Count\tA\tQ\tOperation")
    print("----------------------------------------")

    while(count!=0):
        print(f"{count}\t{A}\t{binary_dividend}\tbefore ALS")
        A,binary_dividend = ALS(A,binary_dividend)
        print(f"{count}\t{A}\t{binary_dividend}\tA <- A-B")
        A = binary_subtraction(A,binary_divisor)
        case = isNegative(A)
        # print(f"A,Q <- {case}")
        if(case):
            binary_dividend = binary_dividend.replace("_","0")
            A = binary_addition(A,binary_divisor)
            print(f"{count}\t{A}\t{binary_dividend}\tQ. = 0 & A<-A+B")
        else:
            # A = binary_subtraction(A,binary_divisor)
            binary_dividend = binary_dividend.replace("_","1")
            print(f"{count}\t{A}\t{binary_dividend}\tQ. = 1")
        print(f"{count}\t{A}\t{binary_dividend}")
        count -= 1
        print("----------------------------------------")

    remainder = int(A,base=2)
    quotient = int(binary_dividend,base=2)
    
    print(f"Remainder = {remainder}, Quotient = {quotient}")

restoring_division(int(input("Enter Dividend = ")),int(input("Enter Divisor = ")),4)