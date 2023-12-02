graph = {
  'A': ['B', 'C'],
  'B': ['A', 'D'],
  'C': ['A', 'D', 'E'],
  'D': ['F', 'C', 'B'],
  'E': ['C', 'F', 'G'],
  'F': ['D', 'E', 'H'],
  'G': ['E', 'H'],
  'H': ['F', 'G']
}

def dfs(graph, current_node, goal_node, visited, path):
    if current_node not in visited:
        path.append(current_node)
        visited.append(current_node)
        not_visited = [i for i in graph.keys() if i not in visited]
        if current_node == goal_node:
            print(f"{visited}\t\t{not_visited}\t\tTrue")
            print(f"path : {path}")
            exit()
        
        print(f"{visited}\t\t{not_visited}\t\tFalse")
        for i in graph[current_node]:
            dfs(graph, i, goal_node, visited, path)

print("\n")
print(f"Nodes in Graph : {[i for i in graph.keys()]}")
start_node = input("Enter start node : ")
goal_node = input("Enter goal node : ")
visited = []
path = []
print("<------------------------------Depth-First Search------------------------------>")
print("Visited\t\tNot Visted\t\tGoal state")
print("<------------------------------------------------------------------------------>")
dfs(graph, start_node, goal_node,visited,path)