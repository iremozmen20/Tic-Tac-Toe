import random

t = [[" "," "," "],
     [" "," "," "],
     [" "," "," "]]
def player_number():
    try:
        s = int(input("Please enter the number of players(1-2): "))
        return s
    except ValueError:
        return print("Please enter a valid input!"), player_number()

def board():
    #Game Board
    print(t[0][0] + "|" + t[0][1] + "|" + t[0][2])
    print("-"*5)
    print(t[1][0] + "|" + t[1][1] + "|" + t[1][2])
    print("-" * 5)
    print(t[2][0] + "|" + t[2][1] + "|" + t[2][2])
    return True
def winner(a):
    #Checking for a Winner
    k=False
    for i in range(3):
        if t[i][0] == t[i][1] == t[i][2] == a:
            k = True
        elif t[0][i] == t[1][i] == t[2][i] == a:
            k = True
        elif t[0][0] == t[1][1] == t[2][2] == a:
            k = True
        elif t[0][2] == t[1][1] == t[2][0] == a:
            k = True
    return k
def x_moves():
    #Player X's moves
    print("X's turn:")
    try:
        x = input("Please enter the row and column number(1-2-3): ")
        a = list(map(int, x.split(" ")))
        if t[a[0] - 1][a[1] - 1] == " ":
            t[a[0] - 1][a[1] - 1] = "X"
            return board()
        else:
            print("THE CELL IS FULL! TRY AGAIN!")
            return board(), x_moves()
    except IndexError:
        print("INVALID ROW AND COLUMN! TRY AGAIN!")
        return board(), x_moves()
    except ValueError:
        print("INVALID INPUT! TRY AGAIN!")
        return board(), x_moves()

def o_moves():
    #Player O's moves
    print("O's turn:")
    try:
        o = input("Please enter the row and column number(1-2-3): ")
        b = list(map(int, o.split(" ")))
        if t[b[0] - 1][b[1] - 1] == " ":
            t[b[0] - 1][b[1] - 1] = "O"
            return board()
        else:
            print("THE CELL IS FULL! TRY AGAIN!")
            return board(), o_moves()
    except IndexError:
        print("INVALID ROW AND COLUMN! TRY AGAIN!")
        return board(), o_moves()
    except ValueError:
        print("INVALID INPUT! TRY AGAIN!")
        return board(), o_moves()

def ai_moves():
    #AI
    print("O's turn:")
    empty = []
    for i in range(3):
        for j in range(3):
            if t[i][j] == " ":
                empty.append((i,j))
    if empty:
        move = random.choice(empty)
        t[move[0]][move[1]] = "O"
        return board()


def tie():
    #Tie
    tf = True
    if winner("X") or winner("O"):
        tf = False
    else:
        for i in range(3):
            for j in range(3):
                if t[i][j] == " ":
                    tf = False
                    break
    return tf

sb = [["X","|","O"],
      ["____"],
      [0,"|",0]]

def score_counter():
    if winner("X") == True:
        sb[2][0] += 1
    elif winner("O") == True:
        sb[2][2] += 1
    print("X"+"|"+"O")
    print("----")
    print(str(sb[2][0])+ "|"+str(sb[2][2]))

def new_round():
    a = input("Would you like to play one more round? (Yes-No): ").capitalize()
    if a == "Yes":
        global t
        t = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
        return tic_tac_toe()
    elif a == "No":
        return print("Game Over! Thanks for playing!")
    else:
        return print("Enter a valid input!"), new_round()

def tic_tac_toe():
    #The main function of the game
    if player_number() == 2:
        board()
        for i in range(9):
            x_moves()
            if tie():
                return print("TIE!")
            elif winner("X"):
                return print("THE WINNER IS X!"), score_counter(), new_round()
            o_moves()
            if winner("O"):
                return print("THE WINNER IS O!"), score_counter(), new_round()
    else:
        board()
        for i in range(9):
            x_moves()
            if tie():
                return print("TIE!"), score_counter(), new_round()
            elif winner("X"):
                return print("THE WINNER IS X!"), score_counter(), new_round()
            ai_moves()
            if winner("O"):
                return print("THE WINNER IS AI!"), score_counter(), new_round()

tic_tac_toe()
