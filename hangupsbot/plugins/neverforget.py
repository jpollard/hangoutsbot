import plugins
import random
import os
import re
import glob

def _initialise(bot):
    plugins.register_handler(_neverforget)


def _neverforget(bot, event, *args):
    """
    Never forget the tragedy that was Brian's and DJ's love

    /bot neverforget
    """

    text = event.text.lower()
    if re.search(r'#neverforget', text):
        try:
            msgSarah = ["Sarah's first beer.",
                        "So much for that pure and innocent persona...",
                        "Look! It's shawnzies cuddle buddy",
                        "OH. MY. GOD.",
                        "The moment when you realize you've hit rock bottom.",
                        "This is the same person that 85% of the guys at Ts were obsessed with.",
                        "Still looks hot."
                       ]
            msgBrian = ["Derek and Brian sitting in a tree...",
                        "Awww, Derek looks so nice for Brian",
                        "The night DJ lost his virginity",
                        "If you look close enough you can see a tear running down DJ's face",
                        "The horrible gimp job that Jacob loves so much",
                        "The number of fingers DJ put in Brians butt",
                        "The number of STD's Brians about to give DJ "]
        
            msgMonkey = ["Thats one ugly monkey,",
                         "At least it's not the DJ rape picture", 
                         "Ron Jeremy and his pleasure monkey", 
                         "Aw gross! ", 
                         "All you can eat wing night, and danyelle ate 6...", 
                         "Remember when shawn broke his car so he didnt have to come?", 
                         "The beginning of planet of the apes."]

            msgPumpkin = ["FUCK YOU DEREK!",
                          "Awww, sooo cute!",
                          "I miss the hallway computer",
                          "Classic DJ",
                          "Now the pumpkin fits inside of DJ",
                          " ",
                          " "]
 
            msgDj = ["", "", "", "", "", "", ""]
            msg = [msgSarah, msgBrian, msgMonkey, msgPumpkin, msgDj]

            sarah = "/home/snowman/.local/share/pics/sarah.jpg"
            brian = "/home/snowman/.local/share/pics/brian.jpg"
            monkey = "/home/snowman/.local/share/pics/monkey.jpg"
            pumpkin = "/home/snowman/.local/share/pics/pumpkin.jpg"
            dj = "/home/snowman/.local/share/pics/dj.jpg"

            images = [sarah, brian, monkey, pumpkin, dj]
            size = len(images) - 1
            num = random.randint(0, size)
            image = open(images[num], "rb")
            filename=os.path.basename(images[num])
      
            photo_id = yield from bot._client.upload_image(image, filename=filename)
            yield from bot.coro_send_message(event.conv.id_, msg[num][random.randint(0,6)] , image_id=photo_id)
            image.close()

        except ValueError:
            yield from bot.coro_send_message(event.conv, _("Error reading image"))
            logger.print(ValueError)

    elif re.search(r'#throwback', text):
        files = glob.glob("/home/snowman/.local/share/hangout_pics/*")
        size = len(files) - 1
        num = random.randint(0, size)
        image = open(files[num], "rb")
        filename = os.path.basename(files[num])

        photo_id = yield from bot._client.upload_image(image, filename=filename)
        yield from bot.coro_send_message(event.conv.id_, message="#throwback", image_id=photo_id)
        image.close()
