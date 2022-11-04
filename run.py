"""
Battleships game code
"""

import random
import gspread
from google.oauth2.service_account import Credentials

# Colorama module
import colorama
from colorama import Fore, Back, Style

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('battleit')


def loginuser():
    """
    Allows set up of username, or use of existing user, or guest login
    """
    login_valid = False
    while login_valid is False:
        print("----------------------------------------")
        print('[L] Login and play using an existing user')
        print('[M] Make an account to record your score')
        print('[G] Play as a guest\n')
        print('Or [Q] you can quit the game at any time.\n')

        login_option = input('Please enter one of the above letters:\n')

        if login_option in ('L', 'l'):
            user = login_existing_user()
            login_valid = True
        elif login_option in ('M', 'm'):
            user = make_login()
            login_valid = True
        elif login_option in ('G', 'g'):
            login_valid = True
            user = 'Guest'
        elif login_option in ('Q', 'q'):
            print(f"You entered {login_option} to quit the game.")
            print("See you again soon!")
            return 'Q'
        else:
            print("------------")
            print("Please retry as the input you entered is not a valid")
            print(f"You entered: {login_option}, so try again.\n")

    return user


def login_existing_user():
    """
    Runs required login existing user functions
    """
    print('--------------------------------------')
    print("You chose to login an existing user")

    acceptable_username = False

    try:
        login = SHEET.worksheet('login')
        if login:
            print("User details Sheet accessed successfully")
    except gspread.exceptions.APIError as errorv:
        print(f"problem occured accessing sheet data.\n{errorv}")
        return 'Q'

    username_data = login.col_values(1)
    password_data = login.col_values(2)

    print("Please note: \nUsername and Password are case sensitive.\
        \n10 characters or less in length")
    print('--------------------------------------')
    while acceptable_username is False:
        username = input('Please enter your username:\n')

        if username in username_data:
            acceptable_username = True
        elif username in ('q', 'Q'):
            print(f"You have entered {username} to quit the game.")
            print("Hope you come back soon!")
            return 'Q'
        else:
            print(f"Username: '{username}', is not recognised.\
                \nPlease try again\n")

    username_place = username_data.index(username)

    acceptable_password = False
    while acceptable_password is False:
        password = input('Please enter your password here:\n')

        if password == password_data[username_place]:
            print('--------------------------------------')
            print(f"Welcome back {username} !!!")
            acceptable_password = True
        elif password == 'q' or password == 'Q':
            print(f"You have entered {password} to quit the game.")
            print("Hope you come back soon!")
            return 'Q'
        else:
            print(f"Password: {password}, is not recognised please try again")

    return username


def make_login():
    """
    Runs required make login functions
    This function will check if a username is already in use.
    If not in use, the function will save the username and password
    to the spreadsheet and enable the recording of scores
    """

    print("You chose to make a new user login")

    acceptable_username = True

    login = SHEET.worksheet('login')
    score = SHEET.worksheet('score')

    username_data = login.col_values(1)

    print("Please note: \nUsername and Password are case sensitive.\
        \n10 characters or less in length")

    while acceptable_username is True:
        username = input('Please enter your chosen username (max 10 chars):\n')
        acceptable_username = False
        if username in username_data:
            print(
                f"Please select another username. \
                    \n'{username}' has already been selected.\n"
                )
            acceptable_username = True
        elif username.count(' ') >= 1 or username == '' or len(username) > 10:
            print(
                f"Please select another username.\
                    \n'{username}' is not valid.\n"
                )
            acceptable_username = True
        elif username in ('q', 'Q'):
            print(f"You have entered {username} to quit the game.")
            print("Hope you come back soon!")
            return 'Q'

    acceptable_password = True

    while acceptable_password is True:
        password = input('Please enter your password (max 10 chars):\n')
        acceptable_password = False
        if password.count(' ') >= 1 or password == '' or len(password) > 10:
            print(
                f"Please select another password.\
                \n'{password}' is not valid.\n"
                )
            acceptable_password = True
        elif password in ('q', 'Q'):
            print(f"You have entered {password} to quit the game.")
            print("Hope you come back soon!")
            return 'Q'

    new_user = [username, password]
    new_user_score = [username, 0, 0, 0]

    try:
        if login.append_row(new_user):
            print(f"{new_user} appended successfully")
    except gspread.exceptions.APIError as errorv:
        print(f"problem occured appending new user data.\n{errorv}")
        return 'Q'

    try:
        if score.append_row(new_user_score):
            print(f"{new_user} score appended successfully")
    except gspread.exceptions.APIError as errorv:
        print(f"problem occured appending score data.\n{errorv}")
        return 'Q'

    print('Thank you for creating an account')

    return username


def ship_generator():
    """
    Generates random locations for ships
    """
    ships = []
    while len(ships) < 5:
        num1 = str(random.randint(1, 5)) + ',' + str(random.randint(1, 5))
        if num1 not in ships:
            ships.append(num1)
    return ships


