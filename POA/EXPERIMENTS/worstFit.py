bNo = 6
pNo = 4
bSizes = [200,400,600,500,300,250]
pSizes = [357,210,468,491]
flag = [0] * len(bSizes)
allocated = [0] * len(bSizes)
MIN_BLOCK_SIZE = -10

print(f"Memory Blocks : {bSizes}")
print(f"Processes : {pSizes}\n")

def getMaxMemoryIndex(psize,memory, flag):
    """
    Returns memory index with max capacity given that it is unallocated.

    Parameters:
    - psize (int): integer representing the process size 
    - memory (list): List representing memory capacities.
    - flag (list): List representing the allocation status (0 for unallocated, 1 for allocated).

    Returns:
    - int: Index of the unallocated memory with the maximum capacity but less than process size.
    """
    max_capacity = -1
    max_index = None
    for i in range(len(memory)):
        if flag[i] == 0 and memory[i] >= psize and memory[i]>max_capacity:
            max_capacity = memory[i]
            max_index = i

    return max_index


for i,psize in enumerate(pSizes):
    index_placed = -1
    allocated_index = getMaxMemoryIndex(psize,bSizes,flag)
    if allocated_index:
        flag[allocated_index] = 1
        allocated[allocated_index] = psize
        print(f"Memory allocation for {psize} - {allocated}")
    else:
        print(f"Memory allocation for {psize} - No Space to allocate")
    
print(f"\nFinal Memory Allocation - {allocated}")

