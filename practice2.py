# ********guess the number************
# condition : hide a number and ask user to guess the number and tell  how much more and less he enter
# condition : tell user the number of guesses he left
# condition :  No. of guesse he took to finish
# condition : tell the result of game

# blue print
"""@@Ask a user to guess correct number, and ask continiously until user enter correct input!!"""
#hide a number
#make a function for every chances



print("---------------------Guess the number----------------------")

n = 100
flag = True
user_input = int(input("Enter your guess number : "))
def play_game():
    """ This is the main function """
    global user_input
    global flag
    global n
    if user_input != 100:
        while incorrect_number():
            flag = True
    else:
        guessed_number()

# User enter incorrect number
def incorrect_number() :
    more_than_number()
    less_than_number()
    return
# When user input number greater than original number
def more_than_number():
    global n
    global flag
    global user_input
    if user_input > n :
        print("You enter number greater than guesssed number !!")
        return

# When user input number less than original number
def less_than_number():
    global n
    global flag
    global user_input
    global flag
    if user_input < n :
        print("You enter number less than guessed number ")
        return


# When user input correct number
def guessed_number():
    global n
    global user_input
    global flag
    if user_input == n :
        print("You guessed number correctly")
        flag = False

play_game()
