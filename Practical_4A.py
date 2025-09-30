import heapq

# Define the map using lowercase city names
Romania_Map = {
    'arad': [('zerind', 75), ('sibiu', 140), ('timisoara', 118)],
    'zerind': [('arad', 75), ('oradea', 71)],
    'oradea': [('zerind', 71), ('sibiu', 151)],
    'sibiu': [('arad', 140), ('oradea', 151), ('fagaras', 99), ('rimnicu vilcea', 80)],
    'timisoara': [('arad', 118), ('lugoj', 111)],
    'lugoj': [('timisoara', 111), ('mehadia', 70)],
    'mehadia': [('lugoj', 70), ('drobeta', 75)],
    'drobeta': [('mehadia', 75), ('craiova', 120)],
    'craiova': [('drobeta', 120), ('rimnicu vilcea', 146), ('pitesti', 138)],
    'rimnicu vilcea': [('sibiu', 80), ('pitesti', 97), ('craiova', 146)],
    'fagaras': [('sibiu', 99), ('bucharest', 211)],
    'pitesti': [('rimnicu vilcea', 97), ('craiova', 138), ('bucharest', 101)],
    'bucharest': [('fagaras', 211), ('pitesti', 101), ('giurgiu', 90), ('urziceni', 85)],
    'giurgiu': [('bucharest', 90)],
    'urziceni': [('bucharest', 85), ('hirsova', 98), ('vaslui', 142)],
    'hirsova': [('urziceni', 98), ('eforie', 86)],
    'vaslui': [('urziceni', 142), ('iasi', 92)],
    'iasi': [('vaslui', 92), ('neamt', 87)],
    'neamt': [('iasi', 87)],
    'eforie': [('hirsova', 86)]
}

# Heuristic values (all lowercase)fff
h = {
    'arad': 366, 'zerind': 374, 'oradea': 380, 'sibiu': 253,
    'timisoara': 329, 'lugoj': 244, 'mehadia': 241, 'drobeta': 242,
    'craiova': 160, 'rimnicu vilcea': 193, 'fagaras': 178,
    'pitesti': 98, 'bucharest': 0, 'giurgiu': 77, 'urziceni': 80,
    'hirsova': 151, 'eforie': 162, 'vaslui': 199, 'iasi': 226,
    'neamt': 234
}

def a_star(start, goal):
    frontier = [(h[start], 0, start, [start])]
    visited = set()

    while frontier:
        f, g, current, path = heapq.heappop(frontier)
        if current == goal:
            return path, g
        if current in visited:
            continue
        visited.add(current)
        for neighbor, cost in Romania_Map.get(current, []):
            if neighbor not in visited:
                heapq.heappush(frontier, (g + cost + h[neighbor], g + cost, neighbor, path + [neighbor]))
    return None, float('inf')

# === User input section ===
start_city = input("Enter the START city: ").strip().lower()
goal_city = input("Enter the GOAL city: ").strip().lower()

if start_city not in Romania_Map or goal_city not in Romania_Map:
    print("Invalid city name(s). Please try again.")
else:
    path, total_cost = a_star(start_city, goal_city)

    if path:
        print(f"\nStep-by-step path from {start_city.title()} to {goal_city.title()}:")
        for i, city in enumerate(path):
            print(f"Step {i + 1}: {city.title()}")
        print(f"\nTotal cost: {total_cost}")
    else:
        print("No path found.")
