from telebot.asyncio_filters import SimpleCustomFilter
from telebot.types import Message


# list of banned users
from tgbot.banned_list import blocked_users




class IsBannedFilter(SimpleCustomFilter):
    """
    Filter to check whether the user is banned or not.
    """

    key = 'banned'

    async def check(self, message: Message):
        return message.chat.id in blocked_users