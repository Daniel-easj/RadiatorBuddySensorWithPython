from sense_hat import SenseHat
from datetime import *
import json
import uuid

# Create an object of the sensehat
sense = SenseHat()

# Function to create a json string


def json_string():
    # Get temperature, round to 2 decimal points
    temperature = round(sense.get_temperature(), 2)
    # Get current time
    now = datetime.now()
    # Stuff everything into a JSON string
    # Get Mac-address(Id), convert to hexcode, then lastly to string
    json_data = {"Id": (str(hex(uuid.getnode()))),
                 "Temperature": temperature,
                 # Format current time to the folllowing format
                 "Timestamp": now.strftime("%d-%m-%Y %H:%M:%S"),
                 "inDoor": True,
                 "Location": "Stue"}
    # Return JSON object
    return json.dumps(json_data)
