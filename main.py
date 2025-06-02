from importsfolder.imports import *





options = {
    '1': ('deposit', deposit),
    '2': ('withdraw', withdraw),
    '3': ('change username', change_username),
    '4': ('change password',change_password),
    '5': ('show account info', show_account_info),
    '6': ('logout', None), 
    '7': ('delete account', delete_account)
}

def login() -> None: 
    while True:
        username = input('username >> ').strip()
        password = getpass.getpass().strip()

        if authenticate(username, password):
            loggedinmainloop(username)
            break
        log('incorrect login credentials', 2)
        continue

def loggedinmainloop(passed_username) -> None:
    username = passed_username
    while True:
        for i, (text, _) in options.items():
            print(f'{i}. {text}')
        choice = input('choice >> ').strip()
        if choice not in options.keys():
            log('choice not in options', 2)
            continue
        elif choice == '3':
            username = change_username(username)
            continue
        elif choice == '6':
            log('logging out... ', 1)
            break
        elif choice == '7':
            if delete_account(username):
                break
            continue

        options[choice][1](username)

def mainloop() -> None:
    while True:
        print('1. create account \n2. login \n3. quit program ')
        choice = input('choice >> ')
        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice =='3':
            log('quitting program... ',1)
            sys.exit()

try:
    if __name__ == '__main__':
        mainloop()
except KeyboardInterrupt:
    log('\nprogram was manually shutdown', 2)
    sys.exit()
except Exception as e:
    log(f'error: {e} ', 3)
    sys.exit()

#test
#double test
#triple test
###quad test
###############newtest
#FINALTEST