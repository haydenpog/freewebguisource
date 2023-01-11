import discord
from discord.ext import commands
from pCrypt import test, testdecode
import sqlite3




guildid = "1029728497935073311"
token = "MTA2MDkzMzgyMTU4OTEwNjc4OQ.GWTZLX.V0EZ7oRs6GeFTEzHjR6wiCMeSImjzJm_71mUTM"
bot = commands.Bot()
@bot.slash_command(name="createaccount") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
@commands.has_role("Admin")
async def createaccount(ctx, username: str, password: str):
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")
    statement = "SELECT id FROM cheat"
    cur = conn.cursor()
    cur.execute(statement)
    logins = cur.fetchall()
    print(logins)
    for item in logins:
        for item2 in item:
            if str(ctx.author.id) == item2:
                print("already a user")
                embed = discord.Embed(
                    title="Account Creator",
                    color=discord.Colour.red(),  # Pycord provides a class with default colors you can choose from
                )
                embed.add_field(name="Failed", value="You already have an account!")
                await ctx.respond(embed=embed)  # Send the embed with some text
                return

    embed = discord.Embed(
        title="Account Creator",
        color=discord.Colour.green(),  # Pycord provides a class with default colors you can choose from
    )
    statement = "INSERT INTO cheat VALUES ('%s','%s','%s');" % (test(username), test(password),str(ctx.author.id))
    print(statement)
    cur = conn.cursor()
    cur.execute(statement)
    conn.commit()
    print(username,password)

    embed.add_field(name="Done", value="The account " + username + " has been created.")
    f = open("account.db","a")
    conn.close()
    await ctx.respond(embed=embed)  # Send the embed with some text


@bot.slash_command(name="checkuserid") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def checkusersid(ctx,user: discord.User):
    conn = sqlite3.connect("database.db")
    statement = "SELECT username, id FROM cheat"
    cur = conn.cursor()
    cur.execute(statement)
    logins = cur.fetchall()
    #user.id()
    for item in logins:
        if str(user.id) in item:
            embed = discord.Embed(
                title="Account Checker",
                color=discord.Colour.green(),
                description="User has been found! Their username is: " + testdecode(item[0])
            )
            await ctx.respond(embed=embed)
            return
    embed = discord.Embed(
        title="Account Checker",
        color=discord.Colour.red(),
        description="User has not been found."
    )
    await ctx.respond(embed=embed)
    return
    print(logins)
    conn.close()

@commands.has_role("Admin")
@bot.slash_command(name="trolluser")
async def trolluser(ctx, username: str):
    c = open(username + ".ini", "r")
    cread = c.read()
    c.close()
    if 'True' in cread:
        f = open(username+".ini", 'w')
        f.write(cread.replace("True","None"))
        f.close()
        embed = discord.Embed(
            title="Account Checker",
            color=discord.Colour.green(),
            description="I have swapped the users settings to False :troll:"
        )
        await ctx.respond(embed=embed)
        return
    else:
        f = open(username + ".ini", 'w')
        f.write(cread.replace("None", "True"))
        f.close()
        embed = discord.Embed(
            title="Account Checker",
            color=discord.Colour.green(),
            description="I have swapped the users settings to True :troll:"
        )
        await ctx.respond(embed=embed)
        return

@commands.has_role("Admin")
@bot.slash_command(name="banaccount")
async def banaccount(ctx, user: discord.User):
    # for read
    conn = sqlite3.connect("database.db")
    statement = "SELECT username, id FROM cheat"
    cur = conn.cursor()
    cur.execute(statement)
    logins = cur.fetchall()
    conn.close()
    # For delete
    conn2 = sqlite3.connect("database.db")
    cur2 = conn2.cursor()

    # user.id()
    for item in logins:
        if str(user.id) in item:
            print(user.id)
            cur2.execute("DELETE FROM cheat WHERE id='%s'" % user.id)
            cur2.fetchall()
            conn2.close()
            embed = discord.Embed(
                title="Account Deleter",
                color=discord.Colour.green(),
                description="User has been found! Their username is: " + testdecode(item[0]) + ". Done Deleting!"
            )
            await ctx.respond(embed=embed)
            return
    embed = discord.Embed(
        title="Account Deleter",
        color=discord.Colour.red(),
        description="User not found."
    )
    await ctx.respond(embed=embed)
    print(logins)
    return


print("running")
bot.run(token)

