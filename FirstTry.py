import bcrypt
import json

def Salt():
    return bcrypt.gensalt()

def UsernameExists(Usertocheck):
    file = open("Database.json")
    jsonf = json.load(file)
    for user in jsonf:
        Username = user["Username"]
        if Usertocheck == Username:
            return 0
    file.close()
    return 1
def GetHash(Usertocheck):
    file = open("Database.json")
    jsonf = json.load(file)
    for user in jsonf:
        Username = user["Username"]
        if Usertocheck == Username:
            file.close()
            return user["Salt"]
    file.close()
    return 1
def PassMatch(username, password):
    file = open("Database.json")
    jsonf = json.load(file)
    for user in jsonf:
        Username = user["Username"]
        Password = user["Password"]
        if Username == username and password == Password:
            return 0
    file.close()
    return 1
def RPasswords(Pass1,Pass2):
    if Pass1 == Pass2:
        return 1
    else:
        return 0

def register(UserName,PassWord):
    Salty = Salt()
    line = str(UserName + " ")
    WholePass = UserName + PassWord
    HashPass = bcrypt.hashpw(WholePass.encode(),Salty)
    line += HashPass.decode() + " " + Salty.decode()
    lines = {
        "Username": UserName,
        "Password": HashPass.decode(),
        "Salt": Salty.decode()
    }
    with open("Database.json","r") as DatApp:
        data = json.load(DatApp)
        data.append(lines)
    with open("Database.json","w") as Datapp:
        json.dump(data,Datapp,indent = 4)
    return 10
def login(UserName,PassWord,Salt):
    Fullpass = UserName + PassWord
    HashPass = bcrypt.hashpw(Fullpass.encode(),Salt.encode())
    matchcheck = PassMatch(UserName,HashPass.decode())
    if matchcheck == 0:
        return -11
    else:
       return 11