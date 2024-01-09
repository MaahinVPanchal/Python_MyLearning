from instabot import Bot
bot = Bot()
bot.login(username="dhoni_maahin",password='777')
bot.follow('dhoni_maahin')
bot.upload_photo("E:/LenovoEdrive/Python-Programming/python_project/Instagram/dhoni.png",caption="python")
bot.unfollow('dhoni_maahin') 
bot.send_message("I am teaching python",["maahi","maahin"])
followers = bot.get_user_followers("dhoni_maahin")
for follower in followers:
    print(bot.get_user_info(follower))
following = bot.get_user_following("dhoni_maahin")
for Following in following:
    print(bot.get_user_info(Following))