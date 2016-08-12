import plugins
import random

def _initialise(bot):
    plugins.register_user_command('tell'):
    plugins.register_handler('_tell', 
