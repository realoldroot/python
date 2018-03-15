# -*- coding: utf-8 -*-
from wxpy import *

bot = Bot(cache_path=False)

tuling = Tuling(api_key='ef7693f7d4f043bf894a8dbf757b15aa')

my_friend = bot.friends()


# 自动回复朋友信息
@bot.register(my_friend)
def forward_message(msg):
    print(msg)
    return tuling.reply_text(msg)


embed()
