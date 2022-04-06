# what are the steps/requiremenyts needed to make t3(tic tak toe)
# board
# display board
# setting rows and columns
#handle turn
#check win
    #check rows
    #check columns
    #check digonal
#chech tie
#flip player

#-------------Global variable-----------

board = ["-","-","-",
         "-","-","-",
         "-","-","-",]
game_is_running = True
winner = None
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# heres a main logic implemented
def play_game():

    display_board()
    while game_is_running :
        flip()
        handle_turn(current_player)


        check_if_game_ended()

    # The game is ended
    if winner =="X" or winner == "O" :
        print(winner)
    else :
        print("Tie.")



def handle_turn(player):
    print(player,"'s turn")
    position = input("Enter the position from 1 to 9: ")
    #print(position)


    valid = False
    while not valid :

        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("invalid input.\n Enter again from 1 to 9 : " )
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there . Go again !")



    board[position] = player
    display_board()

def flip():
    #global variable we needed
    global current_player

    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"
    return

def check_if_game_ended():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner

    row_winner = check_rows()

    columns_winner = check_columns()

    diagonal_winner = check_diagonals()


    if row_winner:
        winner = row_winner
        print("Winner is : ")
    elif columns_winner:
        winner = columns_winner
        print("Winner is : ")
    elif diagonal_winner:
        winner = diagonal_winner
        print("Winner is : ")

    else :
        winner = None

    return




def check_rows():
    global game_is_running

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_is_running = False


    # displaying winner
    if row_1:
        return board[0]
    if row_2:
        return board[4]
    if row_3:
        return board[8]

    return

def check_columns():

    global game_is_running

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_is_running = False

    # displaying winner
    if column_1:
        return board[0]
    if column_2:
        return board[4]
    if column_3:
        return board[2]

    return


def check_diagonals():
    global game_is_running

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_is_running = False

    # displaying winner
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[4]
    return

def check_if_tie():
    #Theres a tie

    global game_is_running
    if "-" not in board:
        game_is_running = False
    return


#calling the main function
play_game()