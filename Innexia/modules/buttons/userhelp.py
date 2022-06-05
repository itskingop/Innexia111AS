from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown
from Innexia.__main__ import *


# Buttons Function for admin module
 
 
def innexia_user_callback(update, context):
    query = update.callback_query
    if query.data == "innexiauser_":
        query.message.edit_text(
            text="""Here is the help for the *Horoscope* module:
  ❍ /hs <sign> 
  Usage: it will show horoscope of daily of your sign.
  List of all signs - aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius and pisces.
        """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_back")
                 ]
                ]
            ),
        )
def innexia_user_afk_callback(update, context):
    query = update.callback_query
    if query.data == "innexiauserafk_":
        query.message.edit_text(
            text=""" *Away from group*
  ❍ /afk <reason>: mark yourself as AFK(away from keyboard).
  ❍ brb <reason>: same as the afk command - but not a command.
  When marked as AFK, any mentions will be replied to with a message to say you're not available!""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_back")
                 ]
                ]
            ),
        )
def innexia_user_about_callback(update, context):
    query = update.callback_query
    if query.data == "innexiauserabout_":
        query.message.edit_text(
            text=""" *Self addded information:*
  ❍ /setme <text>: will set your info
  ❍ /me: will get your or another user's info.
  Examples: 💡
  ➩ /setme I am a wolf.
  ➩ /me @username(defaults to yours if no user specified)
   *Information others add on you:*
  ❍ /bio: will get your or another user's bio. This cannot be set by yourself.
  ❍ /setbio <text>: while replying, will save another user's bio 
  Examples: 💡
  ➩ /bio @username(defaults to yours if not specified).
  ➩ /setbio This user is a wolf (reply to the user)
              """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_back")
                 ]
                ]
            ),
        ) 
def innexia_user_info_callback(update, context):
    query = update.callback_query
    if query.data == "innexiauserinfo_":
        query.message.edit_text(
            text=""" *Overall Information about you:*
  ❍ /info: get information about a user.
   *GET ID:*
  ❍ /id: get the current group id. If used by replying to a message, gets that user's id.
  ❍ /gifid: reply to a gif to me to tell you its file ID.
               """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_back")
                 ]
                ]
            ),
        ) 
def innexia_user_extra_callback(update, context):
    query = update.callback_query
    if query.data == "innexiauserextra_":
        query.message.edit_text(
            text=""" innexia have some extra tool for users, they can use also them*:*
    *Poto* - You can download anyuser profile pic via this tool
  ❍ /poto - reply to user for download all profile picsF
  ❍ /poto 1 - download specific number of pic, it will download first pic of user
    *Fake iDentity* - get easily fake identiy of user
  ❍ /fakegen - generate fake id 
  ❍ /picgen - generate fake pic
        """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_back")
                 ]
                ]
            ),
        )


# Handlers start from here 

user_callback_handler = CallbackQueryHandler(innexia_user_callback, pattern=r"innexiauser_", run_async=True)
user_afk_callback_handler = CallbackQueryHandler(innexia_user_afk_callback, pattern=r"innexiauserafk_", run_async=True)
user_about_callback_handler = CallbackQueryHandler(innexia_user_about_callback, pattern=r"innexiauserabout_", run_async=True)
user_info_callback_handler = CallbackQueryHandler(innexia_user_info_callback, pattern=r"innexiauserinfo_", run_async=True)
user_extra_callback_handler = CallbackQueryHandler(innexia_user_extra_callback, pattern=r"innexiauserextra_", run_async=True)

