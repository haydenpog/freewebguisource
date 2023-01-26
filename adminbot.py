from datetime import datetime, timedelta
import os
import discord
from discord.ext import commands
from pCrypt import test, testdecode
import sqlite3

'''
How to setup!
* set debug to false if it isnt already.
* Change Bot Token to your own
* Change guildid to your own guild's id
* Change the @commands.has_role("Admin") to your role's names
* Startup on a py host or a vps
'''

debug = False
now = datetime.now()
token = ""  # change to your bot token
bot = commands.Bot()


@bot.slash_command(name="debug")
@commands.has_role("Admin")  # This is made for buyers, so I would maybe recommend switching this to "Buyers" or "Purchased" or whatever
async def debugmode(ctx):
    global debug
    if not debug:
        debug = True
        await ctx.respond("Debug Enabled. This may take a few seconds to refresh")
    else:
        debug = False
        await ctx.respond("Debug Disabled. This may take a few seconds to refresh")


@bot.slash_command(name="createaccount")
@commands.has_role("Admin")  # This is made for buyers so I would maybe recommend switching this to "Buyers" or "Purchased" or whatever
async def createaccount(ctx, username: str, password: str):
    f = open("logs.txt", "a")
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")
    statement = "SELECT id FROM cheat"  # find all ids
    cur = conn.cursor()
    cur.execute(statement)
    logins = cur.fetchall()
    print(logins)
    for item in logins:
        for item2 in item:
            if str(ctx.author.id) == item2:  # If there is an already an account with your discord id, it won't allow you.
                print("already a user")
                embed = discord.Embed(
                    title="Account Creator",
                    color=discord.Colour.red(),
                )
                embed.add_field(name="Failed", value="You already have an account!")
                await ctx.respond(embed=embed)  # Send the embed with some text
                yesr = str("[-] | " + now.strftime("%d/%m/%Y %H:%M:%S") + " | " + str(ctx.author.id) + " tried to create an account and failed\n")
                f.write(yesr)
                f.close()
                conn.close()
                return
    # if you go it this far, you don't already have an account, so we will create one!
    embed = discord.Embed(
        title="Account Creator",
        color=discord.Colour.green(),  # Pycord provides a class with default colors you can choose from
    )
    statement = "INSERT INTO cheat VALUES ('%s','%s','%s','%s');" % (test(username), test(password), str(ctx.author.id),now.strftime("%Y-%m-%d"))  # write to the db your inputed user:pass:discordid
    print(statement)  # for debugging, remove if u want
    cur = conn.cursor()
    cur.execute(statement)
    conn.commit()
    print(username, password)  # for debugging, remove if u want
    embed.add_field(name="Done", value="The account " + username + " has been created.")
    conn.close()
    yesr = str("[+] | " + now.strftime("%d/%m/%Y %H:%M:%S") + " | " + str(ctx.author.id) + " successfully created an account\n")
    f.write(yesr)
    f.close()
    await ctx.respond(embed=embed)  # Send the embed with some text
    return


@bot.slash_command(name="setsub")
@commands.has_role("Admin")  # This is made for buyers so I would maybe recommend switching this to "Buyers" or "Purchased" or whatever
async def setsubscription(ctx, username: str, length: int):
    start_date = now.strftime("%m/%d/%y")
    date_1 = datetime.strptime(start_date, "%m/%d/%y")
    end_date = date_1 + timedelta(days=length)
    end_date = str(end_date)[:10]
    print(end_date)
    conn = sqlite3.connect('database.db')
    statement = "SELECT username FROM cheat"  # find all ids
    cur = conn.cursor()
    cur.execute(statement)
    logins = cur.fetchall()
    for login in logins:
        print(login)
        if testdecode(login[0]) == username:
            conn.close()
            # set sub
            conn2 = sqlite3.connect('database.db')
            statement2 = "UPDATE cheat SET sub = '%s' WHERE username = '%s';" % (end_date, login[0])  # find all ids
            cur2 = conn2.cursor()
            cur2.execute(statement2)
            conn2.commit()
            conn2.close()
            embed = discord.Embed(
                title="Account Creator",
                color=discord.Colour.green(),  # Pycord provides a class with default colors you can choose from
                description="You have added " + str(length) + " days to their sub!"
            )
            await ctx.respond(embed=embed)
            return


@bot.slash_command(name="checkuserid")
async def checkusersid(ctx, user: discord.User):
    conn = sqlite3.connect("database.db")
    statement = "SELECT username, id FROM cheat"  # grab all usernames and ids
    cur = conn.cursor()
    cur.execute(statement)
    logins = cur.fetchall()  # save the results to a list
    for item in logins:
        if str(user.id) in item:  # if you have an account linked to your discord
            embed = discord.Embed(
                title="Account Checker",
                color=discord.Colour.green(),
                description="User has been found! Their username is: " + testdecode(item[0])  # prints their username
            )
            await ctx.respond(embed=embed)
            return
    embed = discord.Embed(
        title="Account Checker",
        color=discord.Colour.red(),
        description="User has not been found."
    )
    print(logins)
    conn.close()
    await ctx.respond(embed=embed)
    return


