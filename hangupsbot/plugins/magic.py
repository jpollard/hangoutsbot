import plugins
import asyncio
import random



def _initialise(bot):
    plugins.register_user_command(["magic"])

def magic(bot, event, *args):
    """
    Magic 8 Ball for hangouts

    /bot magic <i>Question</i>
    """

    if not args:
        yield from bot.coro_send_message(event.conv, _("Usage: /bot magic <i>Question</i>"))
        return

    responses = ["It is certain",
                 "It is decidedly so",
                 "Without a doubt",
                 "Yes, definitely",
                 "You may rely on it",
                 "As I see it, yes",
                 "Most likely",
                 "Outlook good",
                 "Yes",
                 "Signs point to yes",
                 "Reply hazy, try again",
                 "Ask again later",
                 "Better not tell you yet",
                 "Cannot predict",
                 "Concentrate and ask again",
                 "Don't count on it",
                 "My reply is no",
                 "My sources say no",
                 "Outlook not so good",
                 "Very doubtful",
                 "I'm not going to answer because you're a moron for even asking.",
                 "I can't answer that right now, I just found a picture of DJ sitting on a tentacle...",
                 "Only if Shawn stops being a little bitch.",
                 
                ]



    yield from bot.coro_send_message(event.conv, _("{}").format(responses[random.randint(0,19)]))
