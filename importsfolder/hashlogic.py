def hashpass(password: str) -> str:
    import hashlib
    hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed