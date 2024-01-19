import config

from pyrogram import enums
from pyrogram.types import InlineKeyboardButton


async def start_button(client):
    if not config.FORCE_SUB_:
        buttons = [
            [
                InlineKeyboardButton(text="Bantuan", callback_data="help"),
                InlineKeyboardButton(text="Tutup", callback_data="close"),
            ],
        ]
        return buttons

    dynamic_button = []
    current_row = []
    for key in config.FORCE_SUB_.keys():
        chat_id = config.FORCE_SUB_[key]
        chat_type = (await client.get_chat(chat_id)).type
        button_name = "Channel" if chat_type == enums.ChatType.CHANNEL else "Group"
        current_row.append(InlineKeyboardButton(text=f"{button_name}", url=getattr(client, f'invitelink{key}')))
        if len(current_row) == config.BUTTON_ROW:
            dynamic_button.append(current_row)
            current_row = []

    if current_row:
        dynamic_button.append(current_row)

    buttons = [
        [
            InlineKeyboardButton(text="Bantuan", callback_data="help"),
        ],
    ] + dynamic_button + [
        [InlineKeyboardButton(text="Tutup", callback_data="close")],
    ]
    return buttons


async def fsub_button(client, message):
    if config.FORCE_SUB_:
        dynamic_button = []
        current_row = []
        for key in config.FORCE_SUB_.keys():
            chat_id = config.FORCE_SUB_[key]
            chat_type = (await client.get_chat(chat_id)).type
            button_name = "Channel" if chat_type == enums.ChatType.CHANNEL else "Group"
            current_row.append(InlineKeyboardButton(text=f"{button_name}", url=getattr(client, f'invitelink{key}')))
            if len(current_row) == config.BUTTON_ROW:
                dynamic_button.append(current_row)
                current_row = []

        if current_row:
            dynamic_button.append(current_row)

        try:
            dynamic_button.append([
                InlineKeyboardButton(
                    text="Coba Lagi",
                    url=f"https://t.me/{client.username}?start={message.command[1]}",
                )
            ])
        except IndexError:
            pass

        return dynamic_button
