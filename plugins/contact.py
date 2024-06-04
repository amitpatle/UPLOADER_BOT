from pyrogram import Client, filters
from plugins.config import Config
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["dev"]))
async def refer(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("</> ᴄᴏɴᴛᴇᴄᴛ ᴅᴇᴠ" ,url="t.me/dankdev") ]   ])
    await message.reply_text(f"**Dank Dev**",reply_markup=reply_markup,)
