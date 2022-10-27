# Battleships game code
import random
import gspread
from google.oauth2.service_account import Credentials

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
    Allows set up of user account, or use of existing account, or guest login
    """
    login_valid = False
    while login_valid is False:
        print("Logging in")
        print("----------")
        print('[L] Login and play using an existing account')
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
    print("You chose to login existing user")

    acceptable_username = False

    login = SHEET.worksheet('login')

    username_data = login.col_values(1)
    password_data = login.col_values(2)

    print("Please note: \nUsername and Password are case sensitive.\
        \n20 characters or less in length")

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
            print(f"Welcome back {username}")
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
        username = input('Please enter your username:\n')
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
        password = input('Please enter your password (max 20 chars):\n')
        acceptable_password = False
        if password.count(' ') >= 1 or password == '' or len(password) > 20:
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

    login.append_row(new_user)
    score.append_row(new_user_score)

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


def setup_battleships(user):
    """
    Runs required gameplay functions to set up
    new game boards, locations and moves
    """
    print("Setting up Battleships")

    print('A hit is displayed as a H')
    print('A miss is displayed as a O\n')
    input("Press enter to continue...")

    player_board = build_board()
    computer_board = build_board()

    print('----------------------------   \
    ----------------------------')

    print(f"{user}'s ships locations        \
    Computer's ships locations\n")

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


def coordinates_entered(ship_map, user):
    """
    Runs required result checking functions
    """
    print("getting moves and results")

    coordinates_not_valid = True
    while coordinates_not_valid is True:
        print("Please enter your move below,")
        print("with column (x) then row (y) separated by a comma\n")
        move = input("i.e. 'x,y' or 'Q' to quit\n")

        if move == 'Q' or move == 'q':
            return 'Q'

    print(ship_map)
    return user


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


def show_results(result, user):
    """
    Runs required result display functions
    """
    print("checking results")
    user = 'testuser'
    result = 'winner'
    print("User is: ", user)
    print("Result is: ", result)
    return user


def check_moves(ship_data, user):
    """
    Function takes the player and computer ship lists and
    checks the length of the list, and while both have a length
    greater than 0 (indicating ships are left the game) the function continues.
    The coordinates_entered function gets move coordinates
    and outcome for both opponents.
    Unless the player has entered Q to quit the game.
    If the game ends without the player quitting it will also calculate
    if the player won, lost, or drew
    """
    while len(ship_data[0]) > 0 and len(ship_data[1]) > 0:
        print(' ')
        print(f"{user} has {len(ship_data[0])} ships left")
        print(f"Computer has {len(ship_data[1])} ships left\n")

        if coordinates_entered(ship_data, user) == 'Q':
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
    print("continue playing?")

    deciding = True
    while deciding is True:
        playchoice = input("Would you like to play another game? \
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
    Runs required program functions
    """
    user = loginuser()
    if user != 'q' and user != 'Q':
        playgame = True
        while playgame is True:
            ship_map = setup_battleships(user)
            result = check_moves(ship_map, user)
            show_results(result, user)
            playgame = continue_playing()


# Checks the game loop
# Allows the user to call other functions for testing
if __name__ == "__main__":
    print('Welcome to the game of Battleships!')
    main()
