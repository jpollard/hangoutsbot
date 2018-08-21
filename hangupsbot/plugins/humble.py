import plugins
import asyncio
import urllib

def _initialise(bot):
    plugins.register_user_command(["humble"])

def humble(bot, event):
    """
    Get the list of games from the current humble bundle.

    /bot humble
    """

    try:
        
        # list of games that have been found
        games = []
        # flag to mark if the next line contains the game name
        game = False
      
       
        with urllib.request.urlopen("http://www.humblebundle.com") as fp:
            html = fp.read()
        # decode the bytestream that urllib returns
        html = html.decode('utf-8')

        # split the html into lines to make it easy to iterate over
        lines = html.splitlines()
        for line in lines:    
            if game: 
                # a game name is coming up, but there are a couple of lines before the actual name.
                # so we're going to do nothing until we get the </div> tag.
                if '</div>' in line and 'More games coming soon!' not in line and '10% off Humble Monthly for New Subscribers' not in line and 'Soundtrack' not in line: 
                    # the line that contains the game title is
                    # setup as x amout of spaces followed by 
                    # </div>title, strip removes the leading spaces
                    # and [6:] returns the substring that doesnt contain 
                    # the markup
                    games.append(line.strip()[6:])
                    # just got game title, reset.
                    game = False
                if 'More games coming soon!' in line or '10% off Humble' in line or 'Soundtrack' in line:
                    game = False

            # the following markup always procedes the game title on the website
            # thus it is used to indicate a title is the next line
            if 'data-anchor-name="#box-art-human-name_anchor"' in line:
                game = True
           
        # starter string to hold the game names
        gameStr = "\n"
        # loop through the game list except the last two which are charities that 
        # humble bundle donates too
        for i in range(0, len(games) - 2):
            gameStr += "--" + games[i] + "\n"
      
        yield from bot.coro_send_message(event.conv, _("<b>Humble Bundle</b> {}").format(gameStr))
    except ValueError:
        yield from bot.coro_send_message(event.conv, _("Error getting games from the current Humble Bundle"))
