from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

tg = Client("my_account")

from pyrogram import Client

api_id = 12345
api_hash = "0123456789abcdef0123456789abcdef"

with Client("my_account", api_id, api_hash) as app:
    app.send_message("me", "Greetings from **Pyrogram**!")

@tg.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(
        text=Script.START_MSG,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Souce", url="https://github.com/vivek-tp/Tg-Bot"),
                    InlineKeyboardButton("Support", url="https://t.me/OpensourceTG")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )

# Copy This And Paste Here And Replace Commands.You Can Change This Bot To Any Bot By Adding More Codes eg: Renamer bot , Group Manager Bot, etc....
