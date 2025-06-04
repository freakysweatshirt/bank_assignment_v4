from .utils import log
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os, sys

def hashpass(password: str) -> str:
    import hashlib
    hashed = hashlib.sha3_256(password.encode('utf-8')).hexdigest()
    return hashed




def load_key() -> Fernet:
    load_dotenv()
    try:
        key_str = os.getenv('ENCRYPTION_KEY')
        if key_str == None:
            raise ValueError
        key = key_str.encode()
        return Fernet(key)
    except ValueError:
        log('environment variable key is not set')
        sys.exit()
    except Exception as e: 
        log(f'error: {e} ', 3)
        sys.exit()
        

def encrypt(info: str) -> str:
    key = load_key()
    encrypted = key.encrypt(info.encode('utf-8'))
    return encrypted.decode('utf-8')

def decrypt(info: str) -> str:
    try:
        key = load_key()
        return key.decrypt(info.encode('utf-8')).decode('utf-8')
    except Exception as e: 
        log(f'failed to decode: {e} ', 3)
        sys.exit()