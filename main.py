from flask import Flask, render_template, redirect, url_for, request, make_response
from pCrypt import pdecode, pencode
import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

statement = "SELECT username, password FROM cheat"
cur = conn.cursor()
cur.execute(statement)
logins = cur.fetchall()


conn.close()


app = Flask(__name__)
oops = ""
username = ""
"""
If you are seeing this you probably downloaded this off github. This webgui source has very bad security
and should have the auth recoded. DO NOT USE SELL THIS YOU WILL GET CRACKED IN HALF A SECOND!
"""
p = open("account.db","r")
print(p.read())
p.close


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        for item in logins:
            if request.form['username'] != pdecode(item[0]) or request.form['password'] != pdecode(item[1]):
                error = 'Invalid Credentials. Please try again.'
                pass
            if request.form['username'] == pdecode(item[0]) and request.form['password'] == pdecode(item[1]):
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


@app.route('/db')
def db():
    f = open('account.db', 'r')
    read = f.read()
    return read


@app.route('/getcfg/<string:User>', methods=['GET','POST'])
def getconfig(User):
    if request.method == 'GET':
        f = open(User + ".ini", 'r')
        op = f.read()
        f.close()
        return op
    if request.method == 'POST':
        c = open(User + ".ini", "r")
        if "True" in c.read():
            c.write(c.read().replace("True","None"))
        elif "None" in c.read():
            c.write(c.read().replace("None","True"))

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
                f = open(User + ".ini", "w")
                f.write(cread.replace("None","True"))
                f.close()
                return "Done"
            elif "None" in data:
                c = open(User + ".ini", "r")
                cread = c.read()
                c.close()
                print('bal')
                f = open(User + ".ini", "w")
                f.write(cread.replace("True","None"))
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

@app.route("/testy", methods=['POST','GET'])
def loginold():
    logindict()
    error = None
    if request.method == 'POST':
        for item in logindict():
            item = item.split(":")
            if request.form['username'] != item[0] or request.form['password'] != item[1]:
                error = 'Invalid Credentials. Please try again.'
                pass
            if request.form['username'] == item[0] and request.form['password'] == item[1]:
                return cheat(request.form["username"])
    return render_template('login.html', error=error)


@app.route('/cheat/<string:User>/', methods=['POST'])
def cheat(User):
    if request.method == 'POST':
        acCPS = str(request.form.get("name_of_slider"))
        acon = str(request.form.get("autoclicker"))
        keybind = str(request.form.get("letter"))
        f = open(User + ".ini", "w")
        f.write(acon + acCPS + keybind)
        f.close()
        return render_template('home.html', username= User)


