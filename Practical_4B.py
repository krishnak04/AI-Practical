# Solve water jug problem. #

capacity = (12, 8, 5)
x = capacity[0]
y = capacity[1]
z = capacity[2]

memory = {}
ans = []

def get_all_state(state):
    a, b, c = state
    if a == 6 and b == 6:
        ans.append(state)
        return True

    if (a, b, c) in memory:
        return False

    memory[(a, b, c)] = 1

    # Pour from A to B
    if a > 0 and b < y:
        pour_amount = min(a, y - b)
        if get_all_state((a - pour_amount, b + pour_amount, c)):
            ans.append(state)
            return True

    # Pour from A to C
    if a > 0 and c < z:
        pour_amount = min(a, z - c)
        if get_all_state((a - pour_amount, b, c + pour_amount)):
            ans.append(state)
            return True

    # Pour from B to A
    if b > 0 and a < x:
        pour_amount = min(b, x - a)
        if get_all_state((a + pour_amount, b - pour_amount, c)):
            ans.append(state)
            return True

    # Pour from B to C
    if b > 0 and c < z:
        pour_amount = min(b, z - c)
        if get_all_state((a, b - pour_amount, c + pour_amount)):
            ans.append(state)
            return True

    # Pour from C to A
    if c > 0 and a < x:
        pour_amount = min(c, x - a)
        if get_all_state((a + pour_amount, b, c - pour_amount)):
            ans.append(state)
            return True

    # Pour from C to B
    if c > 0 and b < y:
        pour_amount = min(c, y - b)
        if get_all_state((a, b + pour_amount, c - pour_amount)):
            ans.append(state)
            return True

    # Empty A
    if a > 0:
        if get_all_state((0, b, c)):
            ans.append(state)
            return True

    # Empty B
    if b > 0:
        if get_all_state((a, 0, c)):
            ans.append(state)
            return True

    # Empty C
    if c > 0:
        if get_all_state((a, b, 0)):
            ans.append(state)
            return True

    return False

# Start solving
initial_state = (12, 0, 0)
print("Start state:", initial_state)
memory = {}
ans = []

if get_all_state(initial_state):
    ans.reverse()
    print("\nSolution Path:")
    for state in ans:
        print(state)
else:
    print("\nNo Solution found to reach (6, 6) from", initial_state)
