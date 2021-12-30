"""Get Detailed info about any message
Syntax: .json"""

import os
from pyrogram import Client, filters


@Client.on_message(filters.command("json"))
async def jsonify(_, message):
    the_real_message = None
    reply_to_id = None

    if message.reply_to_message:
        the_real_message = message.reply_to_message
    else:
        the_real_message = message

    try:
        await message.reply_text(f"<code>{the_real_message}</code>")
    except Exception as e:
        with open("json.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(the_real_message))
        await message.reply_document(
            document="json.text",
            caption=str(e),
            disable_notification=True,
            reply_to_message_id=reply_to_id
        )
        os.remove("json.text")

__help__ = """
 - /json Get Detailed info about any message
 
 You Can Get Entire Details About Any Message Such As Text, Media, Stickers, Photos etc..
 
 Very Simple Steps:-
    1. Send Your Message To Me.
    2. Replay To Your Message By Using Command /json.
    
    Done.... 
"""

__mod_name__ = "Json"