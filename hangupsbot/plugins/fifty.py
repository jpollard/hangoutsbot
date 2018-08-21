import plugins
import asyncio
import urllib
import praw

def _initialise(bot):
    plugins.register_user_command(["fifty50"])

def fifty50(bot, event):
    """
    Get the top post from r/fiftyfifty

    /bot fifty50
    """

    r = praw.Reddit(user_agent='marvin')
    post = r.get_subreddit('linux').get_hot(limit='1')
    try:
        
        # list of games that have been found
        games = []
        # flag to mark if the next line contains the game name
        game = False
      
       
        with urllib.request.urlopen("http://fiftyfifty.reddit.com") as fp:
            html = fp.read()
        # decode the bytestream that urllib returns
        html = html.decode('utf-8')

        # split the html into lines to make it easy to iterate over
        lines = html.splitlines()
        for line in lines:    
            if game:
                # the line that contains the game title is
                # setup as x amout of spaces followed by 
                # <h2>title</h2>, strip removes the leading spaces
                # and [4:-5] returns the substring that doesnt contain 
                # the markup
                games.append(line.strip()[4:-5])
                # just got game title, reset.
                game = False

            # the following markup always procedes the game title on the website
            # thus it is used to indicate a title is the next line
            if "<div class='game-description'>" in line:
                game = True
           
        # starter string to hold the game names
        gameStr = "\n"
        # loop through the game list except the last two which are charities that 
        # humble bundle donates too
        for i in range(0, len(games) - 2):
            gameStr += "--" + games[i] + "\n"
      
        yield from bot.coro_send_message(event.conv, _(str(post)))
    except ValueError:
        yield from bot.coro_send_message(event.conv, _("Error getting games from the current Humble Bundle"))
