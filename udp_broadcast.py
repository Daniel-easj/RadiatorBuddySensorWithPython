from socket import *
import time as t
from temp_sense import *

# Port to broadcast to
BROADCAST_TO_PORT = 11912

socket = socket(AF_INET, SOCK_DGRAM)
socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
# Infinite loop
while True:
    # Calls function from temp_sense.py
    data = json_string()
    # Sends the JSON object as bytes
    socket.sendto(bytes(data, "UTF-8"), ("<broadcast>", BROADCAST_TO_PORT))
    # Print the JSON object to console
    print(data)
    # Wait 30 seconds
    t.sleep(30)
