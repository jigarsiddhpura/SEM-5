a = int(input("Enter the number : "))
print('square root of ', a, a**0.5)
l, b = float(input("Enter the length : ")), float(input("Enter the breadth : "))
print("Area : ", l*b, " ,", "Perimeter : ", 2 * (l + b))
a,b = int(input("Enter 1st numbers : ")), int(input("Enter 2nd numbers : "))
c = a
a = b
b = c
print("Swapping with third variable : ",a,b)
a,b = int(input("Enter 1st numbers : ")), int(input("Enter 2nd numbers : "))
b,a = a,b
print("swapping without third variable : ", a,b)
# another way 
a,b = int(input("Enter 1st numbers : ")), int(input("Enter 2nd numbers : "))
print("a :",a," b :",b)
a = a+b 
b = a-b
a = a-b
print("After Swapping ")
print("a:",a,"b:",b)
# adding elements to list , set , tuples 
n = int(input("Enter the size of list : "))
l = list()
for i in range(n):
    l.append(int(input(f"Enter the {i} element : ")))
print("list :",l)
n = int(input("Enter the size of list : "))
s = set()
for i in range(n):
    s.add(int(input(f"Enter the {i} element : ")))
print("set :", s)
n = int(input("Enter size "))
t = tuple()
l = list(t)
for i in range(n):
    l.append(int(input(f"Enter the {i} element : ")))
t = tuple(l)
print("tuple :", t)