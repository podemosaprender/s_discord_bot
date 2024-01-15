# s_discord_bot
Discord Bot study: what's posible? how?

OjO! Los ToS prohiben scraping!

FROM: https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal

~~~
python -mvenv xenvbot
. xenvbot/bin/activate
pip install discord

export DISCORD_TOKEN="the token you got from creating the bot on discord"
python src/10commands.py
~~~

1. Go to https://discord.com/developers/applications
2. Create an application for your bot
3. Go to the "Bot" tab for your app, "reset token" if none is shown
4. Copy the token to a **SAFE, SECRET** place
5. Go to the "OAuth2" tab in the menu on the left sidebar, then "URL Generator", toggle required permisions and copy the URL at the bottom
6. Paste the URL in your browser, select for which server to activate the bot
7. Edit e.g. hardcoded channel on `10with_commands.py` XXX:get from connection?
8. Run your bot
~~~
export DISCORD_TOKEN="token you saved on step 4"
python src/10commands.py
~~~
 
