from random import choice

game_board_in_play = ["0", "1", "2", "3", "4", "5", "6", "7", "8"] 
playerX = "Player X"
playerO = "Player O"

def welcome_to_new_game(playerX, playerO):
    print "Welcome to ticTacToe."
    display_board([None, None, None]*3)
    print "Let's begin by choosing player X or player O to begin the game."
    raw_input("Press return to begin this game... ")
    first_player = choose_starting_player(playerX, playerO)
    print "Great, the first player is %s" %first_player
    return first_player

def choose_starting_player(playerX, playerO):
    player_list = [playerX, playerO]
    return choice(player_list)

def get_next_player(current_player, next_player):
    return first_player if current_player == next_player else next_player

def determine_second_player_identity(first_player):
    if first_player == playerX:
        second_player = playerO
    else:
        second_player = playerX
    return second_player

def make_move(current_player):
    # if current_player == playerX:
    #     board_marker = "X"
    # else:
    #     board_marker = "O"
    # return board_marker
     player_marks = {playerX : 'X', playerO : 'O'} #dictionary 
     return player_marks[current_player] #current player is the "index" that is equal to either playerX or playerO

def verify_numerical_selection_for_move(user_move_input):
    #if not (str.isdigit(user_move_input)): #class method
    if not user_move_input.isdigit(): #instance method
        user_move_input = raw_input("Please enter a valid number!\n")
        return verify_numerical_selection_for_move(user_move_input)
    user_move_input = int(user_move_input)
    if user_move_input > 8 or user_move_input < 0:
        user_move_input = raw_input("Please enter a number between 0 and 8!\n")
        return verify_numerical_selection_for_move(user_move_input)
    else:
        return user_move_input

def legal_move(current_board, current_move_selection):
    return current_board[current_move_selection].isdigit()

def game_over(current_board):
    for item in current_board:
        #if (str.isdigit(item)): #class method
        if item.isdigit(): #instance method
            return False
    return True

def there_is_a_winner(current_board):
    winning_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for pos1, pos2, pos3 in winning_combinations:
        for character in "XO":
            if current_board[pos1] == current_board[pos2] == current_board[pos3]:
                return True
    return False

def handle_next_move(current_player, next_player):
    move_selection = raw_input ("Ok, %s, make your move. \n" %current_player)
    verfied_move_selection = verify_numerical_selection_for_move(move_selection)
    
    if legal_move(game_board_in_play, verfied_move_selection):
        game_board_in_play[verfied_move_selection] = make_move(current_player)
        display_board(game_board_in_play)
        if there_is_a_winner(game_board_in_play):
            print "Game over! The winner is %s" %current_player
        elif game_over(game_board_in_play):
            print "Game over! Sadly, no winner. Please try again."
        else:
            handle_next_move(get_next_player(current_player, next_player),next_player)
    else:
        print "That was an illegal move, let's try again..."
        handle_next_move(current_player, next_player)

def play_game(current_player, next_player, current_board):
    #first move
    display_board(current_board) 
    move_selection = raw_input ("Ok, %s, make your first move by selecting a number on the board \nto move to. \n" %current_player)
    verfied_move_selection = verify_numerical_selection_for_move(move_selection)
    current_board[verfied_move_selection] = make_move(current_player)
    display_board(current_board)

    #subsequent moves
    handle_next_move(get_next_player(current_player, next_player), next_player)    

def display_board(current_board):
    board = [x if x else " " for x in current_board] #this is a list comprehension - making a new list based on performing operations on the items of an existing list
    print " {} | {} | {} ".format(board[0], board[1], board[2]) #using a format string, append the print statements with the new contents of board
    print "---+---+---"
    print " {} | {} | {} ".format(board[3], board[4], board[5])
    print "---+---+---"
    print " {} | {} | {} ".format(board[6], board[7], board[8])

#program begins here
first_player = welcome_to_new_game(playerX, playerO) 
second_player = determine_second_player_identity(first_player)
play_game(first_player, second_player, game_board_in_play) 








