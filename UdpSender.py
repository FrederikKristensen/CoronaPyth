BROADCAST_TO_PORT = 7000
import time
from socket import *
from datetime import datetime

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
	data = "Id: 1, Name: Maskine 1, Temperature: 38.7, Location: Der, Date: " + str(datetime.now())
	s.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
	print(data)
	time.sleep(1)