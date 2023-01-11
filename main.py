from flask import Flask, render_template, redirect, url_for, request, make_response
from pCrypt import testdecode, test
import sqlite3




app = Flask(__name__)
oops = ""
username = ""
"""
If you are seeing this you probably downloaded this off github. This webgui source has very bad security
and should have the auth recoded. DO NOT USE SELL THIS YOU WILL GET CRACKED IN HALF A SECOND!
"""


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")

    statement = "SELECT username, password FROM cheat"
    cur = conn.cursor()
    cur.execute(statement)
    logins = cur.fetchall()

    conn.close()
    if request.method == 'POST':
        for item in logins:
            if request.form['username'] != testdecode(item[0]) or request.form['password'] != testdecode(item[1]):
                error = 'Invalid Credentials. Please try again.'
                pass
            if request.form['username'] == testdecode(item[0]) and request.form['password'] == testdecode(item[1]):
                return cheat(request.form["username"])
    return render_template('index.html', error=error)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    error = None
    if str(request.cookies.get('user')) == "admin":
        if request.method == 'POST':
            f = open("account.db", "r")
            if str(request.form['username']) + ":" + str(request.form['password']) in f.read():
                error = 'There is already a user with this name.'
                f.close()
            else:
                f.close()
                c = open("account.db", 'a')
                add = "\n" + str(request.form['username']) + ":" + str(request.form['password'])
                c.write(add)
                c.close()
        return render_template('admin.html', error=error)
    else:
        return


@app.route('/db/<string:authuser>/<string:authpass>')
def db(authuser,authpass):
    if request.method == 'GET':
        conn = sqlite3.connect('database.db')
        statement = "SELECT username, password FROM cheat"
        cur = conn.cursor()
        cur.execute(statement)
        logins = cur.fetchall()
        conn.close()
        for item in logins:
            if testdecode(item[0]) == authuser:
                print("username correct "+ authuser)
                if testdecode(item[1]) == authpass:
                    print("user and pass correct, entering.")
                    return '1'
                else:
                    return '0'
            else:
                return "0"

@app.route('/getcfg/<string:User>', methods=['GET','POST'])
def getconfig(User):
    if request.method == 'GET':
        f = open(User + ".ini", 'r')
        op = f.read()
        f.close()
        return op


@app.route('/set/<string:User>', methods=['POST'])
def set(User):
    if request.method == 'POST':
        data = request.data
        print(data)
        data = data.decode("ASCII")
        print(data)
        try:
            if "True" in data:
                c = open(User + ".ini", "r")
                cread = c.read()
                c.close()
                autoclickercfg = cread.split("|")[0]
                f = open(User + ".ini", "w")
                f.write(autoclickercfg.replace("None","True")+"|"+cread.split("|")[1])
                f.close()
                return "Done"
            elif "None" in data:
                c = open(User + ".ini", "r")
                cread = c.read()
                c.close()
                autoclickercfg = cread.split("|")[0]
                f = open(User + ".ini", "w")
                f.write(autoclickercfg.replace("True", "None") + "|" + cread.split("|")[1])
                f.close()
                return "Done"
        except:
            print("error, crashed.")






def keepsign(signon):
    if signon == True:
        return render_template('home.html')
    elif signon == False:
        return redirect(url_for(login))


@app.route("/")
def home():
    return redirect(url_for("login"))



@app.route('/cheat/<string:User>/', methods=['POST'])
def cheat(User):
    if request.method == 'POST':
        acCPS = str(request.form.get("autoclickcps"))
        acon = str(request.form.get("autoclicker"))
        rvalue = str(request.form.get("reachvalue"))
        reach = str(request.form.get("reach"))
        keybind = str(request.form.get("letter"))
        f = open(User + ".ini", "w")
        print(acon + acCPS + keybind + "|" + reach + rvalue)
        f.write(acon + acCPS + keybind + "|" + reach + rvalue)
        f.close()
        return render_template('home.html', username= User)


