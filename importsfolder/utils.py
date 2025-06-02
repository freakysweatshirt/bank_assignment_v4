import getpass, json, sys; sys.dont_write_bytecode = True
accounts_path = 'saved\\accounts.json'
from .hashlogic import hashpass
def log(text: str, state: int) -> None:
    colors = {4:'\033[0m',3:'\033[31m',2:'\033[33m',1:'\033[32m'}
    print(colors[state] + text + colors[4])
    return None

def setpassword() -> str:
    while True:
        password = hashpass(getpass.getpass('password >> '))
        password_confirm = hashpass(getpass.getpass('password confirmation >> '))
        if not password:
            log('password cannot be empty ', 2)
        elif  password == password_confirm:
            return password
        else: 
            log('failed to confirm password, try again ', 2)
            continue

def get_accounts() -> dict:
    try: 
        with open(accounts_path, 'r') as f:
            users  = json.load(f)
            return users
    except Exception as e: 
        log(f'error: {e} ', 3)
        return {}


def save_accounts(accounts: dict) -> None:
    try: 
        with open(accounts_path, 'w') as f:
            json.dump(accounts, f, indent=4)
    except Exception as e: 
        log(f'error: {e} ', 3)
    