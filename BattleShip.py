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
    # cpu guessing variables:
    count = 0
    firsthit = False  # Becomes True if hit ship once, becomes false once ship is sunken
    shipdestroy = False  # Becomes True when ship is continuing to be destroyed
    counthit = 0  # if greater than 1, shipdestroy becomes True
    # end of cpu guessing variables
    while True:
        sleep(3)
        print("\nYour targets:\n")
        print_board(board)
        while True:  # to see if the coordinate was never hit
            try:
                userrow = int(input("\nEnter a row 1-10: ")) - 1
                usercol = int(input("\nEnter a column 1-10: ")) - 1
            except ValueError:
                print("Try Again")
            hit = preboard[userrow][usercol]
            if hit == "#" or hit == "X":
                print("You already hit that spot. Try Again")
            else:
                break
        if hit != "*":
            preboard[userrow][usercol] = "#"
            board[userrow][usercol] = "X"
            if any(hit in line for line in preboard) == False:
                print("\nYou hit and sunk a ship!")
            else:
                print("\nYou hit!")

        else:
            print("\nYou missed!")
            board[userrow][usercol] = "#"
        tots = 0
        for t in range(len(preboard)):
            for y in preboard[t]:
                if y == "#" or y == "*":
                    tots += 1
        if tots == 100:
            print("\n\nYou Win!")
            break  # if all ships were sunken
        sleep(3)
        print("\n\n\nYour Map:")
        print_board(userboard)
        sleep(1)
        print("\n Waiting for your opponent's move......\n")
        sleep(3)
        # computer's turn Let's begin

        while True:
            if firsthit == False:
                cpurow, cpucol = randint(0, 9), randint(0, 9)
                rand = cpuboard[cpurow][cpucol]
                if rand != "#":
                    break
            else:

                possibledir = [[cpurow + 1, cpucol], [cpurow - 1, cpucol], [cpurow, cpucol + 1], [cpurow, cpucol - 1]]
                if shipdestroy == True:  # continue destruction if target hit 2x in a row
                    if huh <= 1:  # in this if/else statement, it makes the count continue based on the direction the 2nd hit was made
                        if huh == 0:
                            possibledir[huh][
                                0] = cpurow + counthit  # counthit is pretty much the counter (+=1) for the amount of hits before a ship is sunk(then counthit=0)
                        else:
                            possibledir[huh][0] = cpurow - counthit
                    else:
                        if huh == 2:
                            possibledir[huh][1] = cpucol + counthit
                        else:
                            possibledir[huh][1] = cpucol - counthit
                    try:
                        if cpuboard[possibledir[huh][0]][possibledir[huh][1]] != "#":
                            rand = cpuboard[possibledir[huh][0]][possibledir[huh][1]]
                            break
                        else:
                            shipdestroy = False
                    except ValueError:
                        while True:
                            cpurow, cpucol = randint(0, 9), randint(0, 9)
                            rand = cpuboard[cpurow][cpucol]
                            if rand != "#":
                                break
                if shipdestroy == False:  # first target was hit, now just starting to find next target
                    while True:
                        huh = randint(0, 3)
                        try:
                            rand = cpuboard[possibledir[huh][0]][possibledir[huh][1]]
                        except IndexError:
                            cpurow, cpucol = randint(0, 9), randint(0,
                                                                    9)  # if suspected ship coordinate is out of range, it'll just choose a random coordinate
                            rand = cpuboard[cpurow][cpucol]
                        if rand != "#":
                            break
                    break

        if firsthit == False:
            cpuboard[cpurow][cpucol] = "#"
        else:
            cpuboard[possibledir[huh][0]][possibledir[huh][1]] = "#"

        # Now to check the coordinates of the computer
        if rand != "*":
            counthit += 1
            count += 1
            if firsthit == False:
                userboard[cpurow][cpucol] = "X"
            else:
                userboard[possibledir[huh][0]][possibledir[huh][1]] = "X"
            if any(rand in bob for bob in userboard) == False:
                print("\nYou got hit and your ship sunk!")
                counthit = 0
                firsthit = False
                shipdestroy = False
            else:
                print("\nYou got hit!")
                firsthit = True
                if counthit > 1:
                    shipdestroy = True

        else:
            print("\nYour opponent missed")
            shipdestroy = False

        if count == 14:
            sleep(2)
            print("\n\nYou lost!")
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
