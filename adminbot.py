import discord
from discord.ext import commands
from pCrypt import pencode
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
        color=discord.Colour.red(),  # Pycord provides a class with default colors you can choose from
    )
    statement = "INSERT INTO cheat VALUES ('%s','%s','%s');" % (pencode(username), pencode(password),str(ctx.author.id))
    print(statement)
    cur = conn.cursor()
    cur.execute(statement)
    conn.commit()
    print(username,password)

    embed.add_field(name="Done", value="The account " + username + " has been created.")
    f = open("account.db","a")
    conn.close()
    await ctx.respond(embed=embed)  # Send the embed with some text

@bot.slash_command(name="checkid") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def checkifused(ctx):
    conn = sqlite3.connect("database.db")
    statement = "SELECT id FROM cheat"
    cur = conn.cursor()
    cur.execute(statement)
    logins = cur.fetchall()
    print(logins)
    for item in logins:
        for item2 in item:
            if str(ctx.author.id) == item2:
                print("already a user")
    conn.close()

print("running")
bot.run(token)

