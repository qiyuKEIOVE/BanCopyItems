#导入模块#
import time

#循环执行#
def bcl_start(server, info):
        while True:
            #间隔三秒#
            time.sleep(3)
            #kill掉带箱子的骡子#
            server.execute('kill @e[type=minecraft:mule,nbt={ChestedHorse:1b,Tame:1b}]')
            #kill掉带箱子的驴#
            server.execute('kill @e[type=minecraft:donkey,nbt={ChestedHorse:1b,Tame:1b}]')
            #kill掉带箱子的行商羊驼#
            server.execute('kill @e[type=minecraft:trader_llama,nbt={ChestedHorse:1b,Tame:1b,Variant:0,Strength:1}]')
            #kill掉带箱子的羊驼#
            server.execute('kill @e[type=minecraft:llama,nbt={Tame:1b}]')