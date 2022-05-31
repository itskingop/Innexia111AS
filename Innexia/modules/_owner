from Innexia.modules.buttons.adminhelp import *

__help__ = """
Admins Play Major Roles To Manage A Group, We Have Created Some Hack Command In Our Bot So It Will Help To Manage Group Easily Via Bot.
You Just Need To Give Commands To Bot And But Will Work for You. Click On Bellow Buttons & Get Detailed Information.
 ❍ /admins*:* list of admins in the chat
"""

__button__ = [ InlineKeyboardButton(text="Group", callback_data="innexiaadmin_"),
            InlineKeyboardButton(text="Promote", callback_data="innexiaadminpromote_"),
            InlineKeyboardButton(text="Purge", callback_data="innexiaadminpurge_"),

] 
__buttons__ = [InlineKeyboardButton(text="Ban", callback_data="innexiaadminban_"), 
              InlineKeyboardButton(text="Mute", callback_data="innexiaadminmute_"),
              InlineKeyboardButton(text="Warn", callback_data="innexiaadminwarn_"),
]

__mod_name__ = "Owner"

dispatcher.add_handler(admin_callback_handler)
dispatcher.add_handler(admin_ban_callback_handler)
dispatcher.add_handler(admin_purge_callback_handler)
dispatcher.add_handler(admin_promote_callback_handler)
dispatcher.add_handler(admin_warn_callback_handler)
dispatcher.add_handler(admin_mute_callback_handler)
