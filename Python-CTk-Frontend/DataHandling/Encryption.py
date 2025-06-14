import bcrypt

def encrypt(rawtxt):
    rawbyte = rawtxt.encode()
    salt = bcrypt.gensalt()
    hashed_txt = bcrypt.hashpw(rawbyte, salt)
    return hashed_txt

def check(input, against):
    check = input.encode()
    match_bool = bcrypt.checkpw(check, against)
    print('check result:', match_bool)
    return match_bool