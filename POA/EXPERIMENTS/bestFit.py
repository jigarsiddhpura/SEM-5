bNo = 6
pNo = 4
bSizes = [200,400,600,500,300,250]
pSizes = [357,210,468,491]
flag = [0] * len(bSizes)
allocated = [0] * len(bSizes)
MAX_BLOCK_SIZE = 999999

print(f"Memory Blocks : {bSizes}")
print(f"Processes : {pSizes}\n")

for i,psize in enumerate(pSizes):
    index_placed = -1
    for j,bsize in enumerate(bSizes):
        if((psize <= bsize) & (bsize < MAX_BLOCK_SIZE) & (flag[j] == 0)):
            index_placed = j
            MAX_BLOCK_SIZE = bsize
    if index_placed != -1:
        flag[index_placed] = 1
        allocated[index_placed] = psize
        print(f"Memory allocation for {psize} - {allocated}")
    else:
        print(f"Memory allocation for {psize} - No Space to allocate")
    MAX_BLOCK_SIZE = 999999

print(f"\nFinal Memory Allocation - {allocated}")

