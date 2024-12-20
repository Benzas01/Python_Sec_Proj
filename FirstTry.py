import bcrypt

def Salt():
    return bcrypt.gensalt()

def UsernameExists(Usertocheck):
    file = open("Database.txt")
    for x in file:
        Username = x.split(" ")[0]
        if Usertocheck == Username:
            file.close()
            return 0
    file.close()
    return 1
def GetHash(Usertocheck):
    file = open("Database.txt")
    for x in file:
        Username = x.split(" ")[0]
        if Usertocheck == Username:
            file.close()
            return x.split(" ")[2]
    file.close()
    return 1
def PassMatch(username, password):
    file = open("Database.txt")
    for x in file:
        Username = x.split(" ")[0]
        Password = x.split(" ")[1]
        print(f";{username};{Username};\n;{password};{Password};")
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
    DatApp = open("Database.txt",'a')
    line = str(UserName + " ")
    WholePass = UserName + PassWord
    HashPass = bcrypt.hashpw(WholePass.encode(),Salty)
    line += HashPass.decode() + " " + Salty.decode()
    DatApp.write("\n" + line)
    DatApp.close()
    return 10
def login(UserName,PassWord,Salt):
    Fullpass = UserName + PassWord
    HashPass = bcrypt.hashpw(Fullpass.encode(),Salt.encode())
    matchcheck = PassMatch(UserName,HashPass.decode())
    if matchcheck == 0:
        return -11
    else:
       return 11