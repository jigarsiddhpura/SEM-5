n = int(input("Enter the number of rows : " ))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()
    
# factorial 
print("\nFactorial example : ")
n = int(input("Enter the number for factorial : "))
fact = 1
if n<0 : print("factorial does not exist !!")
elif n==0: print("Factorial of 0 is 1 ")
else :
    for i in range(1,n+1):
        fact *= i
print(f"Factorial of {n} with for loop : {fact}")
n = int(input("Enter the number for factorial : "))
fact = 1
i=1
if n<0 : print("factorial does not exist !!")
elif n==0: print("Factorial of 0 is 1 ")
else :
    while i <=n:
        fact *=i
        i+=1
print(f"Factorial of {n} with while loop : {fact}")

#Even odd with if else
print("\nEven odd with if else example : ")
n = int (input("Enter a number :"))
if (n%2)==0: print(f"{n} is even")
else: print(f"{n} is odd")

# checking the number
print("\nchecking the number with if elif else example : ")
number = 2+9j
if isinstance(number, int):
    print("Number is an integer.")
elif isinstance(number, list):
    print("Number is a list.")
elif isinstance(number, tuple):
    print("Number is a tuple.")
elif isinstance(number, set):
    print("Number is a set.")
elif isinstance(number, float):
    print("Number is a float data type.")
elif isinstance(number, str):
    print("Number is a string.")
else:
    print("Number is complex.")

# break continue pass
print("\nbreak continue pass example : ")
for letter in 'python':
    if letter == 't' or letter == '0':
        continue
    print('current letter:',letter)
for letter in 'python':
    if letter == 'y':
        break
    print('current letter:',letter)
for letter in 'python':
    if letter in ['p', 'y', 't', 'h']:
        print('hi')
        pass
print('pass letter:',letter)