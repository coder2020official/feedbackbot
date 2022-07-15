from telebot.asyncio_filters import AdvancedCustomFilter
from telebot.types import Message



class MessageLengthFilter(AdvancedCustomFilter):
    """
    Filter to check the length of the message.
    """

    key = 'length'

    async def check(self, message: Message, text):
        if message.text:
            return len(message.text) <= text
        return len(message.caption if message.caption else "") <= text
        