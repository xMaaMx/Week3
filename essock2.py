import socket, platform, os

SRV_ADDR = ""
SRV_PORT = 1234

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.bind (( SRV_ADDR, SRV_PORT))
s.listen (1)
connection, address = s.accept ()
print ( "client connected: ", address )
while 1:
	try:
		data = connection.recv (1024)
	except: continue
	if (data.decode('utf-8') == '1'):
		tosend = platform.platform() + " " + platform.machine ()
		connection.sendall(tosend.encode())
	elif(data.decode('utf-8') == '2'):
		data = connection.recv (1024)
		try:
			filelist = os.listdir (data.decode('utf-8'))
			tosend = " "
			for x in filelist:
				tosend += "," + x
		except:
			tosend = "wrong path"
		connection.sendall(tosend.encode())
	elif(data.decode('utf-8') == '0'):
		connection.close()
		connection, address = s.accept()

