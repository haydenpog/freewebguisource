import os
import discord
from discord.ext import commands
from pCrypt import test, testdecode
import sqlite3


'''
How to setup!
* Change Bot Token to your own
* Change guildid to your own guild's id
* Change the @commands.has_role("Admin") to your role's names
* Startup on a py host or a vps
'''

guildid = "1029728497935073311" # Change this to your discord sever's guild id.
token = "MTA2MDkzMzgyMTU4OTEwNjc4OQ.GWTZLX.V0EZ7oRs6GeFTEzHjR6wiCMeSImjzJm_71mUTM" # change to your bot token
bot = commands.Bot()
@bot.slash_command(name="createaccount")
@commands.has_role("Admin") # This is made for buyers so I would maybe recommend switching this to "Buyers" or "Purchased" or whatever
async def createaccount(ctx, username: str, password: str):
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")
    statement = "SELECT id FROM cheat" # find all ids
    cur = conn.cursor()
    cur.execute(statement)
    logins = cur.fetchall()
    print(logins)
    for item in logins:
        for item2 in item:
            if str(ctx.author.id) == item2: # If there is an already an account with your discord id, it wont allow you.
                print("already a user")
                embed = discord.Embed(
                    title="Account Creator",
                    color=discord.Colour.red(),
                )
                embed.add_field(name="Failed", value="You already have an account!")
                await ctx.respond(embed=embed)  # Send the embed with some text
                conn.close()
                return
    # if you go it this far, you dont already have an account, so we will create one!
    embed = discord.Embed(
        title="Account Creator",
        color=discord.Colour.green(),  # Pycord provides a class with default colors you can choose from
    )
    statement = "INSERT INTO cheat VALUES ('%s','%s','%s');" % (test(username), test(password),str(ctx.author.id)) # write to the db your inputed user:pass:discordid
    print(statement) # for debugging, remove if u want
    cur = conn.cursor()
    cur.execute(statement)
    conn.commit()
    print(username,password) # for debugging, remove if u want

    embed.add_field(name="Done", value="The account " + username + " has been created.")
    conn.close()
    await ctx.respond(embed=embed)  # Send the embed with some text


@bot.slash_command(name="checkuserid")
async def checkusersid(ctx,user: discord.User):
    conn = sqlite3.connect("database.db")
    statement = "SELECT username, id FROM cheat" # grab all usernames and ids
    cur = conn.cursor()
    cur.execute(statement)
    logins = cur.fetchall() # save the results to a list
    for item in logins:
        if str(user.id) in item: # if you have an account linked to your discord
            embed = discord.Embed(
                title="Account Checker",
                color=discord.Colour.green(),
                description="User has been found! Their username is: " + testdecode(item[0]) # prints their username
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
    c = open(username + ".ini", "r") # open their config file
    cread = c.read()
    c.close()
    if 'True' in cread: # if anything is true in it, it will turn it off
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
        f.write(cread.replace("None", "True")) # if anything is false it will turn it true
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
    # THIS TOOK 4 HOURS CAUSE IM RETARD
    conn = sqlite3.connect("database.db")
    statement = "SELECT username, id FROM cheat" # grab all usernames and ids
    cur = conn.cursor()
    cur.execute(statement)
    logins = cur.fetchall() # save them to a list
    print(logins)
    conn.close() # close the db
    # For delete
    for item in logins:
        if str(user.id) in item: # if your id is in  the db
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM cheat WHERE id='" + str(user.id) + "';") # delete your account
            conn.commit() # This took me 4 hours to realize that I forgot this singular line. This just saves the db afterward.
            conn.close()

            embed = discord.Embed(
                title="Account Deleter",
                color=discord.Colour.green(),
                description="User has been found! Their username is: " + testdecode(item[0]) + ". Done Deleting!"
            )
            os.remove(testdecode(item[0])+".ini") # delete their config for space reasons.
            await ctx.respond(embed=embed)
            return
    embed = discord.Embed(
        title="Account Deleter",
        color=discord.Colour.red(),
        description="User not found."
    )
    await ctx.respond(embed=embed)
    return


print("running") # just tell u if the bot is actually running
bot.run(token)

