# Discord-Hydrate-Bot
A Discord Bot that reminds you and others to hydrate  
Feel free to copy and change
  
If you want to test the Bot you can join [This Test Discord](https://discord.gg/dR7QmEzpah) and DM the Hydrate Bot  
(only keeps working if you have at least one mutual Server with the Bot)  
  
If you want to invite this Bot to your Server, so you dont have to join the Test Server klick [on this invite](https://discord.com/oauth2/authorize?client_id=911762663971893258&scope=bot)

## What you need to host yourself
A Server with python and pip  
  
A Database - tested with MariaDB  
You need one Table with two rows  
  
Table name: userlist  
Row name 1 (data type TEXT): userid  
Row name 2 (data type TEXT): active

### Step 1
Clone this Repository  
```git clone https://github.com/JannekKn/Discord-Hydrate-Bot```

### Step 2
Install required packages with pip  
```pip install -r requirements.txt```

### Step 3
Create Bot at the [Discord Application Page](https://discord.com/developers/applications "https://discord.com/developers/applications")

### Step 4 - DONT FORGET
Change the settings-example.py file to settings.py and change the settings in it for your needs  
Most important the Discord Bot Token and Database Credentials  
If you are not german or just wanna change it, change the Chat Messages and Notification Messages

### Step 4
Run the Bot somewhere in a screen or something
```python3 Bot.py```