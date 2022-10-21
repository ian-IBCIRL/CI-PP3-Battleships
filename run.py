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

    return False


def make_login():
    """
    Runs required make login functions
    """
    print("You chose to make a new user login")

    return False


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


def check_moves(ship_map, user):
    """
    Runs required result checking functions
    """
    print("getting moves and results")
    ship_map = "displaying map"
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
