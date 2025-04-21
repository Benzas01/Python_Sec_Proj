import bcrypt
import json
import DB

def Salt():
    return bcrypt.gensalt()
def RPasswords(Pass1,Pass2):
    if Pass1 == Pass2:
        return 1
    else:
        return 0

def register(UserName,PassWord):
    Salty = Salt()
    WholePass = UserName + PassWord
    HashPass = bcrypt.hashpw(WholePass.encode(),Salty)
    DB.InsertUser(UserName,HashPass.decode(),Salty.decode())
    return 10
def login(UserName,PassWord,Salt):
    Fullpass = UserName + PassWord
    HashPass = bcrypt.hashpw(Fullpass.encode(),Salt.encode())
    matchcheck = DB.PassMatch(UserName,HashPass.decode())
    if matchcheck == True:
        return 1
    else:
       return -1