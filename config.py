import os, time

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "23898744")
    API_HASH  = os.environ.get("API_HASH", "0b13c810c80b548604650cbe3c3db0c3")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7029462153:AAGu6Le5E5IiAwK3OQQJj5KB-rYDj-gms3Q") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","JUBA_Pro_Renamer_Bot")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://filmyrohesh51:19SmDYqC1N5DqLkD@cluster0.jogzc68.mongodb.net/?retryWrites=true&w=majority")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/10227000cc9b8620abee0.jpg https://graph.org/file/a73c87a2f99e29a240c34.jpg https://graph.org/file/a95265c23620402559db5.jpg https://graph.org/file/890b6ddf19d515a4754ad.jpg https://graph.org/file/5ca2e65d1ec560ed81dcf.jpg https://graph.org/file/d04ce639d3914b922e180.jpg https://graph.org/file/934334a974d5d930b6ae5.jpg https://graph.org/file/23676243e6c911ca0d6e3.jpg https://graph.org/file/9e815b9d16e996c779d9b.jpg https://graph.org/file/200b827daa7e557f9448c.jpg https://graph.org/file/4d85f124eaf90f3ec5df9.jpg https://graph.org/file/e9b250020c683566f81f6.jpg https://graph.org/file/66b73942bc5a454ca19bb.jpg https://graph.org/file/b89b57383666ed579f006.jpg https://graph.org/file/400a70a15a05f6a6339af.jpg https://graph.org/file/bac3c0e4701f34d7447cd.jpg https://graph.org/file/f962b9e88b2ab1737d21c.jpg https://graph.org/file/d86db9732b4b430edb65c.jpg https://graph.org/file/4d95f39f922a3e0f09d6f.jpg https://graph.org/file/03cde96db2ac56f7cd7de.jpg https://graph.org/file/e6bf0acaf479cea2fe350.jpg https://graph.org/file/bcfd3c61329fa96eb86d4.jpg")
    ADMIN = int(os.environ.get("ADMIN", "5698613889"))

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "Rohesh_Bots") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002076092559"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """Hii {}  

𝚃ʜɪs 𝙸s  𝙿ᴏᴡᴇʀғᴜʟ 𝚁ᴇɴᴀᴍᴇ 𝙱ᴏᴛ
𝚄sɪɴɢ 𝚃ʜɪs 𝙱ᴏᴛ 𝚈ᴏᴜ 𝙲ᴀɴ 𝚁ᴇɴᴀᴍᴇ & 𝙲ʜᴀɴɢᴇ 𝚃ʜᴜᴍʙɴᴀɪʟ 𝙾ғ 𝚈ᴏᴜʀ 𝙵ɪʟᴇ 
𝚈ᴏᴜ 𝙲ᴀɴ 𝙰ʟsᴏ 𝙲ᴏɴᴠᴇʀᴛ 𝚅ɪᴅᴇᴏ 𝚃ᴏ 𝙵ɪʟᴇ & 𝙵ɪʟᴇ 𝚃ᴏ 𝚅ɪᴅᴇᴏ 

Bot Is Made By : @Rohesh_Bots"""

    ABOUT_TXT = """
╭───────────────⍟
├<b>🤖 My Name</b> : {}
├<b>🖥️ Developer</b> : <a href=https://t.me/Rohesh_Gavit>Rohesh Bots</a> 
├<b>👨‍💻 Programer</b> : <a href=https://t.me/Rohesh_Gavit>Rohesh Developer</a>
├<b>📕 Library</b> : <a href=https://github.com/pyrogram>Pyrogram</a>
├<b>✏️ Language</b> : <a href=https://www.python.org>Python 3</a>
├<b>💾 Database</b> : <a href=https://cloud.mongodb.com>Mongo DB</a>
├<b>📊 Build Version</b> : <a href=https://t.me/rohesh_bots>Rename v4.5.0</a></b>     
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

✏️ <b><u>How To Rename A File</u></b>

➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].           

𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/Rohesh_Gavit>Developer</a>
"""

    PROGRESS_BAR = """\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ <b>🗃️ Sɪᴢᴇ:</b> {1} | {2}
┣⪼ <b>⏳️ Dᴏɴᴇ :</b> {0}%
┣⪼ <b>🚀 Sᴩᴇᴇᴅ:</b> {3}/s
┣⪼ <b>⏰️ Eᴛᴀ:</b> {4}
╰━━━━━━━━━━━━━━━➣"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> `7507446728upi@axl`
"""
