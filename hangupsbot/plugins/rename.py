"""
   A hangouts bot plugin that makes a comment anytime the hangouts name is changed.
"""
import plugins
import random
import asyncio
import appdirs
import os

def _initialise(bot):
    plugins.register_handler(_watch_rename, type='rename')
    return []

@asyncio.coroutine
def _watch_rename(bot, event, command):
    # Dont handle events caused by bot
    if event.user.is_self:
        return

    # Else say something clever
    else:
        return bot.coro_send_message(event.conv, _("{}").format(get_response()))

def get_response():
    # open the file that contains the responses to the renaming of  the hangout.
    dirs = appdirs.AppDirs('hangupsbot', 'hangupsbot')
    rename_responses_path = os.path.join(dirs.user_data_dir, 'rename.txt')
    renameFile = open(rename_responses_path)
    responses = []
    for line in renameFile:
        responses.append(line)

    renameFile.close()
    
    return responses[random.randint(0, len(responses) - 1)]
