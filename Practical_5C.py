# Game Start
print("\n")
print("\tGame Start\nNow the task is to move all of them to right side of the river")
print("rules:\n1. The boat can carry at most two people\n2. If cannibals num greater than missionaries then the cannibals would eat the missionaries\n3. The boat cannot cross the river by itself with no people on board")

# Initial state
lM = 3
lC = 3
rM = 0
rC = 0
k = 0

# Game loop
while True:
    # Print current state
    print("\n")
    for i in range(lM):
        print("M ", end="")
    for i in range(lC):
        print("C ", end="")
    print("|     --- | ", end="")
    for i in range(rM):
        print("M ", end="")
    for i in range(rC):
        print("C ", end="")
    print("\n")

    # Check for win condition
    if rM == 3 and rC == 3:
        print("You won the game : \n\tCongrats")
        print(f"Total attempts: {k}")
        break

    # Check for lose condition
    if (lM > 0 and lM < lC) or (rM > 0 and rM < rC):
        print("Cannibals eat missionaries:\nYou lost the game")
        break

    # Left side -> Right side river travel
    while True:
        try:
            print("\nLeft side -> right side river travel")
            uM = int(input("Enter number of Missionaries travel :- "))
            uC = int(input("Enter number of Cannibals travel :- "))

            # Validation checks
            if (uM == 0 and uC == 0) or ((uM + uC) > 2) or (uM < 0 or uC < 0) or (lM - uM < 0) or (lC - uC < 0):
                print("Wrong input. Please re-enter.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter numbers.")

    # Update state after left to right travel
    lM -= uM
    lC -= uC
    rM += uM
    rC += uC
    k += 1

    # Check for lose condition after left->right
    if (lM > 0 and lM < lC) or (rM > 0 and rM < rC):
        print("\nCannibals eat missionaries:\nYou lost the game")
        break

    # Print updated state
    print("\n")
    for i in range(lM):
        print("M ", end="")
    for i in range(lC):
        print("C ", end="")
    print("| --> | ", end="")
    for i in range(rM):
        print("M ", end="")
    for i in range(rC):
        print("C ", end="")
    print("\n")

    # Check for win condition again
    if rM == 3 and rC == 3:
        print("You won the game : \n\tCongrats")
        print(f"Total attempts: {k}")
        break

    # Right side -> Left side river travel
    while True:
        try:
            print("\nRight side -> Left side river travel")
            userM = int(input("Enter number of Missionaries travel :- "))
            userC = int(input("Enter number of Cannibals travel :- "))

            # Validation checks
            if (userM == 0 and userC == 0) or ((userM + userC) > 2) or (userM < 0 or userC < 0) or (rM - userM < 0) or (rC - userC < 0):
                print("Wrong input. Please re-enter.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter numbers.")

    # Update state after right to left travel
    lM += userM
    lC += userC
    rM -= userM
    rC -= userC
    k += 1

    # Check for lose condition after right->left
    if (lM > 0 and lM < lC) or (rM > 0 and rM < rC):
        print("\nCannibals eat missionaries:\nYou lost the game")
        break
