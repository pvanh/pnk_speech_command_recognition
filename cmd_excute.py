import paho.mqtt.client as mqtt
import json
# Define command code:
#  _________________
# |____D___|____I___|
# |________A________|
# |________O________|
# D: device code (4 bits)
device_code = {
   "Den":             0x1,
   "Tivi":            0x2,
   "Quat":            0x3,
   "Rem Cua":         0x4,
   "Thang May":       0x5,
   "Cua":             0x6
}
# I: identify code (4 bits)
id_code = {
    "Phong Khach":    0x1,
    "Phong Ngu":      0x2,
    "Phong Tam":      0x3,
    "Phong Bep":      0x4
}
# A: action code and optional (8 bits)
action_code = {
    "Bat":            0x01,
    "Tat":            0x02,
    "Sang Hon":       0x03,
    "Toi Hon":        0x04,
    "Mo Di":          0x05,
    "Keo Len":        0x06,
    "Keo Xuong":      0x07,
    "Len":            0x08,
    "Xuong":          0x09,
    "Dong":           0x0a,
    "Mo":             0x0b,
    "Chuyen":         0x0c,
    "Tang":           0x0d,
    "Giam":           0x0e
}

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


# ______________ MQTT ________________
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect_async("10.0.55.82", 1884, 60)
client.loop_start()

lamp1 = 'zigbee2mqtt/0x0017880103ac7e57/set'  # Den phong khach
lamp2 = 'zigbee2mqtt/0x0017880103b08db6/set'  # Den phong ngu
def send_cmd(code):
    print(hex(code))
    if code == 0x110100:
        # Bat den phong khach
        msg = {
            "state": "ON",
            "brightness": 150
        }
        client.publish(lamp1, json.dumps(msg))
    elif code == 0x110200:
        # Tat den phong khach
        msg = {
            "state": "OFF"
        }
        client.publish(lamp1, json.dumps(msg))
    elif code == 0x110300:
        # Den phong khach sang hon
        msg = {
            "state": "ON",
            "brightness": 255
        }
        client.publish(lamp1, json.dumps(msg))
    elif code == 0x110400:
        # Den phonog khach toi hon
        msg = {
            "state": "ON",
            "brightness": 50
        }
        client.publish(lamp1, json.dumps(msg))
    if code == 0x120100:
        # Bat den phong khach
        msg = {
            "state": "ON",
            "brightness": 150
        }
        client.publish(lamp2, json.dumps(msg))
    elif code == 0x120200:
        # Tat den phong khach
        msg = {
            "state": "OFF"
        }
        client.publish(lamp2, json.dumps(msg))
    elif code == 0x120300:
        # Den phong khach sang hon
        msg = {
            "state": "ON",
            "brightness": 255
        }
        client.publish(lamp2, json.dumps(msg))
    elif code == 0x120400:
        # Den phonog khach toi hon
        msg = {
            "state": "ON",
            "brightness": 50
        }
        client.publish(lamp2, json.dumps(msg))
    else:
        print("Command not found!")

    