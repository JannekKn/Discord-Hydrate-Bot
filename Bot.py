import discord
from discord.ext import commands,tasks
import settings
import mysql.connector as database
import datetime

def opendatabase():
    try:
        conn = database.connect(
            user = settings.DATABASE_USER,
            password = settings.DATABASE_PASSWORD,
            host = settings.DATABASE_HOSTNAME,
            port = settings.DATABASE_PORT,
            database = settings.DATABASE_NAME

        )
    except database.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")

    return conn

def addUser(conn, userid, active):
    try:
        cur = conn.cursor()
        statement = "INSERT INTO userlist (userid, active) VALUES (%s, %s)"
        cur.execute(statement, (userid,active))
        conn.commit()
    except database.Error as e:
        print(f"Error Database: {e}")

def UpadteUser(conn, userid, active):
    try:
        cur = conn.cursor()
        statement = "UPDATE userlist SET active = %s WHERE userid = %s"
        cur.execute(statement, (active, userid))
        conn.commit()
    except database.Error as e:
        print(f"Error Database: {e}")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="",intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready!")
    await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name="to hydrated Users", url=settings.TWITCH_URL))
    sendmessage.start()

@bot.event
async def on_message(message):
    if isinstance(message.channel, discord.channel.DMChannel) and message.author != bot.user:
        usermsg = str(message.content).lower()

        if usermsg == "start":
            conn = opendatabase()
            cur = conn.cursor()

            userid = message.author.id

            cur.execute("SELECT userid, active FROM userlist")
            ispresent = 0
            rows = cur.fetchall()
            for row in rows:
                uid = "".join(row[0])
                if uid == str(userid):
                    ispresent = 1
                    if row[1] == '1':
                        isactive = 1
                    else:
                        isactive = 0
                    break
            
            if ispresent == 0:
                addUser(conn, userid, 1)
                await message.channel.send(settings.MSG_REMINDER_START)
                print(message.author.name + " - " + str(userid) + " started alerting")
            else:
                if isactive == 0:
                    UpadteUser(conn, userid, 1)
                    await message.channel.send(settings.MSG_REMINDER_START)
                    print(message.author.name + " - " + str(userid) + " started alerting")
                else:
                    await message.channel.send(settings.MSG_REMINDER_ALREADY_ON)
                    print(message.author.name + " - " + str(userid) + " tried to start but was already started")

            conn.close()

        elif usermsg == "stop":
            conn = opendatabase()
            cur = conn.cursor()

            userid = message.author.id

            cur.execute("SELECT userid, active FROM userlist")
            ispresent = 0
            rows = cur.fetchall()
            for row in rows:
                uid = "".join(row[0])
                if uid == str(userid):
                    ispresent = 1
                    if row[1] == '1':
                        isactive = 1
                    else:
                        isactive = 0
                    break
                
            if ispresent == 0:
                addUser(conn, userid, 0)
                await message.channel.send(settings.MSG_REMINDER_STOP_BUT_WAS_OFF)
                print(message.author.name + " - " + str(userid) + " tried to stop but was never on list")

            else:
                if isactive == 1:
                    UpadteUser(conn, userid, 0)
                    await message.channel.send(settings.MSG_REMINDER_TURNED_OFF)
                    print(message.author.name + " - " + str(userid) + " stoped alerting")
                else:
                    await message.channel.send(settings.MSG_REMINDER_STOP_BUT_WAS_OFF)
                    print(message.author.name + " - " + str(userid) + " tried to stop but was already off")

            conn.close()

        else:
            await message.channel.send(settings.MSG_UNKNOWN_COMMAND)
            print(message.author.name + " - " + str(userid) + " wrote some crap unknown command :P")


@tasks.loop(seconds=1800)
async def sendmessage(): 
    date = str(datetime.date.today())
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    timestamp = date + " - " + current_time

    print(timestamp + ": ALERTS SENDING...")

    conn = opendatabase()
    cur = conn.cursor()

    cur.execute("SELECT userid FROM userlist")

    for user in cur:
        uid = "".join(user)
        user = await bot.fetch_user(uid)
        userguilds = user.mutual_guilds
        if userguilds is not None:
            usermutualguildid = userguilds[0].id
            userguild = bot.get_guild(usermutualguildid)
            member = userguild.get_member(int(uid))
            username = user.name

            status = member.raw_status
            print(username + " is " + status)
            if status != "offline" and status != "idle":
                channel = await user.create_dm()
                embed=discord.Embed(title="HI " + username + ",", color=0x00b3ff)
                embed.set_thumbnail(url=settings.ATTATCHED_PICTURE_LINK)
                embed.add_field(name="Hydrate", value=settings.NOTIFICATION_TEXT, inline=False)
                embed.set_footer(text=settings.NOTIFICATION_FOOTER)
                await channel.send(embed=embed)
    conn.close()

bot.run(settings.TOKEN)


# invite https://discord.com/oauth2/authorize?client_id=911762663971893258&scope=bot