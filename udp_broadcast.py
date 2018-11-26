from socket import *
import time as t
from temp_sense import *

BROADCAST_TO_PORT = 11912

socket = socket(AF_INET, SOCK_DGRAM)
# s.bind(('', 14593))     # (ip, port)
# no explicit bind: will bind to default IP + random port
socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
    data = json_string()
    socket.sendto(bytes(data, "UTF-8"), ("<broadcast>", BROADCAST_TO_PORT))
    print(data)
    t.sleep(30)
