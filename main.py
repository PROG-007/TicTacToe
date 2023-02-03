import os
import random
while True:
    inp=""
    quit=False
    while True:
        os.system("cls")
        inp=str(input("A - Bored? Play against your own computer.\nM - Got some company? Challenge them to this 2 player mode.\nQ - Quit\n\nEnter your Selection: "))
        if len(inp) == 1 and inp.lower() in ['a', "m"]:
            break
        elif len(inp) == 1 and inp.lower() == "q":
            quit=True
            break
        else:
            print("Invalid Choice. Enter Again.")
        os.system("PAUSE")
    if quit:
        os.system("PAUSE")
        break
    board=[[" "]*3 for i in range(3)]
    rows="ABC"
    player=1
    temp=""
    if inp.lower() == "a":
        temp="computer"
    else:
        temp=2
    won=False
    while True:
        a=""
        while True:
            os.system("cls")
            print("  1 2 3")
            for i in range(3):
                print(rows[i],end="")
                for j in range(3):
                    print(f"|{board[i][j]}",end="")
                print("|")
            a=str(input(f"Player {player} - Enter the Box you want to place your symbol on: "))
            if len(a) != 2 or a == None:
                print("Please enter in the format <Row Letter><Column Number>")
            elif int(ord(a[0].lower())) not in [97,98,99]:
                print(f"Please enter a valid Row letter - Instead of {a[0]}, try entering a,b,c.")
            elif int(a[-1]) not in [1,2,3]:
                print(f"Please enter a valid Column number - Instead of {a[-1]}, try entering 1,2,3.")
            elif board[int(ord(a[0].lower()))-97][int(a[-1])-1] != " ":
                print("Sorry, that position is already taken!")
            else:
                break
            os.system("PAUSE")
        if inp.lower() == "a":
            board[int(ord(a[0].lower()))-97][int(a[-1])-1] = "X"
            ############DUMB BOT CODE########################
            lstX=[]
            lstY=[]
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == " ":
                        lstX.append(i)
                        lstY.append(j)
            if len(lstX) != 0:
                rndmIndx=random.choice(range(len(lstX)))
                board[lstX[rndmIndx]][lstY[rndmIndx]] = "O"
            #################################################
        elif inp.lower() == "m":
            if player == 1:
                board[int(ord(a[0].lower()))-97][int(a[-1])-1] = "X"
            elif player == 2:
                board[int(ord(a[0].lower()))-97][int(a[-1])-1] = "O"
            player, temp = temp, player
        os.system("cls")
        print("  1 2 3")
        for i in range(3):
            print(rows[i],end="")
            for j in range(3):
                print(f"|{board[i][j]}",end="")
            print("|")
        for i in range(3):
            sum=0
            for j in board[i]:
                sum+=int(ord(j))
            if sum == int(ord("X"))*3:
                print(f"\nPLAYER 1 WON!!")
                won=True
                os.system("PAUSE")
            elif sum == int(ord("O"))*3:
                if inp.lower() == "a":
                    print(f"\nPLAYER COMPUTER WON!!")
                if inp.lower() == "m":
                    print(f"\nPLAYER 2 WON!!")
                won=True
                os.system("PAUSE")
            if won:
                break
        if won:
            break
        for i in range(3):
            sum=0
            for j in range(3):
                sum+=int(ord(board[j][i]))
            if sum == int(ord("X"))*3:
                print(f"\nPLAYER 1 WON!!")
                won=True
                os.system("PAUSE")
            elif sum == int(ord("O"))*3:
                
                if inp.lower() == "a":
                    print(f"\nPLAYER COMPUTER WON!!")
                if inp.lower() == "m":
                    print(f"\nPLAYER 2 WON!!")
                won=True
                os.system("PAUSE")
            if won:
                break
        if won:
            break
        ind=1
        for _ in range(2):
            sum=0
            for i in range(3):
                if ind == 1:
                    sum+=int(ord(board[2-i][i]))
                else:
                    sum+=int(ord(board[i][i]))
            if sum == int(ord("X"))*3:
                print(f"\nPLAYER 1 WON!!")
                won=True
                os.system("PAUSE")
            elif sum == int(ord("O"))*3:
                if inp.lower() == "a":
                    print(f"\nPLAYER COMPUTER WON!!")
                if inp.lower() == "m":
                    print(f"\nPLAYER 2 WON!!")
                won=True
                os.system("PAUSE")
            else:
                ind=0
            if won:
                break
        if won:
            break
        if not won:
            space=False
            for i in board:
                for j in i:
                    if j == " ":
                        space=True
                        break
                if space:
                    break
            if not space:
                print("\nMatch Drawed")
                won=True
                os.system("PAUSE")
        if won:
            break
