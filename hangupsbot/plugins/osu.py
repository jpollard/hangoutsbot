import plugins
import re

def _initialise(bot):
    plugins.register_handler(_scan_for_oh)

def _scan_for_oh(bot, event, command):
    ohtext = event.text.lower()
    if re.search(r'^oh |^o h |^o-h', ohtext):
        yield from bot.coro_send_message(event.conv, _("I-O!"))

