from random import randint
from string import ascii_uppercase
from time import sleep

def usership_creator(map, numtimes):
    alphabet = ascii_uppercase
    print("\n\n\n\nIf any of your ships intersect, we'll ask you to redraw your coordinates. DONT ADD SPACES ")
    for z in range(numtimes):
        size = 2 + z
        letter = alphabet[size - 2]

        while True:
            print("\n\nShip number " + str(z+1) + ":")
            try:
                row = int(input(" Enter a row 1-"+str(10-size)+": "))-1
                col = int(input("\n Enter a column 1-"+str(10-size)+": "))-1
                diro = input(("\n Do you want the ship to be horizontal or vertical? Enter h or v: "))
            except ValueError:
                print("Try Again")
            direction = 1 if diro == "h" else 2


            if direction == 1:  # horizontal
                a = ["*"] * size
                b = map[row][col:col + size]
                if a == b:
                    c = [letter] * size
                    map[row][col:col + size] = c
                    break
            else:  # vertical
                a = ["*"] * size
                b = [map[i][col] for i in range(row, row + size)]
                if b == a:
                    for i in range(row, row + size):
                        map[i][col] = letter
                    break

def shipmaker(map, numtimes):
    alphabet = ascii_uppercase
    for z in range(numtimes):
        size = 2+z
        letter = alphabet[size-2]

        while True:
            direction = randint(1, 2)
            row = randint(0,len(map)-size-1)
            col = randint(0,len(map)-size-1)
            if direction == 1: #horizontal
                a = ["*"]*size
                b = map[row][col:col+size]
                if a == b:
                    c = [letter]*size
                    map[row][col:col+size] = c
                    break
            else: #vertical
                a = ["*"]*size
                b = [ map[i][col] for i in range(row,row+size) ]
                if b==a:
                    for i in range(row,row+size):
                        map[i][col] = letter
                    break

def start_game(userboard, board, preboard, cpuboard):
    sleep(7)
    shipcount = 0
    while True:
        sleep(3)
        print("\nYour targets:\n")
        print_board(board)
        while True: #to see if the coordinate was never hit
            try:
                userrow = int(input("\nEnter a row 1-10: "))-1
                usercol = int(input("\nEnter a column 1-10: "))-1
            except ValueError:
                print("Try Again")
            hit = preboard[userrow][usercol]
            if hit == "#" or hit == "X":
                print("You already hit that spot. Try Again")
            else: break

        if hit != "*":
            preboard[userrow][usercol] = "#"
            board[userrow][usercol] = "X"
            if any(hit in line for line in preboard) == False:
                print("\nYou hit and sunk a ship!")
                shipcount+=1
            else: print("\nYou hit!")

        else:
            print("\nYou missed!")
            board[userrow][usercol] = "#"
        tots = 0
        for t in range(len(preboard)):
            for y in preboard[t]:
                if y == "#" or y=="*":
                    tots+=1
        sleep(1)
        print("\n"+str(shipcount)+" out of 4 ships sunken")
        if tots==100:
            print("\n\nYou Win!")
            break #if all ships were sunken
        sleep(3)
        print("\n\n\nYour Map:")
        print_board(userboard)
        sleep(1)
        print("\n Waiting for your opponent's move......\n")
        sleep(3)
        #computer's turn
        count = 0
        while True:
            cpurow,cpucol = randint(0,9),randint(0,9)
            rand = cpuboard[cpurow][cpucol]
            if rand != "#":
                break
        cpuboard[cpurow][cpucol] = "#"
        if rand != "*":
            count+=1
            if any(rand in bob for bob in userboard) == False:
                print("\nYou got hit and your ship sunk!")
            else: print("\nYou got hit!")
            userboard[cpurow][cpucol] = "X"
        else: print("\nYour opponent missed")
        if count == 14:
            print("\n\nyou lost!")
            break








def print_board(boad):
    for row in boad:
        print(" ".join(row))

board,preboard,userboard,cpuboard = [],[],[],[]



for x in range(10):    #creates the boards and fills them with a 10x10 array filled with "O"
  board.append(["*"] * 10)
  preboard.append(["*"] * 10)
  userboard.append(["*"] * 10)
  cpuboard.append(["*"] * 10)


shipmaker(preboard,4)



print("\n\n\n\n\n\n\n\nWelcome to BattleShip. Pointers: \n -Board is 10x10 \n -the initial ship is 2 blocks long and increases by 1 with every ship "
      "\n -Ship 1 is 'A', Ship 2 is 'B', and so on.. \n Let's start the game with four ships.")
usership_creator(userboard,4)
cpuboard = userboard
print("\n\n\n\n\nHere's what your board looks like. Don't worry, the computer can't cheat.")
sleep(1)
print_board(userboard)
sleep(6)
print("Let's get started! Key: 'X' means the ship was hit, '#' means it missed \n It's your turn first, choose a target to shoot your missile:")


start_game(userboard, board, preboard, cpuboard)

print("\n\n\n                 GAME OVER          ")
