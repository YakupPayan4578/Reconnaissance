# --------------------------------------------Find the Target-------------------------------------

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Wrong Input! ")
	print("Correct example: python3 scanner.py <IP address> ")
	sys.exit()

print ("-" * 50)

print("Target scanning: " + target)
print("Scan started at " + str(datetime.now()))

print("-" * 50)

# -------------------------------------------Scanning Engine---------------------------------------

try:
	for port in range(1, 1025):
	
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1)
		
		result = s.connect_ex((target, port))

		if result == 0:
			print(f"Port {port} is OPEN")
	
		s.close()

# ------------------------------------------Error Control-----------------------------------------

except KeyboardInterrupt:
	print("\nProgram is ended by user! ")
	sys.exit()

except socket.gaierror:
	print("Hostname couldn't resolved! ")
	sys.exit()

except socket.error:
	print("Couldn't connect to server! ")
	sys.exit()


