def histogram(input_list :list) -> list[int]:
    sorted_list = list(set(input_list))
    hist = []
    
    for i in sorted_list:
        hist.append((i,input_list.count(i)))
        
    histogram = sorted(hist,key=lambda x:x[1])
    return histogram

# h = histogram([13,7,12,7,11,13,14,13,7,11,13,14,12,14,14,7])
# print(h)

def hanoi(disks, source, aux, target):
    if disks==1:
        print(f"Move 1 disk from peg{source} to peg{target}")
        return
    hanoi(disks-1,source,target,aux)
    print(f"Move disk {disks} from peg{source} to peg{target}")
    hanoi(disks-1,aux,source,target)

# disk_count = int(input("Enter num of disks : "))
# hanoi(disk_count,'A','B','C')

def perfect_number(num):
    """Checks if a number is perfect or not."""
    sum = 0
    for i in range(1,num//2+1):
        if num % i == 0: sum+= i

    return True if sum==num else False

n = int(input("\nEnter a num : "))
isPerfect = perfect_number(n)
print(f"{n} is a perfect number\n") if isPerfect else print(f"{n} is a not a perfect number\n")

# code to print greatest of two number using lamda

# a = int(input("Enter 1st number : "))
# b = int(input("Enter 2nd number : "))

# maximum = lambda a,b : a if a>b else b
# print(f"Maximum btw {a},{b} is {maximum(a,b)}")



