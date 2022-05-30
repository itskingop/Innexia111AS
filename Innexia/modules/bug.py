from datetime import datetime

from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    Message,
)

from Innexia import pbot as pgram, OWNER_ID, OWNER_USERNAME, SUPPORT_CHAT
from Innexia.utils.errors import capture_err


def content(msg: Message) -> [None, str]:
    text_to_return = msg.text

    if msg.text is None:
        return None
    if " " not in text_to_return:
        return None
    try:
        return msg.text.split(None, 1)[1]
    except IndexError:
        return None


@pgram.on_message(filters.command("bug"))
@capture_err
async def bug(_, msg: Message):
    if msg.chat.username:
        chat_username = (f"@{msg.chat.username} / `{msg.chat.id}`")
    else:
        chat_username = (f"Private Group / `{msg.chat.id}`")

    bugs = content(msg)
    user_id = msg.from_user.id
    mention = (
        f"[{msg.from_user.first_name}](tg://user?id={str(msg.from_user.id)}"
        + ")"
    )

    datetimes_fmt = "%d-%m-%Y"
    datetimes = datetime.utcnow().strftime(datetimes_fmt)

    bug_report = f"""
**#BUG : ** **@{OWNER_USERNAME}**
**ғʀᴏᴍ ᴜsᴇʀ : ** **{mention}**
**ᴜsᴇʀ ɪᴅ : ** **{user_id}**
**ɢʀᴏᴜᴘ : ** **{chat_username}**
**ʙᴜɢ ʀᴇᴘᴏʀᴛ : ** **{bugs}**
**ᴇᴠᴇɴᴛ sᴛᴀᴍᴘ : ** **{datetimes}**"""


    if msg.chat.type == "private":
        await msg.reply_text(" 🚫 <b>ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs.</b>")
        return

    if user_id == OWNER_ID:
        if bugs:
            await msg.reply_text(
                "🚫 <b>ʜᴏᴡ ᴄᴀɴ ʙᴇ ᴏᴡɴᴇʀ ʙᴏᴛ ʀᴇᴘᴏʀᴛɪɴɢ ʙᴜɢ??</b>",
            )
            return
        await msg.reply_text(
            "ᴏᴡɴᴇʀ ɴᴏᴏʙ ʜᴀɪ!"
        )
    elif bugs:
        await msg.reply_text(
            f"<b>ʙᴜɢ ʀᴇᴘᴏʀᴛ : {bugs}</b>\n\n"
            "✅ <b>ᴛʜᴇ ʙᴜɢ ᴡᴀs sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇᴘᴏʀᴛᴇᴅ ᴛᴏ ᴛʜᴇ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ!</b>",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Cʟᴏsᴇ ", callback_data="close_reply")]]
            ),
        )

        thumb = "https://te.legra.ph/file/c1c3ff192dce27b35d5fb.png"

        await pgram.send_photo(
            SUPPORT_CHAT,
            photo=thumb,
            caption=f"{bug_report}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "➡ Vɪᴇᴡ Bᴜɢ", url=f"{msg.link}")
                    ],
                    [
                        InlineKeyboardButton(
                            "❌ Cʟᴏsᴇ", callback_data="close_send_photo")
                    ]
                ]
            )
        )
    else:
        await msg.reply_text("❎ <b>ɴᴏ ʙᴜɢ ᴛᴏ ʀᴇᴘᴏʀᴛ ғᴏᴜɴᴅ ᴛɪʟʟ ɴᴏᴡ!</b>")


@pgram.on_callback_query(filters.regex("close_reply"))
async def close_reply(msg, CallbackQuery):
    await CallbackQuery.message.delete()

@pgram.on_callback_query(filters.regex("close_send_photo"))
async def close_send_photo(_, CallbackQuery):
    is_Admin = await pgram.get_chat_member(
        CallbackQuery.message.chat.id, CallbackQuery.from_user.id
    )
    if not is_Admin.can_delete_messages:
        return await CallbackQuery.answer(
            "ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴄʟᴏsᴇ ᴛʜɪs.", show_alert=True
        )
    await CallbackQuery.message.delete()


__mod_name__ = "Bug"
