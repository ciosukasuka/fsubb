# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram import Client, types


def start_button(c: Client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                types.InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                types.InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                types.InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=c.invitelink2),
            ],
            [
                types.InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                types.InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                types.InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=c.invitelink),
            ],
            [
                types.InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                types.InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                types.InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ],
            [
                types.InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=c.invitelink),
                types.InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=c.invitelink2),
            ],
            [
                types.InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons


def fsub_button(c: Client, m: types.Message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                types.InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=c.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    types.InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{c.username}?start={m.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                types.InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=c.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    types.InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{c.username}?start={m.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                types.InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=c.invitelink),
                types.InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=c.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    types.InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{c.username}?start={m.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
