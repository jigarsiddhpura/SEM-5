graph = {
  'A': ['B', 'C'],
  'B': ['A', 'D'],
  'C': ['A', 'D', 'E'],
  'D': ['B', 'C', 'F'],
  'E': ['C', 'F', 'G'],
  'F': ['D', 'E', 'H'],
  'G': ['E', 'H'],
  'H': ['F', 'G']
}

def bfs(graph, current_node, goal_node, visited, path, queue):
    visited.append(current_node)
    queue.append(current_node)
    not_visited = [i for i in graph.keys() if i not in visited]
    print(f"{visited}\t\t{not_visited}\t\tFalse")
    while queue:
        node = queue.pop(0)  # ⭐ 
        
        path.append(node)
        if node == goal_node:
            not_visited = [i for i in graph.keys() if i not in visited]
            print(f"{visited}\t\t{not_visited}\t\tTrue")
            print(f"path : {path}")
            break
        
        for neighbour_node in graph[node]:
            if neighbour_node not in visited:
                visited.append(neighbour_node)
                queue.append(neighbour_node)
                not_visited = [i for i in graph.keys() if i not in visited]
                print(f"{visited}\t\t{not_visited}\t\tFalse")
            
print("\n")
print(f"Nodes in Graph : {[i for i in graph.keys()]}")
start_node = input("Enter start node : ")
goal_node = input("Enter goal node : ")
visited = []
queue = []
path = []
print("<------------------------------Breadth-First Search------------------------------>")
print("Visited\t\tNot Visted\t\tGoal state")
print("<------------------------------------------------------------------------------>")
bfs(graph, start_node, goal_node,visited,path,queue)