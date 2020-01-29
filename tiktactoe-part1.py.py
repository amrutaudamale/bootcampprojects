import random
import sys

board = {i: None for i in range(1,10)}


def show(board):
    '''
    To print the board
    :param board: takes dictionary as a parameter with 10 key-values pairs
    :return: nothing
    '''
    print("Board:\n{}|{}|{}\n{}|{}|{}\n{}|{}|{}\n".format(board[7], board[8], board[9], board[4], board[5], board[6],board[1], board[2], board[3]))


def choose_first():
    '''
    Function to choose first player randomly
    :return: nothing
    '''
    player_id = random.randint(1,2)
    if player_id == 2:
        print(f"player{player_id} will go first and it is now our player1 and hence player1 will be player2")


def make_a_choice():
    '''
    Function to get choice of "X" "O" from first player
    :return:
    '''
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input(f"Player1, choose X or O:")
    player_1 = marker
    if player_1 == 'X':
        return('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    '''
    Function to mark a position on board
    :param board: board, marker and position where to mark
    :param marker: euther "X" or "O"
    :param position:
    :return: None
    '''
    board[position] = marker
    show(board)


def player_choice(board):
    choice = 0
    while choice == 0:
        try:
            choice_list = [i for i in board if board[i] is None]
            if len(choice_list) == 0:
                print("\n\n Game Over, no one won the game")
                sys.exit()
            else:
                choice = int(input("{}".format([i for i in board if board[i] is None])))
        except Exception as excp:
            print("Exception:{}".format(excp))
            choice = 0
        if board[choice] is not None:
            print("Position occupied; Retry:")
            choice = 0
        else:
            return choice


def win_check(board, mark):
    return ((board[7] == board[5] == board[3] == mark or
    board[7] == board[4] == board[1] == mark or
    board[7] == board[8] == board[9] == mark or
    board[8] == board[5] == board[2] == mark or
    board[9] == board[6] == board[3] == mark or
    board[1] == board[2] == board[3] == mark or
    board[4] == board[5] == board[6] == mark or
    board[1] == board[5] == board[9] == mark) and not None)

def replay():
    play_again = input("Do you want to play again [yes/no]")
    if play_again == "yes":
        return True
    else:
        return False


if __name__ == "__main__":
    print("Welcome to Tic Tac Toe Game!!")
    choose_first()
    player1, player2 = make_a_choice()
    print("\nplayer1 : {}, player2: {}\n".format(player1,player2))
    show(board)
    while True:
        # player 1 choice
        print(f"Player1: Mark {player1} from positions :", )
        position_1 = player_choice(board)
        place_marker(board, player1, position_1)
        if win_check(board, player1):
            print("\n\nCongratulations!,Player1 won the game!")
            break

        # player 2 choice
        print(f"Player2: Mark {player2} from positions :",)
        position_2 = player_choice(board)
        place_marker(board, player2, position_2)
        # check if anyone won
        if win_check(board, player2):
            print("\n\nCongratulations!, Player2 won the game!")
            break
    #if not replay():
        #    break