import os
board=[[" "]*3 for i in range(3)]
rows="ABC"
player=1
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
    if player == 1:
        board[int(ord(a[0].lower()))-97][int(a[-1])-1] = "X"
    elif player == 2:
        board[int(ord(a[0].lower()))-97][int(a[-1])-1] = "O"
    else:
        board[int(ord(a[0].lower()))-97][int(a[-1])-1] = " "
    player, temp = temp, player
    os.system("cls")
    print("  1 2 3")
    for i in range(3):
        print(rows[i],end="")
        for j in range(3):
            print(f"|{board[i][j]}",end="")
        print("|")
    for i in range(2):
        sum=0
        for j in range(3):
            sum+=int(ord(board[j][i]))
        if sum == int(ord("X"))*3:
            print("\n PLAYER 1 WON!!")
            won=True
        elif sum == int(ord("O"))*3:
            print("\n PLAYER 2 WON!!")
            won=True
        if won:
            break
    if won:
        break
    for i in range(2):
        sum=0
        for j in range(3):
            sum+=int(ord(board[i][j]))
        if sum == int(ord("X"))*3:
            print("\n PLAYER 1 WON!!")
            won=True
        elif sum == int(ord("O"))*3:
            print("\n PLAYER 2 WON!!")
            won=True
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
            print("\n PLAYER 1 WON!!")
            won=True
        elif sum == int(ord("O"))*3:
            print("\n PLAYER 2 WON!!")
            won=True
        else:
            ind=0
        if won:
            break
    if won:
        break
