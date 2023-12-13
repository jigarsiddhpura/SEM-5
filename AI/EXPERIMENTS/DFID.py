graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F', 'X'],
  'D': ['F', 'C'],
  'E': ['G', 'H'],
  'F': [],
  'X': [],
  'G': [],
  'H': [],
}


def dfid(graph, current_node, goal_node, visited, path, depth):
    for i in range(1,depth+1):
        print(f"Depth : {i}")
        path, status = dfs(graph, current_node, goal_node, [], [], 0, i)
        
    return path, status

def dfs(graph, current_node, goal_node, visited, path, curr_depth, depth):
    if curr_depth<=depth:
        if current_node not in visited:
            path.append(current_node)
            visited.append(current_node)
            not_visited = [i for i in graph.keys() if i not in visited]
            if current_node == goal_node:
                print(f"{visited}\t\t{not_visited}\t\tTrue")
                print(f"path : {path}")
                return path,True
            
            print(f"{visited}\t\t{not_visited}\t\tFalse")
            for i in graph[current_node]:
                path, status = dfs(graph, i, goal_node, visited, path, curr_depth+1, depth)
                if status:
                    return path, True
                
        return path,False
    else:
        return path,False

path1, status =  dfid(graph,'A','D',[],[],3)

if not status:
    print("No path found")
