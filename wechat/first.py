from wxpy import *

bot = Bot(cache_path=True)

# 向文件助手发信息
bot.file_helper.send("hello")
