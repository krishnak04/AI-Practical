import os
import time

Board = [' '] * 10
Player = 1
Win = 1
Draw = -1
Running = 0
Game = Running
Mark = 'X'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def DrawBoard():
     print(f"{Board[1]} | {Board[2]} | {Board[3]} ")
     print("---+---+---")
     print(f" {Board[4]} | {Board[5]} | {Board[6]} ")
     print("---+---+---")
     print(f" {Board[7]} | {Board[8]} | {Board[9]} ")

def Check_Position(x):
    return Board[x] == ' '

def CheckWin():
    global Game
    combos = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # columns
        (1, 5, 9), (3, 5, 7)  # diagonals
    ]
    for combo in combos:
        if Board[combo[0]] == Board[combo[1]] == Board[combo[2]] != ' ':
            Game = Win
            return
    # Check for draw
    if all(Board[i] != ' ' for i in range(1, 10)):
        Game = Draw
    else:
        Game = Running

print("Tic-Tac-Toe Game")
print("Player 1 [X] --- Player 2 [O]\n")
print("Game starting...")
time.sleep(1)

while Game == Running:
    clear_screen()
    DrawBoard()
    if Player % 2 != 0:
        print("Player 1's chance (X)")
        Mark = 'X'
    else:
        print("Player 2's chance (O)")
        Mark = 'O'

    try:
        choice = int(input("Enter position (1-9):-- "))
        if choice < 1 or choice > 9:
            print("Invalid position! Choose between 1 and 9.")
            time.sleep(1)
            continue
    except ValueError:
        print("Invalid input! Enter a number between 1 and 9.")
        time.sleep(1)
        continue

    if Check_Position(choice):
        Board[choice] = Mark
        Player += 1
        CheckWin()
    else:
        print("Position already taken! Try again.")
        time.sleep(1)

clear_screen()
DrawBoard()
if Game == Draw:
    print("Game Draw!")
elif Game == Win:
    Player -= 1
    if Player % 2 != 0:
        print("Player 1 won!")
    else:
        print("Player 2 won!")
