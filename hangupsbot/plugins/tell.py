import plugins
import asyncio
import json

def _initialise(bot):
    plugins.register_user_command(["tell"])

def tell(bot, event, dly, *args):
    """
    

    /bot remindme <b>delay (minutes)</b> <i>Message</i>
    """

    if not args:
        yield from bot.coro_send_message(event.conv, _("Usage: /bot remindme <b>delay (minutes)</b> <i>Message</i>"))
        return

    try:
        numeral, delayTime, timeMeasure = timeMeasurement(dly)
        yield from bot.coro_send_message(event.conv, _("Private reminder for <b>{}</b> in {} {}.").format(event.user.full_name, numeral, timeMeasure))
        conv_1on1 = yield from bot.get_1to1(event.user.id_.chat_id)
        yield from asyncio.sleep(delayTime)
        yield from bot.coro_send_message(event.conv, _("<b>Reminder:</b> " + " ".join(str(x) for x in args)))
    except ValueError:
        yield from bot.coro_send_message(event.conv, _("Error creating reminder, invalid delay"))

