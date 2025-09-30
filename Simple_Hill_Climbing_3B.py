def simple_hill_climbing(numbers):
    if not numbers:
        return None

    current_index = 0
    while current_index + 1 < len(numbers):
        if numbers[current_index] < numbers[current_index + 1]:
            current_index += 1
        else:
            break
    return numbers[current_index]

try:
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.strip().split()))

    max_number = simple_hill_climbing(numbers)
    if max_number is not None:
        print(f"The maximum number found using hill climbing is: {max_number}")
    else:
        print("No numbers were entered.")
except ValueError:
    print("Please enter valid integers separated by spaces.")