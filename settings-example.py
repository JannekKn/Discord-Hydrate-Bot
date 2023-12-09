#Settings for Bot, please fill out / replace everything

#Discord Bot Token (https://discord.com/developers/applications)
TOKEN = 'YourBotToken'

#Database Credentials
DATABASE_USER     = "databaseuser"
DATABASE_PASSWORD = "0123456789"
DATABASE_HOSTNAME = "1.1.1.1"
DATABASE_PORT     = 49153
DATABASE_NAME     = "DatabaseName"

#The Bot Status is "Streaming to hydrated Users", this is Twitch Link where you get redirected if you click on Watch in the Useer Popout
TWITCH_URL = 'https://www.twitch.tv/jannek'

#How long should the Bot wait until reminding again? Time in seconds:
TIMER = 1800 # Default is 1800 seconds (30min) | if you update this, please also update the time in the MSG_REMINDER_START Message

#Chat Messages
MSG_REMINDER_START = 'Du wurdest mit auf die Liste zum erinnern gesetzt! \nDu wirst nun alle 30min daran erinnert etwas zu trinken... \nDies jedoch nur wenn du online bist, damit der Bot nicht nervt, falls du nicht am PC sitzt \nfalls du dich auf offline stellst :middle_finger: :)'
MSG_REMINDER_ALREADY_ON = 'Du bist schon auf der kack Liste (╯°□°）╯︵ ┻━┻ <- Datenbank'
MSG_REMINDER_TURNED_OFF = 'wurdest von der Liste genommen!'
MSG_REMINDER_STOP_BUT_WAS_OFF = 'Die Erinnerung war für dich gar nicht an, falls du trotzdem benachrichtigt wirst schreib Jannek'
MSG_UNKNOWN_COMMAND = 'Es gibt nur 2 Commands: \n- start \n- stop'

#Hydrate Notification
NOTIFICATION_TEXT = 'Dies ist deine Erinnerung etwas zu trinken!'
ATTATCHED_PICTURE_LINK = 'http://jannek.desertbushgames.de/robotwaterBottle.png'
NOTIFICATION_FOOTER = 'Bot by Jannek'