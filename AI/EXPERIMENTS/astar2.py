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

# open = [node,fn,path from start to node]

def calcfn(node,path):
    fn = 0
    for i,curr_node in enumerate(path):
        if i != (len(path)-1):
            fn += graph[curr_node][path[i+1]]
        else:
            fn += graph_heu[node]
    print(f"fn = {fn}, node = {node}, path = {path}")

    return fn


def astar(current,goal,open,close):
    path = open[0][2]
    open = []
    cost = 0

    while(1):
        print(f"\ncurrent node = {current}\n")
        close.append(current)
        open = open[1:]
        if current==goal: break

        for node,gn in graph[current].items():
            fn = calcfn(node,path)+gn
            open.append([node,fn,path+[node]])

        open = sorted(open, key=lambda x:x[1])
        cost = open[0][1]
        current = open[0][0]
        print(f"open list =  {open}")
        print(f"close list =  {close}")

        path = open[0][2]

    print(f"\npath is {path} with cost = {cost}")


open = [['S',graph_heu[start],['S']]]
astar(start,goal,open,[])