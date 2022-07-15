import asyncio

# filters
from tgbot.filters.admin_filter import AdminFilter
from tgbot.filters.message_length import MessageLengthFilter
from tgbot.filters.banned_filter import IsBannedFilter
from telebot.asyncio_filters import IsReplyFilter

# handlers
from tgbot.handlers.admin import admin_user
from tgbot.handlers.user_message import (
    user_text_message, user_media_message, message_is_too_long,
    user_is_banned
)
from tgbot.handlers.banning import ban_user, unban_user


# telebot
from telebot.async_telebot import AsyncTeleBot

# config
from tgbot import config


MEDIA = ['photo', 'video', 'audio', 'document', 'voice', 'animation']
TEXT_MEDIA = ['text', 'photo', 'video', 'audio', 'document', 'voice', 'animation']

bot = AsyncTeleBot(config.TOKEN)
def register_handlers():

    bot.register_message_handler(ban_user, admin=True, pass_bot=True, is_reply=True, commands=['ban'])

    bot.register_message_handler(unban_user, admin=True, pass_bot=True, is_reply=True, commands=['unban'])

    bot.register_message_handler(admin_user, admin=True, pass_bot=True, is_reply=True, content_types=TEXT_MEDIA)

    bot.register_message_handler(user_text_message, content_types=['text'], pass_bot=True, admin=False, length=config.MAX_MESSAGE_LENGTH, banned=False)

    bot.register_message_handler(user_media_message, content_types=MEDIA,pass_bot=True, admin=False, length=config.MAX_CAPTION, banned=False)

    bot.register_message_handler(message_is_too_long, content_types=TEXT_MEDIA, pass_bot=True, admin=False, banned=False)

    bot.register_message_handler(user_is_banned, content_types=TEXT_MEDIA, pass_bot=True, admin=False, banned=True)


register_handlers()



# custom filters
bot.add_custom_filter(AdminFilter())
bot.add_custom_filter(MessageLengthFilter())
bot.add_custom_filter(IsBannedFilter())
bot.add_custom_filter(IsReplyFilter())


async def run():
    await bot.polling(non_stop=True)


asyncio.run(run())
