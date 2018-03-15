from wxpy import *

bot = Bot(cache_path=True)

# 定位群

group = bot.groups().search('学习交流群')[0]

foreman = group.search('工头')[0]


@bot.register(group)
def forward_boss_message(msg):
    if msg.member == foreman:
        msg.forward(bot.file_helper, prefix='发言')


# 堵塞线程
embed()
