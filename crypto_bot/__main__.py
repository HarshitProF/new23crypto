from . import bot
from .handlers import handle
def connect():
    bot.register_message_handler(handle.message_handle,pass_bot=True)
    bot.register_chat_join_request_handler(handle.send_message,pass_bot=True)
    bot.infinity_polling()
connect()