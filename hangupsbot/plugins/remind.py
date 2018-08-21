import plugins
import asyncio

SECOND = 1.0
MINUTE = 60.0 * SECOND
HOUR = 60.0 * MINUTE
DAY = 24.0 * HOUR
WEEK = 7.0 * DAY

def timedelay(dly):
    """
    Extract the time delay for the reminder and return the number of seconds
    """

    scale = dly[-1:].lower()
    if not scale.isdigit():
        time = dly[:-1]
    else:
        time = dly

    scaleWord = {
        's' : 'second(s)',
        'm' : 'minute(s)',
        'h' : 'hour(s)',
        'd' : 'day(s)',
        'w' : 'week(s)',
    }.get(scale, 'minute(s)')

    scaleTime = {
        'second(s)' : lambda time : float(time) * SECOND,
        'minute(s)' : lambda time : float(time) * MINUTE,
        'hour(s)'   : lambda time : float(time) * HOUR,
        'day(s)'    : lambda time : float(time) * DAY,
        'week(s)'   : lambda time : float(time) * WEEK,
    }[scaleWord](time)

    return scaleTime, time, scaleWord


def _initialise(bot):
    plugins.register_user_command(["remindme","remindall","saveme"])

def remindme(bot, event, dly, *args):
    """
    Posts a custom message to a 1on1 after a delay

    /bot remindme <b>delay{s,m,h,d,w}</b> <i>Message</i>
    """

    if not args:
        yield from bot.coro_send_message(event.conv, _("Usage: /bot remindme <b>delay{s,m,h,d,w}</b> <i>Message</i>"))
        return

    try:
        delayTime, delayScaledTime, delayTimeScale = timedelay(dly)
        yield from bot.coro_send_message(event.conv, _("Private reminder for <b>{}</b> in {} {}").format(event.user.full_name, delayScaledTime, delayTimeScale ))
        conv_1on1 = yield from bot.get_1to1(event.user.id_.chat_id)
        yield from asyncio.sleep(delayTime)
        yield from bot.coro_send_message(conv_1on1, _("<b>Reminder:</b> " + " ".join(str(x) for x in args)))
    except ValueError:
        yield from bot.coro_send_message(event.conv, _("Error creating reminder, invalid delay"))

def saveme(bot, event, dly, *args):
    """
    Posts a custom message to a 1on1 after a delay w/o the reminder part. Good for setting up an interruption if needed.

    /bot saveme <b>delay{s,m,h,d,w}</b> <i>Message</i>
    """

    if not args:
        yield from bot.coro_send_message(event.conv, _("Usage: /bot saveme <b>delay{s,m,h,d,w}</b> <i>Message</i>"))
        return

    try:
        delayTime, delayScaledTime, delayTimeScale = timedelay(dly)
        yield from bot.coro_send_message(event.conv, _("Text you in {}").format(delayScaledTime))
        conv_1on1 = yield from bot.get_1to1(event.user.id_.chat_id)
        yield from asyncio.sleep(delayTime)
        yield from bot.coro_send_message(event.conv, _(" ".join(str(x) for x in args)))
    except ValueError:
        yield from bot.coro_send_message(event.conv, _("Error creating reminder, invalid delay"))


def remindall(bot, event, dly, *args):
    """
    Posts a custom message to the chat after a delay

    /bot remindall <b>delay{s,m,h,d,w}</b> <i>Message</i>
    """

    if not args:
        yield from bot.coro_send_message(event.conv, _("Usage: /bot remindall <b>delay{s,m,h,d,w}</b> <i>Message</i>"))
        return

    try:
        delayTime, delayScaledTime, delayTimeScale = timedelay(dly)
        yield from bot.coro_send_message(event.conv, _("Public reminder in {} {}").format(delayScaledTime, delayTimeScale))
        yield from asyncio.sleep(delayTime)
        yield from bot.coro_send_message(event.conv, _("<b>Reminder:</b> " + " ".join(str(x) for x in args)))
    except ValueError:
        yield from bot.coro_send_message(event.conv, _("Error creating reminder, invalid delay"))
