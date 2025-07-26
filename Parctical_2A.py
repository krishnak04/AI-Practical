# Simulate 4-Queen / N-Queen problem. #

N = int(input("Enter The Board Size And No.Of Queens To Be Placed:"))
board = [0] * N

def is_safe(row, col):
    for prev_row in range(row):
        if board[prev_row] == col or \
           abs(board[prev_row] - col) == abs(prev_row - row):
            return False
    return True

def solve(row):
    if row == N:
        print_solution()
        return True  # Continue searching for all solutions

    for col in range(N):
        if is_safe(row, col):
            board[row] = col
            if solve(row + 1):
                return True
    return False

def print_solution():
    for i in range(N):
        row = ['.'] * N
        row[board[i]] = 'Q'
        print(" ".join(row))
    print()

solve(0)
