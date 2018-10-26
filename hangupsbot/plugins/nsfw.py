import plugins
import random
import os
import re
import glob
import requests
import urllib.request

def _initialise(bot):
    plugins.register_handler(_nsfw)
    plugins.register_admin_command("enable_nsfw")

def enable_nsfw(bot, event, *args):
    """
    Eable the #nsfw keyword
    """
    conv_id_list = [event.conv_id]

    # If no memory entry exists, make one
    if not bot.memory.exists(["conversations"]):
        bot.memory.set_by_path(["conversations"], {})

    for conv in conv_id_list:
        if not bot.memory.exists(["conversations"]):
            bot.memory.set_by_path(["conversations", conv], {})

    if bot.memory.exists(["conversations", event.conv_id, "nsfw"]):
        new_nsfw = (bot.memory.get_by_path(["conversations", event.conv_id, "nsfw"]) + 1)%2
    else:
        new_nsfw = 1

    bot.memory.set_by_path(["conversations", conv, "nsfw"], new_nsfw)

    bot.memory.save()

    yield from bot.coro_send_message(conv, "NSFW settings updated")

def _nsfw(bot, event, *args):
    """
    Posts a NSFW image
    """
    memory_nsfw_path = ["conversations", event.conv_id, "nsfw"]

    memory_nsfw_status = False
    if bot.memory.exists(memory_nsfw_path):
        memory_nsfw_status = bot.memory.get_by_path(memory_nsfw_path)

    if memory_nsfw_status:
        text = event.text.lower()
        num = random.randint(0,49)

        if re.search(r'#nsfw', text):
            imageLocation = '/home/snowman/.local/share/hangupsbot/.nsfw.jpg'
            try:
                url = 'https://www.reddit.com/r/nsfw/.json?limit=1'
                headers = {'User-Agent': 'python:com.happyrobotics.marvin:v0.01 (by /u/emulator3)'}

                r = requests.get('https://www.reddit.com/r/nsfw/hot/.json?limit=50', headers=headers)
                     if 200 == r.status_code:
                         postJson = r.json()
                         link = postJson.get('data').get('children')[num].get('data').get('url')
                         urllib.request.urlretrieve(link, '/home/snowman/.local/share/hangoutsbot/nsfw.jpg')

                         filename=os.path.basename(imageLocation)

                         photo_id = yield from bot._client.upload_image(image, filename=filename)
                         yield from bot.coro_send_message(event.conv.id_, 'yep' , image_id=photo_id)
                         image.close()

            except ValueError:
                yield from bot.coro_send_message(event.conv, _("Error reading image"))
                logger.print(ValueError)
