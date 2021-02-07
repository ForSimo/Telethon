# @iqthon c 2021
import asyncio
import io 
import telethon.sync
from telethon.tl.functions.users import GetFullUserRequest
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon import events, errors, functions, types
from userbot import ALIVE_NAME, LESS_SPAMMY
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "no name!"
PREV_REPLY_MESSAGE = {}


@command(pattern=r"\/start", incoming=True)
async def _(event):
    chat_id = event.from_id
    userid = event.sender_id
    if not pmpermit_sql.is_approved(chat_id):
        chat = await event.get_chat()
        if event.fwd_from:
            return
        if event.is_private:
         Nudas = (""
                  ""
                  ""
                  "")
         PM = ("- Welcome | @ForSimo."
            f""
            ""
            ""
            ""
            ""
            ""
            "")
         ONE = ("@ForSimo")
         TWO = ("@ForSimo")
         THREE = ("@ForSimo")
         FOUR = ("@ForSimo")
         LWARN = ("@ForSimo")
     
        async with borg.conversation(chat) as conv:
         await borg.send_message(chat, PM)
         chat_id = event.from_id
         response = await conv.get_response(chat)
         y = response.text
         if y == "1":
             await borg.send_message(chat, ONE)
             response = await conv.get_response(chat)
             await event.delete()
             if not response.text == "/start":
                 await response.delete()
                 await borg.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 await event.delete()
                 await response.delete()
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "2":
             await borg.send_message(chat, LWARN)
             response = await conv.get_response(chat)
             if not response.text == "/start":
                 await borg.send_message(chat, TWO)
                 await asyncio.sleep(3)
                 await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "3":
             await borg.send_message(chat, Nudas)
             response = await conv.get_response(chat)
             await event.delete()
             await response.delete()
             x = response.text
             if x == "1":
                 await borg.send_message(chat, "@ForSimo")
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, LWARN)
                     response = await conv.get_response(chat)
                     await event.delete()
                     await response.delete()
                     response = await conv.get_response(chat)
                     if not response.text == "/start":
                         await borg.send_message(chat, TWO)
                         await asyncio.sleep(3)
                         await event.client(functions.contacts.BlockRequest(chat_id))
             elif x == "2":
                 await borg.send_message(chat, "@ForSimo")
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, LWARN)
                     response = await conv.get_response(chat)
                     await event.delete()
                     await response.delete()
                     response = await conv.get_response(chat)
                     if not response.text == "/start":
                         await borg.send_message(chat, TWO)
                         await asyncio.sleep(3)
                         await event.client(functions.contacts.BlockRequest(chat_id))
             elif x == "3":
                 await borg.send_message(chat, "@ForSimo")
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, LWARN)
                     response = await conv.get_response(chat)
                     await event.delete()
                     await response.delete()
                     response = await conv.get_response(chat)
                     if not response.text == "/start":
                         await borg.send_message(chat, TWO)
                         await asyncio.sleep(3)
                         await event.client(functions.contacts.BlockRequest(chat_id))
             else:
                 await borg.send_message(chat, "@ForSimo")
                 response = await conv.get_response(chat)
                 if not response.text.startswith("/start"):
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "4":
             await borg.send_message(chat, FOUR)
             response = await conv.get_response(chat)
             await event.delete()
             await response.delete()
             if not response.text == "/start":
                 await borg.send_message(chat, LWARN)
                 await event.delete()
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "5":
             await borg.send_message(chat, FOUR)
             response = await conv.get_response(chat)
             if not response.text == "/start":
                 await borg.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         else:
             await borg.send_message(chat, "@ForSimo")
             response = await conv.get_response(chat)
             z = response.text
             if not z == "/start":
                 await borg.send_message(chat, LWARN)
                 await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))