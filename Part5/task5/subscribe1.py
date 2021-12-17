# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 21:10:45 2021

@author: 86182
"""
#消息订阅
import random

from paho.mqtt import client as mqtt_client

import WdataSTR as wd

#设置 MQTT Broker 连接地址，端口以及 topic，同时我们调用 Python random.randint 函数随机生成 MQTT 客户端 id。
broker = 'broker.emqx.io'
port = 1883
topic = "/python/mqtt1"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'


#编写连接回调函数
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")#连接成功
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):#该函数将在客户端从 MQTT Broker 收到消息后被调用，
                                          #在该函数中我们将打印出订阅的 topic 名称以及接收到的消息内容。
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        wd.WdataSTR(msg.payload.decode())#将数据保存到文本
        
    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()