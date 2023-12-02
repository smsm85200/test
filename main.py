import time
import pyrogram
from pyrogram import Client
import requests
import os
from time import sleep
from pyrogram.errors import FloodWait, BadRequest
import re
tok = "6100362120:AAEASUEw65Kw4JvB4sHdL-eDMj09dqLi3WQ"
idown = "411414467" 
qq = 0
ok = requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=ʜᴀʟᴏ ᴋɪɴɢ')
app = Client("ACCC", api_id=26022994, api_hash="2e84a6b68bd6b5a79f46e8192668e0ea",bot_token="6100362120:AAEASUEw65Kw4JvB4sHdL-eDMj09dqLi3WQ" )
with app:
 while True:
    username = set(filter(None, open("user.txt").read().split("\n")))
    for user in username:
        qq += 1
        print(qq)
        url = f"https://t.me/{user}"
        sleep(0.1)
        req = requests.get(url)
        if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
                op = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=
ᵿˢᴱᴿ : [ @{user} ]''')
                with open("user.txt", "r") as file:
                    lines = file.readlines()
                with open("user.txt", "w") as file:
                    for line in lines:
                     if user not in line:
                        file.write(line)

  
