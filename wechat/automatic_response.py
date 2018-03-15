from wxpy import *

bot = Bot(cache_path=True)


# bot.file_helper.send("hello")


# 收到消息自动回复的功能。
@bot.register()
def print_message(msg):
    print(msg.text)
    return msg.text


# 进入Python命令行，让程序保持运行
embed()
