import pwinput, getpass
from .configfunctions import *

def log(text: str, state: int) -> None:
    colors = {4:'\033[0m',3:'\033[31m',2:'\033[33m',1:'\033[32m'}
    print(colors[state] + text + colors[4])
    return None

def setpassword() -> str:
    from .storing import hashpass
    setting = getconfig()['hide_password']
    while True:
        if setting == 'MASK':
            password = hashpass(pwinput.pwinput(prompt='password >> ', mask='*'))
            password_confirm = hashpass(pwinput.pwinput(prompt='password confirmation >> ', mask='*'))
        elif setting == 'HIDE':
            password = hashpass(getpass.getpass('password >> '))
            password_confirm = hashpass(getpass.getpass('password confirmation >> '))
        elif setting == 'FALSE':
            password = input('password >> ')
            password_confirm = input('password confirmation >> ')
        if not password:
            log('password cannot be empty ', 2)
        elif  password == password_confirm:
            return password
        else: 
            log('failed to confirm password, try again ', 2)
            continue


def getpassword():
    setting = getconfig()['hide_password']
    if  setting == 'MASK':
        return pwinput.pwinput(prompt='password >> ', mask='*')
    elif setting == 'HIDE':
        return getpass.getpass('password >> ')
    elif setting == 'FALSE':
        return input('password >> ')
