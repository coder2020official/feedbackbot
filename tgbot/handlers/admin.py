from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
from telebot.asyncio_helper import ApiTelegramException
from telebot import logger


from tgbot.utils.extract_id import extract_id

async def admin_user(message: Message, bot: AsyncTeleBot):
    """
    Send the message to the admin.
    """
    user_id = extract_id(message.reply_to_message.text if message.reply_to_message.text else message.reply_to_message.caption)
    if not user_id:
        await bot.reply_to(
            message,
            text='Please reply to a user\'s message.'
        )
        return

    try:
        await bot.copy_message(
            chat_id=user_id,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )
    except ApiTelegramException as e:
        if 'blocked' in e.description:
            await bot.reply_to(
                message,
                text='User has blocked the bot.'
            )
        else:
            logger.error(e)