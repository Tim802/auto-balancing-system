import bcrypt

def encrypt(rawtxt):
    rawbyte = rawtxt.encode()
    salt = bcrypt.gensalt()
    hashed_txt = bcrypt.hashpw(rawbyte, salt)
    return hashed_txt

def check(input, against):
    check = input.encode()
    if bcrypt.checkpw(check, against):
        return 1
    else:
        return 0