import json
import paho.mqtt.client as mqtt
import random
import time
import threading
import sys

mqttc = mqtt.Client("client1", clean_session=False)
mqttc.username_pw_set("xlrkyogu", "5Bnptg3tgPrW")
mqttc.connect("m13.cloudmqtt.com", 13091, 60)


def pub():
    mqttc.publish("sensor/temp", payload=random.normalvariate(30, 0.5), qos=0)
    threading.Timer(1, pub).start()

pub()