from .savefunctions import get_accounts
from .utils import log
from .storing import decrypt
from main import loggedinmainloop
from dotenv import load_dotenv
import os, getpass
load_dotenv()
def show_all_account_info() -> None:
    accounts = get_accounts()
    for index, account in enumerate(accounts.items()):
        print(f'{index} >> <<username: {account[0]} balance: {decrypt(account[1]['balance'])}>>')

def edit_account_info() -> None:
    while True:
        show_all_account_info()
        try:
            choice = int(input('account to edit >> '))
            if -1 < choice < len(get_accounts()):
                loggedinmainloop(list(get_accounts().keys())[choice])
                break
            else:
                raise IndexError
        except ValueError:
            log('must enter a number ', 2)
            continue
        except IndexError:
            log('invalid option ', 2)
        except Exception as e: 
            log(f'error: {e} ', 3)
def admin_authenticate() -> None:
    admin_pass = getpass.getpass('admin password >> ')
    if os.getenv('ADMIN_PASSWORD') == admin_pass:
        admin_mainloop()
        return 
    log('incorrect password ', 2)

admin_choices = {
    '1': ('show accounts ', show_all_account_info),
    '2': ('edit accounts ', edit_account_info),
    '3': ('exit', None)
}
def admin_mainloop() -> None:
    while True:
        try:
            for i, (text, _) in admin_choices.items():
                print(f'{i}. {text}')
            choice = input('choice >> ').strip()
            if choice not in admin_choices.keys():
                log('choice not in options', 2)
                continue
            elif choice == '3':
                log('exiting admin mode ', 1)
                break
            admin_choices[choice][1]()
            
        except Exception as e: 
            log(f'error: {e} ', 3)