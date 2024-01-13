# (c) @PredatorHackerzZ || @TeleRoidGroup

import os
import re

id_pattern = re.compile(r'^.\d+$')

class Config(object):
	API_ID = int(os.environ.get("API_ID", "10261086"))
	API_HASH = os.environ.get("API_HASH", "9195dc0591fbdb22b5711bcd1f437dab")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6419538709:AAHUZvAmXDuaITcnCSHe-Pco28RoF7fC1q0")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Tamil_series_HDT_bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002102114753"))
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "tnshort.net")
	SHORTLINK_API = os.environ.get('SHORTLINK_API', "832ad5ffe369f8dbfcd785735cd76a2b53ee2c46")
	#BOT_OWNER = int(os.environ.get("BOT_OWNER", "1498007933 1426588906"))
	BOT_OWNER = [int(bot_owner) if id_pattern.search(bot_owner) else bot_owner for bot_owner in environ.get('BOT_OWNER', '1498007933 1426588906').split()]
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Abdulxfilestore:Abdulxfilestore@cluster0.qplh8td.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002102114753")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001724477147")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** [Heroku](https://heroku.com)
│
├🔸 **Developer:** [Predator HackerzZ](https://t.me/hari_op)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [ʜᴀʀɪ](https://t.me/hari_op)
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

❌ **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
"""
