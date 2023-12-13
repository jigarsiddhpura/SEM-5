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

def ARS(a,q):
    """all are binary strings"""
    q1 = q[-1]
    q = a[-1]+q[:-1]
    a = a[0]+a[:-1]
    return a,q,q1

def isNegative(bin_number):
    return bin_number[0] == "1"


def booth(multiplier,multiplicant,count,A="0000",Q1="0"):
    binary_multiplier  = bin(multiplier)[2:].zfill(count) if multiplier>0 else bin(multiplier)[3:].zfill(count)
    binary_multiplicant = bin(multiplicant)[2:].zfill(count) if multiplicant>0 else bin(multiplier)[3:].zfill(count)
    print(f"Multiplier Q = {binary_multiplier}, Multiplicant M = {binary_multiplicant}, A = {A}, count = {count}, Q1 = 0\n")
    print("Count\tA\tQ\tQ1")
    print("----------------------------------------")

    while(count!=0):
        print(f"{count}\t{A}\t{binary_multiplier}\t{Q1}")
        case = binary_multiplier[-1]+Q1
        print(f"A,Q <- {case}")
        if(case=="01"):
            A = binary_addition(A,binary_multiplicant)
            print(f"{count}\t{A}\t{binary_multiplier}\t{Q1}\tbefore ARS")
        elif(case=="10"):
            A = binary_subtraction(A,binary_multiplicant)
            print(f"{count}\t{A}\t{binary_multiplier}\t{Q1}\tbefore ARS")
        elif(case=="00" or case=="11"):
            pass
        A,binary_multiplier,Q1 = ARS(A,binary_multiplier)
        print(f"{count}\t{A}\t{binary_multiplier}\t{Q1}")
        count -= 1
        print("----------------------------------------")

    bin_ans = A+binary_multiplier
    ans = int(complement(bin_ans),base=2) if isNegative(bin_ans) else int(bin_ans,base=2)
    print(f"Answer = {ans}")


booth(int(input("Enter Multiplier = ")),int(input("Enter Multiplicant = ")),4)