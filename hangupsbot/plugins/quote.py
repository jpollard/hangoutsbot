import plugins
import asyncio
import random

def _initialise(bot):
    plugins.register_user_command(["qoute"])

def qoute(bot, event, *args):
    """
    Save a statement or display a randomly saved statement.

    /qoute <i>@username</i> - saves the last thing said by that person
    /qoute - prints a random qoute
    """

    # todo:
    # 1) get chat id
    # 2) create a file for that id
    # 3) parse qoute to see if it's alone or with a user id
    # 4) 
