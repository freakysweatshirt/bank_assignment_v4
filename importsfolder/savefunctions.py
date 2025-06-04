from .utils import log
import json
accounts_path = 'accounts.json'
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
    