from telebot import TeleBot
from telebot.types import InputFile
from telebot.types import Message
from db import db
def message_handle(message:Message,bot:TeleBot):
    print(message)
    if message.chat.id==741728025:
        chats=db.db().get_chats()
        print(chats)
        j=0
        k=0

        for chat1 in chats:
            chat=chat1[0]
            print(chat)
            if message.content_type=="text":
                text=message.text
                try:
                    bot.send_message(chat,text)
                    k=k+1
                except Exception as e:
                    print(e)
            
            if message.content_type=="video":
                try:
                    bot.send_video(chat,video=message.video.file_id,caption=message.caption)
                    k=k+1
                except Exception as e:
                    print(e)
            if message.content_type=="photo":
                try:
                    bot.send_photo(chat,photo=message.photo[0].file_id,caption=message.caption)

                    k=k+1
                except Exception as e:
                    print(e)

            j=j+1
        resulted=f"message sent to{k+1} people out of {j+1} people"
        bot.send_message(message.chat.id, resulted)
from db import db
def send_message(ChatjoinRequest,bot:TeleBot):
    file=open('message.txt')
    try:
        bot.approve_chat_join_request(ChatjoinRequest.chat,ChatjoinRequest.from_user)
    except Exception as e:
        print(e)
    print()
    try:
        result=db.db().insert(ChatjoinRequest.user_chat_id)
        print(result)
    except Exception as e:
        print(e)
    bot.send_video(chat_id=ChatjoinRequest.user_chat_id,caption=message1,video=InputFile('images/VID_20230219_122105_301.mp4'))