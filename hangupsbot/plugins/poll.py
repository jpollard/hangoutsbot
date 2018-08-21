import plugins
import asyncio
import random

def _initialise(bot):
    plugins.register_user_command(["poll"])

def poll(bot, event, *args):
    """
    Poll the individuals of a hangout. Polls are anonymous

    /poll <b>"Question"</b> <i>"choice 1"</i> <i>"choice 2"</i> ... <i>"choice 9"</i> <i>"choice"</i>
    """

    if not args:
        yield from bot.coro_send_message(event.conv, _("Usage: /bot pollard <question> <answers1, answers2>"))
        return

    try:
Get
        # Things to implement
        # 1) Get the people in the current hangout.
        # 2) Split the poll up

        items = " "
        for arg in args:
             items += arg + " "

        itemList = items.split(',')

        yield from bot.coro_send_message(event.conv, _("Poll sent. To see the current results simply ask"))
    except ValueError:
        yield from bot.coro_send_message(event.conv, _("I dont like any of those options, please try a new set."))
