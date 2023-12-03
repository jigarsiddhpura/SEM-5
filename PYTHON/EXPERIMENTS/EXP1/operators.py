a = 18
b = 3
print("\nArithmetic Operators :")
print(f'Addition of {a} and {b} is ',a+b)
print(f'subtraction of {a} and {b} is ',a-b)
print(f'Modulo of {a} and {b} is ',a%b)
print(f'Multiplication of {a} and {b} is ',a*b)
print(f'Division of {a} and {b} is ',a/b)
print(f'Remainder of {a} by {b} is ',a//b)
print(f'{a} raise to {b} is ',a**b)

c = 14
print("\nAssignment Operators :")
print("Inital value of c :")
print(c)
c+=6
print("Adding 6 to it gives ",c)
c-=6
print("subtracting 6 to it gives ",c)
c*=6
print("multiplying 6 to it gives ",c)
c/=6
print("divding by 6 to it gives ",c)
c%=6
print("taking modulo gives ",c)
c//=6
print("c raised to 6 gives ",c)
c**=6

d = 15
e = 10
print('\nComparison Operators :')
print(f"is {d} equal to {e}",d==e)
print(f"is {d} not equal to {e}",d!=e)
print(f"is {d} greater than or equal to {e}",d>=e)
print(f"is {d} smaller than or equal to {e}",d<=e)
print(f"is {d} greater than {e}",d>e)
print(f"is {d} smaller than {e}",d<e)

f = 10
g = 19
print('\nLogical Operators :')
print(f"if {f}>=10 and {g} <20 then : ", f>=10 and g<20)
print(f"if {f}>=10 or {g} >20 then : ", f>=10 or g>20)

h = 9
i = 19
print('\nidentity Operators :')
print(f"h is i ", h is i)
print(f"h is not i ", h is not i)

x = 'java'
y = 'javascript'
print("\nMembership Operators : ")
print(f'is {x} in {y} : ',x in y)
print(f'is {x} not in {y} : ',x not in y)

a = 5
b = 7
print("\nBitwise Operators : ")
print(f"{a} and {b} is : ",a&b)
print(f"{a} or {b} is : ",a|b)
print(f"{a} ^ {b} is : ",a^b)
print(f"{a} << 3 is : ",a<<3)
print(f"{b} >> 3 is : ",b>>3)
print(f"~ {a} is : ",~a)
print(f"~ {b} is : ",~b)
print(f"{a} >> 2 is : ",b>>2)