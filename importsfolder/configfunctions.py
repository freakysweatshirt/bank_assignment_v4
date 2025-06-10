import json, sys
def getconfig() -> dict:
    from .utils import log
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            return config
    except json.JSONDecodeError:
        print('json file corrupted \nexiting')
        sys.exit()
    except Exception as e:
            log(f'error: {e} ', 3)

def show_config() -> None:
    from .utils import log
    config = getconfig()
    for index, (setting, state) in enumerate(config.items()):
        log(f'{index} >> {setting} >> {state}', 1)
def change_config() -> None:
    from .utils import log 
    while True:
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
                    log('choice not in options ', 2)
                    continue
                with open('config.json', 'w') as f: 
                    json.dump(config, f)
                    log('setting successfully changed ', 1)
                    break
        except Exception as e:
            print(f'error: {e} ')
