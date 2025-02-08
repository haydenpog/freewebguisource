# Skidable Webgui Based Off Minecraft Webgui Clients.


*WARNING YOU MUST HAVE ATLEAST BASIC PYTHON / C# KNOWLEDGE TO EFFECTIVELY USE THIS PROJECT*

This webgui client comes with:
```
Easily hostable
Quick startup.
SQLite Database (With sql injection prevention)
Access subscriptions (P2C)
Custom String Encryption
Login System
Webgui Cheat Menu
Keybinds you edit from web
Realtime Configuring (fast updating)
C# login base
Hidden Files *Flask makes all files hidden through inspect element-sources
Discord bot for managing accounts
    * Create Accounts
    * Ban Accounts
    * Discord link to account
    * Adding subscriptions
    * Logs 
Light weight and fast speeds on even the shittiest of hosting
Somewhat Easy Expandability
Spaghetti code (random ass variable names dont @ me)
```
# Possible questions

Q: How would I add my own custom html files?
A: By editing the template files in the template folder, you can change how your webgui looks!

Q: How do I start up the server?
A: You can either buy a vps and download python on it (easiest), or buy a cheap python hosting server and upload the files

Q: Am I allowed to use this in my p2c 
A: Yes but with credit, and if you don't ill crack ur shit in 2 minutes you nn :D

Q: How long did this take to make?
A: Umm, I skipped doing like 10 weeks worth of classwork doing this so like plz enjoy :D

Q: Is this sustainable and easy to keep up?
A: Its alright, with the new subscriptions it's pretty easy to keep up with

Q: Is this C# only?
A: No, that's all I could give a fuck to do. Feel free to interpret my code into other coding languages how you want.

# To add new features:
* Add new box with things in the html
* Add new form.get for the new items in client  function
* Add to the config write string
* Add to the linkage program so it reads.
* Add the real feature to ur client ofc :D

# How to run the site off a VPS
It's just like a normal pc, start the start.py and make sure you have port 5000 forwarded. The discord bot does not require port-forwarding, so just run the script, and it should work.
To portforward, please check the next section.

# How to portforward off a VPS
https://tryrdp.com/blog/port-forwarding-on-windows-vps/ - Is a guide to do it on a Windows based VPS
https://bit.ly/3QB1SOC - Is a guide to do it on a Linux based VPS

# How do I test this before downloading?
Make a fork and run a github workspace, than pip install both py-cord and flask
after doing that, create 2 configs for hosting them in the debug tab. After that
portforward port 5000. And start both programs, it should run on a website that you could find in the
portforwarding tab. The bot should also be up at this time.

# How to localhost the bot:
* Run start.py
* Run adminbot.py
* done

# How to start the discord bot:
* Change Bot Token to your own
* Change the @commands.has_role("Admin") to your role's names (for people without the role, it won't respond / do anything. it shows as an error in the console but ignore it.)
* Startup adminbot.py on a py host, vps, or even your own pc (remember you have to keep the adminbot py file in the same directory it is now. Otherwise, it may break connections with all the databases, configs, etc.)


