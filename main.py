import sqlite3
import time
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request

from pCrypt import testdecode

app = Flask(__name__)
oops = ""
username = ""
now = datetime.now()


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    conn = sqlite3.connect('database.db')  # Open db for reading
    print("Opened database successfully")

    statement = "SELECT username, password, sub FROM cheat"  # grabs all the users and passes from the db
    cur = conn.cursor()
    cur.execute(statement)
    logins = cur.fetchall()  # puts them in a list
    conn.close()  # closes the connection, so it doesn't kill the host / ur pc
    if request.method == 'POST':  # checks if u submit ur info
        for item in logins:  # set every login to a seperate list
            if request.form['username'] != testdecode(item[0]) or request.form['password'] != testdecode(item[1]):  # Check if password and username work
                error = 'Invalid Credentials. Please try again.'  # Responds with an error
                pass
            if request.form['username'] == testdecode(item[0]) and request.form['password'] == testdecode(item[1]):  # check if login info correct
                newdate2 = time.strptime(item[2], "%Y-%m-%d")
                newdate1 = time.strptime(now.strftime("%Y-%m-%d"), "%Y-%m-%d")
                if newdate1 < newdate2:
                    return cheat(request.form["username"])  # sends u to the webgui
                else:
                    error = "Your subscription has run out!"
    return render_template('index.html', error=error)  # render the login page with an error if u have one.


@app.route('/db/<string:authuser>/<string:authpass>/<string:date>')  # api link
def db(authuser, authpass, date):
    if request.method == 'GET':
        conn = sqlite3.connect('database.db')  # Opens db
        statement = "SELECT username, password, sub FROM cheat"  # grabs all available login infos
        cur = conn.cursor()
        cur.execute(statement)
        logins = cur.fetchall()  # sets login info to a a list
        print(logins)  # print for debugging, you can remove if u want (only u can see this)
        conn.close()  # kills pc without
        for item in logins:
            print(item)  # print for debugging, you can remove if u want (only u can see this)
            print(testdecode(item[0]),testdecode(item[1]))  # print for debugging, you can remove if u want (only u can see this)
            if testdecode(item[0]) == authuser:  # if one of the usernames matches the one you put in than it sends to password check
                if testdecode(item[1]) in authpass:  # checks if password is correct
                    print("user and pass correct, entering.")
                    newdate2 = time.strptime(item[2], "%Y-%m-%d")
                    newdate1 = time.strptime(date, "%Y-%m-%d")
                    if newdate1 < newdate2:
                        return '1'
                    else:
                        return '0'  # binary epic coding | this just renders a 1 on the page.
        print("FALSE")
        return '0'


@app.route('/getcfg/<string:User>', methods=['GET', 'POST'])
def getconfig(User):
    """
    This is just how I get the config for the link program.
    :param User:
    :return file contents:
    """

    if request.method == 'GET':
        f = open(User + ".ini", 'r')
        op = f.read()
        f.close()
        return op  # Returns the config files contents.


@app.route('/set/<string:User>', methods=['POST'])
def set(User):
    """
    Used for keybinds. When a key is pressed it sends a post request to this link and this changes your cheat on / off.
    :param User:
    :return:
    """
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
                f.write(autoclickercfg.replace("None", "True") + "|" + cread.split("|")[1])
                print(autoclickercfg.replace("None", "True") + "|" + cread.split("|")[1])
                f.close()
                return "Done"
            elif "None" in data:
                c = open(User + ".ini", "r")
                cread = c.read()
                c.close()
                autoclickercfg = cread.split("|")[0]
                f = open(User + ".ini", "w")
                f.write(autoclickercfg.replace("True", "None") + "|" + cread.split("|")[1])
                print(autoclickercfg.replace("True", "None") + "|" + cread.split("|")[1])
                f.close()
                return "Done"
        except:
            print("error, crashed.")


@app.route("/")
# spaghetti code :skull:
def home():
    return redirect(url_for("login"))


def checkreality(config:str): # Check config formating
    #True15a|None3.02
    if "|" in config:
        config = config.split("|")
        if "True" in config[0]:
            return True
        elif "None" in config[0]:
            return True
        else:
            return False
    else:
        return False


@app.route('/cheat/<string:User>/', methods=['POST'])
def cheat(User):
    # cheat and config saving
    conn = sqlite3.connect('database.db')  # Open db for reading
    statement = "SELECT username, sub FROM cheat"  # grabs all the users and passes from the db
    cur = conn.cursor()
    cur.execute(statement)
    logins = cur.fetchall()  # puts them in a list
    conn.close()
    for login in logins:
        if User in testdecode(login[0]):
            sub = login[1]
    if request.method == 'POST':
        # autoclicker
        acCPS = str(request.form.get("autoclickcps"))
        acon = str(request.form.get("autoclicker"))
        keybind = str(request.form.get("letter"))

        # reach
        rvalue = str(request.form.get("reachvalue"))
        reach = str(request.form.get("reach"))

        configset = str(request.form.get("cfgset"))

        '''
        To add new features:
        * Add new box with things in the html
        * Add new form.get in here
        * Add to the config below V
        * Add to the linkage program so it reads.
        * Add to ur cheat ofc :D
        '''
        f = open(User + ".ini", "w")
        f.write(acon + acCPS + keybind + "|" + reach + rvalue)
        f.close()
        if checkreality(configset) == True:
            d = open(User + ".ini", "w")
            print(configset)
            d.write(configset)
            d.close()
        else:
            print("false")
        return render_template('home.html', username=User, sub=sub)
