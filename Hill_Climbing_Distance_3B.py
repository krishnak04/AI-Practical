import math

point1 = [1, 5]
point2 = [6, 4]
point3 = [5, 2]
point4 = [2, 3]

increment = 0.1
starting_point = [1, 1]

def distance(x1, y1, x2, y2):
    return math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)

def sum_of_distances(x, y, p1, p2, p3, p4):
    d1 = distance(x, y, p1[0], p1[1])
    d2 = distance(x, y, p2[0], p2[1])
    d3 = distance(x, y, p3[0], p3[1])
    d4 = distance(x, y, p4[0], p4[1])
    return d1 + d2 + d3 + d4

def new_distance(x, y, p1, p2, p3, p4):
    total = sum_of_distances(x, y, p1, p2, p3, p4)
    return [x, y, total]

def best_next_point(min_val, d1, d2, d3, d4):
    if d1[2] == min_val:
        return [d1[0], d1[1]]
    elif d2[2] == min_val:
        return [d2[0], d2[1]]
    elif d3[2] == min_val:
        return [d3[0], d3[1]]
    else:
        return [d4[0], d4[1]]

min_distance = sum_of_distances(starting_point[0], starting_point[1], point1, point2, point3, point4)
flag = True
i = 1

while flag:
    d1 = new_distance(starting_point[0] + increment, starting_point[1], point1, point2, point3, point4)
    d2 = new_distance(starting_point[0] - increment, starting_point[1], point1, point2, point3, point4)
    d3 = new_distance(starting_point[0], starting_point[1] + increment, point1, point2, point3, point4)
    d4 = new_distance(starting_point[0], starting_point[1] - increment, point1, point2, point3, point4)

    print(f"Step {i}: Current Position = ({round(starting_point[0], 2)}, {round(starting_point[1], 2)})")

    minimum = min(d1[2], d2[2], d3[2], d4[2])

    if minimum < min_distance:
        starting_point = best_next_point(minimum, d1, d2, d3, d4)
        min_distance = minimum
        i += 1
    else:
        flag = False

print(f"\nMinimum total distance found at ({round(starting_point[0], 2)}, {round(starting_point[1], 2)})")