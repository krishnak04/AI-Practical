# Implement breadth first search algorithm. #

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6'],
    '4': [],
    '5': ['6'],
    '6': []
}

print("Graph:", graph)
start_node = input("Enter a Starting Node (e.g., 1–6):-- ")
if start_node in graph:
    bfs(graph, start_node)
else:
    print(f"Node {start_node} is not in the graph.")
