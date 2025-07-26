def tower_of_hanoi(n, source, destination, intermediate):
    if n == 1:
        print(f"Move disc 1 from pole {source} to pole {destination}")
        return
    tower_of_hanoi(n - 1, source, intermediate, destination)
    print(f"Move disc {n} from pole {source} to pole {destination}")
    tower_of_hanoi(n - 1, intermediate, destination, source)

try:
    n = int(input("Enter Number Of Discs: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        tower_of_hanoi(n, 'A', 'C', 'B')
except ValueError:
    print("Invalid input! Please enter an integer.")