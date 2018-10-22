import plugins
import random
import os
import re
import glob
import requests
import urllib.request

def _initialise(bot):
    plugins.register_handler(_nsfw)


def _nsfw(bot, event, *args):
    """
    Posts a NSFW image
    """

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