@commands.has_role("Admin")
@bot.slash_command(name="trolluser")
async def trolluser(ctx, username: str):
    c = open(username + ".ini", "r")  # open their config file
    d = open("logs.txt", "a")
    cread = c.read()
    c.close()
    if 'True' in cread:  # if anything is true in it, it will turn it off
        f = open(username + ".ini", 'w')
        f.write(cread.replace("True", "None"))
        f.close()
        embed = discord.Embed(
            title="Account Checker",
            color=discord.Colour.green(),
            description="I have swapped the users settings to False :troll:"
        )
        yesr = str(" [+] | " + now.strftime("%d/%m/%Y %H:%M:%S") + " | " + str(ctx.author.id) + " has trolled " + username + " successfully\n")
        d.write(yesr)
        d.close()
        await ctx.respond(embed=embed)
        return
    else:
        f = open(username + ".ini", 'w')
        f.write(cread.replace("None", "True"))  # if anything is false it will turn it true
        f.close()
        embed = discord.Embed(
            title="Account Checker",
            color=discord.Colour.green(),
            description="I have swapped the users settings to True :troll:"
        )
        yesr = str("[+] | " + now.strftime("%d/%m/%Y %H:%M:%S") + " | " + str(ctx.author.id) + " has trolled " + username + " successfully\n")
        d.write(yesr)
        d.close()
        await ctx.respond(embed=embed)
        return


@commands.has_role("Admin")
@bot.slash_command(name="banaccount")
async def banaccount(ctx, user: discord.User):
    # THIS TOOK 4 HOURS CAUSE IM DUMB
    conn = sqlite3.connect("database.db")
    statement = "SELECT username, id FROM cheat"  # grab all usernames and ids
    cur = conn.cursor()
    cur.execute(statement)
    logins = cur.fetchall()  # save them to a list
    print(logins)
    conn.close()  # close the db
    # For delete
    for item in logins:
        if str(user.id) in item:  # if your id is in  the db
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM cheat WHERE id='" + str(user.id) + "';")  # delete your account
            conn.commit()  # This took me 4 hours to realize that I forgot this singular line. This just saves the db.
            conn.close()

            embed = discord.Embed(
                title="Account Deleter",
                color=discord.Colour.green(),
                description="User has been found! Their username is: " + testdecode(item[0]) + ". Done Deleting!"
            )
            d = open("logs.txt", "a")
            yesr = str(
                "[*] | " + now.strftime("%d/%m/%Y %H:%M:%S") + " | " + str(ctx.author.id) + " has banned " + testdecode(
                    item[0]) + " successfully\n")
            d.write(yesr)
            d.close()
            await ctx.respond(embed=embed)
            try:
                os.remove(testdecode(item[0]) + ".ini")  # delete their config for space reasons.
            except:
                print("User doesnt have a config. Continuing")
                pass
            return
    embed = discord.Embed(
        title="Account Deleter",
        color=discord.Colour.red(),
        description="User not found."
    )
    await ctx.respond(embed=embed)
    return


@commands.has_role("Admin")
@bot.slash_command(name="cleardata")
async def cleardata(ctx, areyousure: bool):
    if debug == True:
        if areyousure:
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("DROP TABLE cheat;")  # delete your account
            cur.execute("CREATE TABLE cheat (username text,password text,id text,sub text);")
            import pathlib
            path = str(pathlib.Path(__file__).parent.resolve())
            for x in os.listdir(path):
                if x.endswith(".ini"):
                    print(x)
                    os.remove(path + r'/' + x)
            cur.execute("INSERT INTO cheat VALUES ('%s','%s','0','9999-12-25');" % (test("admin"), test("admin")))
            conn.commit()
            conn.close()
            await ctx.respond("DB HAS BEEN RESET | Login: admin:admin")
            return
        else:
            await ctx.respond("dumbass")
    else:
        await ctx.respond("Debug mode is currently is disabled.")


@commands.has_role("Admin")
@bot.slash_command(name="logs")
async def logs(ctx):
    await ctx.send(file=discord.File(r'logs.txt'))


@commands.has_role("Admin")
@bot.slash_command(name="changepassword")
async def changepassword(ctx, newpass: str):
    conn = sqlite3.connect("database.db")
    statement = "SELECT username, id FROM cheat"  # grab all usernames and ids
    cur = conn.cursor()
    cur.execute(statement)
    logins = cur.fetchall()  # save the results to a list
    for item in logins:
        if str(ctx.author.id) in item:  # if you have an account linked to your discord
            conn.close()
            embed = discord.Embed(
                title="Account Checker",
                color=discord.Colour.green(),
                description="User has been found!" + testdecode(item[0]) + "'s Password has been changed."
                # prints their username
            )
            conn2 = sqlite3.connect("database.db")
            statement2 = "UPDATE cheat SET password = '%s' WHERE id = '%s'" % (test(newpass), str(ctx.author.id))  # grab all usernames and ids
            cur2 = conn2.cursor()
            cur2.execute(statement2)
            conn2.commit()
            conn2.close()
            await ctx.respond(embed=embed)
            return
    embed = discord.Embed(
        title="Account Checker",
        color=discord.Colour.red(),
        description="User has not been found."
    )
    print(logins)
    conn.close()
    await ctx.respond(embed=embed)
    return


print("running")  # just tell u if the bot is actually running
bot.run(token)