def print_boards(computer_board, player_board, user):
    """
    prints locations for ships in horizontal format
    """
    print('----------------------------   \
    ----------------------------')

    print(f"{user}'s ship locations         \
    Computer's ship locations\n")

    board_gap = '                   '
    print(*computer_board[0], board_gap, *player_board[0])
    print(*computer_board[1], board_gap, *player_board[1])
    print(*computer_board[2], board_gap, *player_board[2])
    print(*computer_board[3], board_gap, *player_board[3])
    print(*computer_board[4], board_gap, *player_board[4])
    print(*computer_board[5], board_gap, *player_board[5])
    print(*computer_board[6], board_gap, *player_board[6])

    print(' ')
    print('----------------------------   \
    ----------------------------')


def setup_battleships(user):
    """
    Runs required gameplay functions to set up
    new game boards, locations and moves
    """
    print("Setting up Battleships for", user)

    print('A hit is displayed as a ' + Fore.YELLOW + 'H' + Fore.WHITE)
    print('A miss is displayed as a O')

    player_board = build_board()
    computer_board = build_board()

    players_input_moves = []
    computer_potential_moves = [
        '1,5', '3,4', '1,1', '2,3', '1,4',
        '5,1', '3,3', '5,5', '3,1', '2,2',
        '4,3', '3,5', '4,1', '4,4', '5,3',
        '2,1', '4,5', '4,2', '2,4', '3,2',
        '1,2', '5,4', '2,5', '1,3', '5,2'
        ]

    player_ships_locations = ship_generator()
    computer_ships_locations = ship_generator()

    return player_ships_locations, computer_ships_locations,\
        players_input_moves, computer_potential_moves, \
        player_board, computer_board


def enter_coordinates(ship_map_data, user):
    """
    Runs required result checking functions
    """

    coordinates_not_valid = True
    while coordinates_not_valid is True:

        player_board = ship_map_data[4]
        computer_board = ship_map_data[5]

        print_boards(computer_board, player_board, user)

        # loop until we get valid x,y input
        print("Please enter your move below,")
        print("with column (x) then row (y) separated by a comma\n")
        move = input("i.e. 'x,y' or 'Q' to quit\n")

        if move == 'Q' or move == 'q':
            return 'Q'

        # exit loop if x,y are valid based on checking move entered
        # against player move options
        coordinates_not_valid = move_checker(move, ship_map_data[2])

    # randomly generate computer move from range of valid moves
    computer_move = \
        ship_map_data[3].pop(random.randrange(len(ship_map_data[3])))
    computername = 'Computer'

    # check computer move for a hit or not
    hit_or_miss(computer_move, ship_map_data[0], ship_map_data[5],
                computername, user)
    # check player move for a hit or not
    hit_or_miss(move, ship_map_data[1], ship_map_data[4], user, computername)


def hit_or_miss(move, enemy_ships_locations,
                board_layout, name, oppositions_name):
    """
    Takes the move and checks if it's the same as a enemy ship
    coordinates if so will send a H if not O
    """
    if move in enemy_ships_locations:
        hit = 'H'
        enemy_ships_locations.remove(move)
    else:
        hit = 'O'
    outcome(move, board_layout, hit, name, oppositions_name)


def outcome(move, board_layout, hit, name, oppositions_name):
    """
    Take the users input and edit the board data to insert
    H or O depending if it's a hit or miss
    """
    xandy = move.split(',')
    x_coord = int(xandy[0])
    y_coord = int(xandy[1])

    if hit == 'H':
        board_layout[y_coord][x_coord] = Fore.YELLOW + 'H' + Fore.WHITE
        move_outcome = Fore.YELLOW + 'Hit!' + Fore.WHITE
    else:
        board_layout[y_coord][x_coord] = 'O'
        move_outcome = 'Miss'

    print(' ')
    print(f"{name} fired at {oppositions_name}'s ships.")
    print(f"The target location is: {move} and it's a {move_outcome}")
    print('--------------------------------------')


def build_board():
    """
    Generates the starting board which is blank
    Runs required functions to build a player board/map for ships
    """

    gamemap = [
        ['   ', '1', '2', '3', '4', '5'],
        ['  1', '-', '-', '-', '-', '-'],
        ['  2', '-', '-', '-', '-', '-'],
        ['y 3', '-', '-', '-', '-', '-'],
        ['  4', '-', '-', '-', '-', '-'],
        ['  5', '-', '-', '-', '-', '-'],
        ['   ', ' ', ' ', 'x', ' ', ' ']]
    return gamemap


