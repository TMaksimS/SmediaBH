"""Main app"""

import asyncio
import datetime

from pyrogram import Client
from pyrogram import filters
from pyrogram.types.messages_and_media.message import Message

from settings import API_HASH, API_ID, LOGER, FTIME, STIME, TTIME
from src.database.repository import RepoUsers
from src.database.schemas import User
from src.static.static import ResponseMSG, Commands

app = Client("my_account", API_ID, API_HASH)


@LOGER.catch
@app.on_message(filters=filters.private)
async def hear(
        client: Client,
        message: Message,
        ftime: float = FTIME,
        stime: float = STIME,
        ttime: float = TTIME
):
    """Head coroutine"""
    if message.chat.id == (await client.get_me()).id:
        if message.text == Commands.GET_ALL_NEW_USERS.value:
            res = await RepoUsers().get_all_new_users(
                date=datetime.datetime.now().date()
            )
            await client.send_message(
                chat_id=message.chat.id,
                text=f"{ResponseMSG.COMMAND1.value}{len(res)}"
            )
    else:
        if message.from_user.id == (await client.get_me()).id:
            pass
        else:
            user_id = message.from_user.id
            in_bd = await RepoUsers().get_user_by_user_id(user_id)
            if in_bd:
                pass
            else:
                data = User(
                    user_id=message.from_user.id,
                    f_name=message.from_user.first_name,
                    s_name=message.from_user.last_name,
                    user_name=message.from_user.username,
                    phone_number=message.from_user.phone_number,
                    date=message.date
                )
                added_in_db = await RepoUsers().add_user(data)
                LOGER.info(
                    f"New {user_id} has been added to DB {added_in_db}"
                )
                await asyncio.sleep(ftime)
                await client.send_message(
                    chat_id=message.chat.id,
                    text=ResponseMSG.GREETINGS.value
                )
                LOGER.info(
                    f"chat id {message.chat.id},"
                    f" message {ResponseMSG.GREETINGS.name}"
                )
                await asyncio.sleep(stime)
                await client.send_message(
                    chat_id=message.chat.id,
                    text=ResponseMSG.STUFF.value
                )
                await client.send_photo(
                    chat_id=message.chat.id,
                    photo="src/static/photos/SBH.png"
                )
                LOGER.info(
                    f"chat id {message.chat.id}"
                    f", message {ResponseMSG.STUFF.name}"
                )
                await asyncio.sleep(ttime)
                await client.send_message(
                    chat_id=message.chat.id,
                    text=ResponseMSG.AFTER_STUFF.value
                )
                LOGER.info(
                    f"chat id {message.chat.id}, "
                    f"message {ResponseMSG.AFTER_STUFF.name}"
                )


if __name__ == "__main__":
    app.run()
