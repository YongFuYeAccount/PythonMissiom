# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 17:06:59 2021

@author: 86182
"""


#消息发布
import random
import time
import socket

from paho.mqtt import client as mqtt_client#导入 Paho MQTT客户端

#设置 MQTT Broker 连接地址，端口以及 topic，同时我们调用 Python random.randint 函数随机生成 MQTT 客户端 id。
broker = 'broker.emqx.io'
port = 1883 #TCP的端口号
topic = "/python/mqtt1"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'#随机生成客户端的id

#编写连接回调函数
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:#连接成功
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)#连接失败

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

#发布消息
def publish(client):#每秒调用 MQTT 客户端 publish 函数向 /python/mqtt 主题发送消息。
    msg_count = 0
    while True:
        time.sleep(1)
        #msg = f"messages: {msg_count}"
        msg = mes
        result = client.publish(topic, msg)
        print(msg_count)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        break
        


def SERVER1():
    s = socket.socket()
    host = socket.gethostname()
    port = 9009
    s.bind((host, port))

    s.listen(5)
    while True:
        print('等待用户连接……')
        c, addr = s.accept()        #阻塞进程，等待客户端接入
        print('用户已连接 address:{}\n服务器:请发送数据'.format(addr))
        c.send(bytes("请问需要什么帮助?",encoding="utf-8"))
        while True:
            mes = str(c.recv(1024),encoding = "utf-8")
            print("客户端：{}".format(mes))
            #mes = input("服务器：")
            #c.send(bytes(mes,encoding="utf-8"))
            publish(a)  
            
        c.close()
    return mes #返回的类型是字符串（str）

def run():#运行函数
    client = connect_mqtt()
    client.loop_start()
    SERVER1()
    #publish(client)



if __name__ == '__main__':
    run()















