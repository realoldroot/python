from wxpy import *

bot = Bot(cache_path=True)

friends_stat = bot.friends().stats()

friend_loc = []

# print(friends_stat['province'])

# 每一个元素是一个二元列表Counter，分别存储地区和人数信息
for province, count in friends_stat['province'].items():
    if province != "":
        friend_loc.append([province, count])

# 排序
friend_loc.sort(key=lambda x: x[1], reverse=True)

# 打印人数最多的10个地区
for item in friend_loc[:10]:
    print(item[0], item[1])

for sex, count in friends_stat["sex"].items():
    # 1代表MALE, 2代表FEMALE
    if sex == 1:
        print("男 %d" % count)
    elif sex == 2:
        print("女 %d" % count)
