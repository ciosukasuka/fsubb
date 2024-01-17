# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

from bot import Bot
from config import OWNER
from Data import Data
from pyrogram import errors, types, filters


@Bot.on_message(filters.private & filters.incoming & filters.command("about"))
async def _about(client: Bot, msg: types.Message):
    await client.send_message(
        msg.chat.id,
        Data.ABOUT.format(client.username, OWNER),
        disable_web_page_preview=True,
        reply_markup=types.InlineKeyboardMarkup(Data.mbuttons),
    )


@Bot.on_message(filters.private & filters.incoming & filters.command("help"))
async def _help(client: Bot, msg: types.Message):
    await client.send_message(
        msg.chat.id,
        "<b>Cara Menggunakan Bot ini</b>\n" + Data.HELP,
        disable_web_page_preview=True,
        reply_markup=types.InlineKeyboardMarkup(Data.buttons),
    )


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: types.CallbackQuery):
    data = query.data
    if data == "about":
        try:
            await query.message.edit_text(
                text=Data.ABOUT.format(client.username, OWNER),
                disable_web_page_preview=True,
                reply_markup=types.InlineKeyboardMarkup(Data.mbuttons),
            )
        except errors.MessageNotModified:
            pass
    elif data == "help":
        try:
            await query.message.edit_text(
                text="<b>Cara Menggunakan Bot ini</b>\n" + Data.HELP,
                disable_web_page_preview=True,
                reply_markup=types.InlineKeyboardMarkup(Data.buttons),
            )
        except errors.MessageNotModified:
            pass
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except Exception:
            pass
