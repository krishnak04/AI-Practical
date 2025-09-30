import heapq

Alphabet_map = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('J', 3)],
}

h = {
    'A': 10, 'B': 8, 'C': 5, 'D': 7, 'E': 3,
    'F': 6, 'G': 5, 'H': 3, 'I': 1, 'J': 0
}

def alpha_star(start, goal):
    frontier = [(h[start], 0, start, [start])]  # (f = g + h, g, current_node, path)
    visited = set()

    while frontier:
        f, g, current, path = heapq.heappop(frontier)

        if current == goal:
            return path, g

        if current in visited:
            continue

        visited.add(current)

        for neighbor, cost in Alphabet_map.get(current, []):
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + h[neighbor]
                heapq.heappush(frontier, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')

start = input("Enter the START city: ").strip().upper()
goal = input("Enter the GOAL city: ").strip().upper()

valid_nodes = set(Alphabet_map.keys()) | set(h.keys())
if start not in valid_nodes or goal not in valid_nodes:
    print("Invalid city name. Please enter valid cities from the map.")
else:
    path, cost = alpha_star(start, goal)
    if path:
        print("\nPath:", " -> ".join(path))
        print("Total cost:", cost)
    else:
        print(f"No path found from {start} to {goal}.")