# Implement depth first search algorithm.  #

from collections import deque

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)


graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6'],
    '4': [],
    '5': ['6'],
    '6': []
}

print("Graph:", graph)
start_node = input("Enter a Starting Node (e.g., 1-6):-- ")
if start_node in graph:
    dfs(graph, start_node)
else:
    print(f"Node {start_node} is not in the graph.")