def display_results_table(result, user):
    """
    Runs required result display functions
    Displays the result of the game and if the player has an
    account will display their total win/lose/draw
    """

    score = SHEET.worksheet('score')

    if user != 'Guest':
        username_place = score.col_values(1).index(user)
        win = score.col_values(2)[username_place]
        lose = score.col_values(3)[username_place]
        draw = score.col_values(4)[username_place]

    if result == 'W':
        print(f"Congratulations {user}, you WON!")
        if user != 'Guest':
            win = int(win) + 1
    elif result == 'L':
        print(f"Sorry {user} you lost. Better luck next time!")
        if user != 'Guest':
            lose = int(lose) + 1
    elif result == 'D':
        print(f"Nearly a win {user}, but you drew!")
        if user != 'Guest':
            draw = int(draw) + 1

    if user != 'Guest' and result != 'Q':
        print("Recording results and displaying results over time")
        print(f"\nWins: {win}\nLoses: {lose}\nDraws: {draw}")

        score.update('B' + str(username_place+1), win)
        score.update('C' + str(username_place+1), lose)
        score.update('D' + str(username_place+1), draw)


def move_checker(move, valid_input_moves):
    """
    Runs required move checking functions
    Checks the players input moves for input being a number, within
    the range of the board, have only entered 2 coordinates, and not
    already been entered
    """
    print('--------------------------------------')

    print("Your Move is: ", move)
    print("Checking if it is valid")

    ranges = range(1, 6)
    moves = move.split(',')

    try:
        if len(moves) != 2:
            print("\nYou entered the incorrect number of coordinates,")
            print(f"You have entered: {len(moves)} coordinates. Please")
            print("enter 2 coordinates only\n")
        elif moves[0].isnumeric() is False:
            print(f"\nx coordinate is not a digit\
                \nYou have entered: {moves[0]}\n")
        elif moves[1].isnumeric() is False:
            print(f"\ny coordinate is not a digit\
                \nYou have entered: {moves[1]}\n")
        elif int(moves[0]) not in ranges:
            print("\nx coordinate is not a row on the map,")
            print(f"you have entered: {moves[0]}\n")
        elif int(moves[1]) not in ranges:
            print("\ny coordinate is not a column on the map,")
            print(f"you have entered: {moves[1]}\n")
        elif move in valid_input_moves:
            print(f"\nYou already fired at this location: {moves}\n")
        else:
            valid_input_moves.append(move)
            return False
    except ValueError:
        print("\nPlease check - entered coordinates are not valid")
        print(f"you entered: {moves}\n")

    return True


def check_moves(ship_data, user):
    """
    Function takes the player and computer ship lists and
    checks the length of the list, and while both have a length
    greater than 0 (indicating ships are left the game) the function continues.
    The enter_coordinates function gets move coordinates
    and outcome for both opponents.
    Unless the player has entered Q to quit the game.
    If the game ends without the player quitting it will also calculate
    if the player won, lost, or drew
    """
    while len(ship_data[0]) > 0 and len(ship_data[1]) > 0:
        print(' ')
        print(f"{user} has {len(ship_data[0])} ships left")
        print(f"Computer has {len(ship_data[1])} ships left\n")
        input("Press enter to see the map and enter a target.")

        if enter_coordinates(ship_data, user) == 'Q':
            print(f"Your remaining ships are at: {ship_data[0]}")
            print(f"The remaining opponent ships are at: {ship_data[1]}\n")
            return 'Q'

    if len(ship_data[0]) != 0 and len(ship_data[1]) == 0:
        # player wins
        print(f"Your remaining ships are at: {ship_data[0]}\n")
        return 'W'
    if len(ship_data[1]) != 0 and len(ship_data[0]) == 0:
        # computer wins
        print(f"The remaining opponent ships are at: {ship_data[1]}\n")
        return 'L'
    if len(ship_data[0]) == 0 and len(ship_data[1]) == 0:
        # both sides were destroyed in the same round -> draw
        return 'D'


def continue_playing():
    """
    Runs required continue playing functions
    to check if player would like to continue playing
    """
    deciding = True
    while deciding is True:
        playchoice = input("\nWould you like to play another game? \
        \nEnter [P] to play again\nor \nEnter [Q] to quit the game\n")

        if playchoice in ('P', 'p'):
            return True
        if playchoice in ('Q', 'q'):
            print('Thank you for playing Battleships!')
            return False

        print(f"Your input is not valid, you have entered: {playchoice},")
        print("Please try again.\n")


def main():
    """
    Runs required overall program functions
    login, playgame, setup, check moves, display and continue
    """
    user = loginuser()
    if user != 'q' and user != 'Q':
        playgame = True
        while playgame is True:
            ship_map = setup_battleships(user)
            current_result = check_moves(ship_map, user)
            display_results_table(current_result, user)
            playgame = continue_playing()


# Checks the game loop
# Allows the user to call other functions for testing
if __name__ == "__main__":
    print("----------------------------------------")
    print('Welcome to the game of Battleships!')
    print("----------------------------------------")
    main()
