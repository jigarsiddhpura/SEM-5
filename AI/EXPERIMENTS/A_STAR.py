# Define the graph
graph = {
    'S': {'A': 5, 'B': 8, 'C': 12},
    'A': {'D': 6, 'E': 9},
    'B': {'F': 10},
    'C': {'G': 11},
    'D': {'H': 8, 'I': 15},
    'E': {'J': 7},
    'F': {'K': 12},
    'G': {'L': 9},
    'H': {'M': 10},
    'I': {'N': 5},
    'J': {'N': 8},
    'K': {'N': 6},
    'L': {'N': 10},
    'M': {'N': 7},
    'N': {'Z': 0},
    'Z': {}
}

# Define the heuristic values for A* search
graph_heu = {
    'S': 20,
    'A': 16,
    'B': 18,
    'C': 15,
    'D': 12,
    'E': 10,
    'F': 8,
    'G': 6,
    'H': 6,
    'I': 5,
    'J': 4,
    'K': 3,
    'L': 2,
    'M': 1,
    'N': 0,
    'Z': 0
}

start = 'S' 
goal = 'Z'
open = []
close = []
open.append([start,graph_heu[start],[start]])

def calcFn(path,node):
    """Calculate F(n) based on path and current node"""
    fn = 0
    for i in range(len(path)-1):
        fn += graph[path[i]][path[i+1]]
    fn += graph[path[-1]][node] + graph_heu[node]
    print(f"fn = {fn}, node = {node}, path = {path}")
    return fn

if __name__=="__main__":
    while(1):
        currentNode = open[0][0]
        print(f"Currently at node {currentNode}\n")
        current_path = open[0][2]
        close.append(currentNode)

        if(currentNode == goal): break

        # iterating through all childs
        for node,gn in graph[currentNode].items():
            fn = calcFn(current_path,node)
            open.append([node,fn,current_path+[node]])

            # sorting based on F(n)
            open = sorted(open, key=lambda x:x[1])
        
        # removing the visited node from open list
        open = [pair for pair in open if pair[0] != currentNode]
        print(f"Open List = {open}\nClose List = {close}\n")

print(f"Optimized path from {start} to {goal} is {open[0][1]}")
    





