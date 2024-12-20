from flask import Flask, abort, render_template, request
import FirstTry

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
    if FirstTry.UsernameExists(UserName) == 0:
        return render_template("Error.html")
    if FirstTry.RPasswords(PassWord,RPassWord) == 0:
        return render_template("Error2.html")
    FirstTry.register(UserName,PassWord)
    return render_template("Success.html")
@app.route("/login")
def Login():
    return render_template("Login.html")
@app.route("/Login", methods=['POST'])
def LoginProc():
    UserName = request.form.get('UserName')
    PassWord = request.form.get('PassWord')
    if FirstTry.UsernameExists(UserName) == 1:
        return render_template("Error.html")
    Salt = FirstTry.GetHash(UserName)
    if FirstTry.login(UserName,PassWord,Salt) == -11:
        return render_template("Success.html")
    else:
        return render_template("Error2.html")



