from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from tgbot.banned_list import blocked_users
from tgbot.utils.extract_id import extract_id


async def ban_user(message: Message, bot: AsyncTeleBot):
    """
    Bans the user.
    """
    user_id = extract_id(message.reply_to_message.caption if message.reply_to_message.caption else message.reply_to_message.text)
    if user_id not in blocked_users:
        blocked_users.append(user_id)

        await bot.reply_to(
            message,
            text='Banned the user.'
        )

        await bot.send_message(
            chat_id=user_id,
            text='You have been banned by the admin.'
        )
        return
    await bot.reply_to(
        message,
        text='User is already banned.'
    )

async def unban_user(message: Message, bot: AsyncTeleBot):
    """
    Unbans the user.
    """
    
    user_id = extract_id(message.reply_to_message.caption if message.reply_to_message.caption else message.reply_to_message.text)

    if user_id in blocked_users:
        blocked_users.remove(user_id)
        await bot.reply_to(
            message,
            text='Unbanned the user.'
        )
        await bot.send_message(
            chat_id=user_id,
            text='You have been unbanned by the admin.'
        )
        return
    await bot.reply_to(
        message,
        text='The requested user is not banned. Unbanning was skipped.'
    )