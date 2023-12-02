bNo = 6
pNo = 4
bSizes = [200,400,600,500,300,250]
pSizes = [357,210,468,491]
flag = [0] * len(bSizes)
allocated = [0] * len(bSizes)

print(f"Memory Blocks : {bSizes}")
print(f"Processes : {pSizes}\n")

for i,psize in enumerate(pSizes):   
    for j,bsize in enumerate(bSizes):
        if((psize <= bsize) & (flag[j] == 0)):
            flag[j] = 1
            allocated[j] = psize
            print(f"Memory allocation for {psize} - {allocated}")
            break
        elif(j == len(bSizes)-1):
            print(f"Memory allocation for {psize} - No Space to allocate")

print(f"\nFinal Memory Allocation - {allocated}")

