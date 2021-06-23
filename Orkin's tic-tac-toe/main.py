from IPython.display import clear_output
import random


def banner():
    clear_output()
    try:
        title = open('welcome_banner.txt')
        inp = title.read()
        print(inp)
    except:
        print("WELCOME TO ORKIN'S TIC-TAC-TOE!")


def player_names():
    print('ENTER THE PLAYERS NAMES')
    print('default names: Orkin1 & Orkin2')

    player1 = input('Player1:')
    player2 = input('Player2:')

    if player1 == '' or player1 == ' ':
        player1 = 'Orkin1'
    if player2 == '' or player2 == ' ':
        player2 = 'Orkin2'

    if player1 == player2:
        player1 = player1 + '_1'
        player2 = player2 + '_2'

    return (player1, player2)


def player_markers():
    query = input('Mr.' + player1 + ', What do you want?X or O :')
    if query.lower() == 'x':
        player1_marker = 'X'
        player2_marker = 'O'
        return (player1_marker, player2_marker)

    elif query.lower() == 'o' or query == '0':
        player1_marker = 'O'
        player2_marker = 'X'
        return (player1_marker, player2_marker)

    else:
        print('please enter a valid input.')
        player_markers()


def display_board(board, player1, player2):
    clear_output()

    print('═══ '+ player1 + ' Vs ' + player2 +' ═══')
    print('╔═════════════════════╗')
    print('║ ╔═════╔═════╗═════╗ ║')
    print('║ ║  '+board[7]+'  ║  '+board[8]+'  ║  '+board[9]+'  ║ ║')
    print('║ ║═════║═════║═════║ ║')
    print('║ ║  '+board[4]+'  ║  '+board[5]+'  ║  '+board[6]+'  ║ ║')
    print('║ ║═════║═════║═════║ ║')
    print('║ ║  '+board[1]+'  ║  '+board[2]+'  ║  '+board[3]+'  ║ ║')
    print('║ ╚═════╚═════╝═════╝ ║')
    print('╚═════════════════════╝')


def first_turn(player1, player2):
    turn = random.randint(1, 2)
    if turn == 1:
        return player1
    else:
        return player2


def int_query(ques, player, error_msg):
    while True:
        try:
            query = int(input('Mr.' + player+', ' + ques))
            break
        except:
            print(error_msg)
        else:
            int_query(ques, player, error_msg)
    return query

def select_position(board, player, player1, player2, player1_marker, player2_marker):

    query = int_query('Please choose the position where you want to place your marker : ', player, 'Invalid input, Please enter a valid input')

    if query not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print('Mr.' + player + ', please enter a valid position!')
    elif board[query] != ' ':
        print('Mr.' + player + ', position given by you was already occupied. Give another valid position')
    else:
        place_marker(board, query, player, player1, player2, player1_marker, player2_marker)


def place_marker(board, position, player, player1, player2, marker1, marker2):
    if player == player1:
        board[position] = marker1
    elif player == player2:
        board[position] = marker2


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


def full_board(board):
    return ' ' not in board


def replay(player1, player2):
    query = input('Would you like play again Mr.' + player1 + ' & Mr.' + player2 + '? y/n: ').lower()
    return query == 'y'


if __name__ == '__main__':
    banner()
    player1, player2 = player_names()

    while True:
        board = [' '] * 10
        board[0] = '#'

        print('                                 ')
        print('---------------------------------')
        print('Player 1 : ' + player1)
        print('Player 2 : ' + player2)
        print('---------------------------------')
        print('                                 ')

        query = input('ARE YOU READY?y/n :')
        if query.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False
            break

        player1_marker, player2_marker = player_markers()

        display_board(board, player1, player2)
        turn = first_turn(player1, player2)

        while game_on:

            if turn == player1:
                select_position(board, turn, player1, player2, player1_marker, player2_marker)
                display_board(board, player1, player2)
                if win_check(board, player1_marker):
                    print('Congrats Mr.' + player1 + '! You won this game!')
                    break

                elif full_board(board):
                    print('Its a draw! well played')
                    break

                else:
                    turn = player2

            elif turn == player2:
                select_position(board, turn, player1, player2, player1_marker, player2_marker)
                display_board(board, player1, player2)

                if win_check(board, player2_marker):
                    print('Congrats Mr.' + player2 + '! You are the OrkinKing of this game!')
                    break

                elif full_board(board):
                    print('Its a draw! well played')
                    break

                else:
                    turn = player1

        if not replay(player1, player2):
            break
