from sense_hat import SenseHat
from datetime import *
import json
import uuid
sense = SenseHat()


def json_string():
    temperature = round(sense.get_temperature(), 2)
    now = datetime.now()
    json_data = {"mac_address": (str(hex(uuid.getnode())))+"*",
                 "temperature": temperature,
                 "timestamp": now.strftime("%d-%m-%Y %H:%M:%S"),
                 "indoor": True,
                 "location": "Stue"}
    return json.dumps(json_data)
