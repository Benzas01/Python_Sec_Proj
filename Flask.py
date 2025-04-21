from flask import Flask, abort, render_template, request
import FirstTry
import DB
from password_strength import PasswordStats, policy

paspolicy = policy.PasswordPolicy.from_names(
    entropybits=20
)

app = Flask(__name__)
@app.route("/")
def First():
    return render_template("Yes.html")
@app.route("/register")
def Register():
    return render_template("Register.html")
@app.route("/Register", methods=['POST'])
def RegisterProc():
    UserName = request.form.get('UserName')
    PassWord = request.form.get('PassWord')
    RPassWord = request.form.get('RPassWord')
    if DB.UserExists(UserName) == 1:
        return render_template("Error.html")
    if FirstTry.RPasswords(PassWord,RPassWord) == 0:
        return render_template("Error2.html")
    testedpass = paspolicy.password(PassWord)
    testedpassfails = testedpass.test()
    print(len(testedpassfails))
    if len(testedpassfails) != 0:
        return render_template("Error3.html")
    FirstTry.register(UserName,PassWord)
    return render_template("Success.html")
@app.route("/login")
def Login():
    return render_template("Login.html")
@app.route("/Login", methods=['POST'])
def LoginProc():
    UserName = request.form.get('UserName')
    PassWord = request.form.get('PassWord')
    if DB.UserExists(UserName) == 0:
        return render_template("Error.html")
    Salt = DB.GetHash(UserName)
    print(Salt)
    if FirstTry.login(UserName,PassWord,Salt) == 1:
        return render_template("Success.html")
    else:
        return render_template("Error2.html")



