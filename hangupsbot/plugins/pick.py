import plugins
import asyncio
import random

def _initialise(bot):
    plugins.register_user_command(["pick"])

def pick(bot, event, *args):
    """
    Pick an item from a list of comma seperated items.

    /bot pick <i>item 1, item 2, ... , item N</i>
    """

    if not args:
        yield from bot.coro_send_message(event.conv, _("Usage: /bot pick <i>item 1, item 2, ... item N</i>"))
        return

    try:
        items = " "
        for arg in args:
             items += arg + " "
        
        itemList = items.split(',')

        yield from bot.coro_send_message(event.conv, _("<b>{}</b>").format(itemList[random.randint(0, len(itemList) - 1)]))
    except ValueError:
        yield from bot.coro_send_message(event.conv, _("I dont like any of those options, please try a new set."))

