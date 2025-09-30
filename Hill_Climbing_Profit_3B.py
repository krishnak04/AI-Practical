import random

def Profit(price):
    return - (price - 50) ** 2 + 1000

def Hill_Climbing(start_price, step_size, max_iteration):
    current_price = start_price
    current_Profit = Profit(current_price)

    for i in range(max_iteration):
        neighbor = current_price + random.choice([-step_size, step_size])
        neighbor_Profit = Profit(neighbor)

        if neighbor_Profit > current_Profit:
            current_price = neighbor
            current_Profit = neighbor_Profit
            print(f"Step {i + 1}: Moved to Price = {current_price}, Profit = {current_Profit}")
        else:
            print(f"Step {i + 1}: No Better Price Found. Stopping.")
            break

    return current_price, current_Profit

start_price = random.randint(0, 100)
best_price, best_Profit = Hill_Climbing(start_price, step_size=1, max_iteration=100)
print(f"\nBest Price Found: {best_price}, Max Profit: {best_Profit}")