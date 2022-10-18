# Battleships game code
import random
import time
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
    Runs required login functions
    """
    print("logging in")
    return 'testuser'


def play_battleships(user):
    """
    Runs required gameplay functions
    """
    print("playing battleships")
    user = 'testuser'
    random_number = random.randint(1, 100)
    print(random_number)
    current_time = time.gmtime()
    print(current_time)

    print(user)
    return user


def check_result(ship_map, user):
    """
    Runs required gameplay functions
    """
    print("playing battleships")
    ship_map = 1
    print(ship_map)
    return user


def results(result, user):
    """
    Runs required result functions
    """
    print("checking results")
    user = 'testuser'
    result = 'winner'
    print(result)
    print(user)
    return user


def continue_playing():
    """
    Runs required continue playing functions
    """
    print("checking results")
    user = 'testuser'
    result = 'winner'
    print(result)
    print(user)
    return user


def main():
    """
    Runs required program functions
    """
    user = loginuser()
    if user != 'q' and user != 'Q':
        playgame = True
        while playgame is True:
            ship_map = play_battleships(user)
            result = check_result(ship_map, user)
            results(result, user)
            playgame = continue_playing()


print('Welcome to the game of Battleships!')
main()
