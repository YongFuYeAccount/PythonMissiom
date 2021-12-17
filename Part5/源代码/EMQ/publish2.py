# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 20:51:55 2021

@author: 86182
"""
#发布方
import json
import time
import paho.mqtt.client as mqtt
#连接成功时调用该函数
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))
#收到信息时调用该函数
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#连接mqtt broker
client.connect('127.0.0.1', 1883, 600) # 600为keepalive的时间间隔
client.loop_start() # 保持连接
print("#########################################")
time.sleep(1)
stus = {"Tempeature":30.1,"Humidity":40.2,"Hours":12, "Minutes":15}
res2 = json.dumps(stus)  # 先把字典转成json
#向 topic发送数据
client.publish('主题名', payload=res2, qos=0)
client.loop()