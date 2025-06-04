from .imports import  setpassword, log
from .savefunctions import get_accounts, save_accounts
from .storing import *

def authenticate(username, password) -> bool:
    accounts = get_accounts()
    if username in accounts and hashpass(accounts[username]['password']) == password:
        return True
    return False


def create_account() -> None:
    from main import loggedinmainloop
    while True:    
        try:
            username = input('username >> ').strip()
            if username in get_accounts():
                log('username is taken ', 2)
                continue
            elif not username:
                log('username cannot be empty', 2)
                continue
            password = setpassword()
            balance = int(input('balance >> '))
            

            if balance < 0:
                log('balance must be 0 or more ', 2)
                continue

            accounts = get_accounts()
            accounts[username] = { 'password': password, 'balance': encrypt(str(balance))}
            save_accounts(accounts)

            log('account successfully created ', 1)
            break
        except ValueError:
            log('balance must be a number ', 2)
            continue
        except Exception as e: 
            log(f'error: {e} ', 3)
            break
    loggedinmainloop(username)

def deposit(username) -> None:
    while True:
        accounts = get_accounts()
        try:
            log(f'current balance: {decrypt(accounts[username]['balance'])} ', 2)
            deposit = int(input('money to deposit >> '))
            if deposit <= 0:
                log('number must be over 0 ', 2)
                continue
            new_balance = int(decrypt(accounts[username]['balance'])) + deposit
            accounts[username]['balance'] = encrypt(str(new_balance))
            save_accounts(accounts)
            log(f'successfully deposited {deposit} dollars , balance is now {new_balance}', 1)
            break
        except ValueError:
            log('please enter a number ', 2)
            continue
        except Exception as e:
            log(f'error: {e} ', 3)


def withdraw(username) -> None: 
    accounts = get_accounts()
    while True:
        try:
            balance = int(decrypt(accounts[username]['balance']))
            log(f'current balance: {balance} ', 2)
            if balance <= 0:
                log('account has no money ', 2)
                continue
            withdraw = int(input('money to withdraw >> '))
            if withdraw <= 0:
                log('number must be over 0 ', 2)
                continue
            if withdraw > balance:
                log('cannot take out more than account holds ', 2)
                continue
            new_balance = int(decrypt(accounts[username]['balance'])) - withdraw
            accounts[username]['balance'] = encrypt(str(new_balance))  
            save_accounts(accounts)
            log(f'successfully withdrew {withdraw} dollars , balance is now {new_balance}', 1)
            break
        except ValueError:
            log('please enter a number ', 2)
            continue
        except Exception as e:
            log(f'error: {e} ', 3)


def change_username(username) -> str:
    accounts = get_accounts()
    while True:
        try:
            new_user = input('new username >> ').strip()
            if new_user in accounts:
                log('username taken ', 2)
                continue
            if new_user == username:
                log('new username must be different to current username ', 2)
                continue
            accounts[new_user] = accounts.pop(username)
            save_accounts(accounts)
            log('username successfully reset ', 1)
            return new_user
        except Exception as e:
            log(f'error: {e} ', 3)


def change_password(username) -> None:
    accounts = get_accounts()
    while True:
        try:
            new_password = setpassword()
            if not new_password:
                log('password must not be empty ', 2)
                continue
            accounts[username]['password'] = new_password
            save_accounts(accounts)
            log('password successfully reset ', 1)
            break
        except Exception as e:
            log(f'error: {e} ', 3)


def show_account_info(username) -> None:
    accounts = get_accounts()
    log(f'username : {username} \nbalance: {decrypt(accounts[username]['balance'])}', 1)

def delete_account(username) -> bool:
    accounts = get_accounts()
    while True:
        choice = input('are you sure you want to delete your account? y/n ').strip().lower()
        if choice == 'y':
            log('deleting account...', 3)
            del accounts[username]
            save_accounts(accounts)
            log('account successfully deleted ', 1)
            return True
        elif choice == 'n':
            log('account has not been altered ', 2)
            return False
        else:
            log('choice not in options ', 2 )
            continue