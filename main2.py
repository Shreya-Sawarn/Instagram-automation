#We first need to install the instabot module since it is not already present.
# Run the command 'pip install instabot' in the terminal to get instabot module.

from instabot import Bot

bot = Bot()

bot.login(username="your-username")

bot.upload_photo("photo-address",caption="Uploaded using python")
