import json, sys
def getconfig() -> dict:
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            return config
    except json.JSONDecodeError:
        print('json file corrupted \nexiting')
        sys.exit()
    except Exception as e:
            print(f'error: {e} ')

def show_config() -> None:
    config = getconfig()
    for index, (setting, state) in enumerate(config.items()):
        print(f'{index} >> {setting} >> {state}')
def change_config() -> None:
    try:
        config = getconfig()
        show_config()
        choice = (input('choice >> '))
        if choice == '0':
            print('1. mask \n2. hide \n3. show')
            choice = input('choice>> ').strip()
            if choice == '1':
                config['hide_password'] = 'MASK'
            elif choice == '2':
                config['hide_password'] = 'HIDE'
            elif choice == '3':
                config['hide_password'] = 'FALSE'
            else:
                print('choice not in options ')
            with open('config.json', 'w') as f: 
                json.dump(config, f)
    except Exception as e:
        print(f'error: {e} ')
