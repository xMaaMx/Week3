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

#SRV_ADDRESS, virgolette lasciate vuote poichè li va inserito l'ip a livello di input
#SRV_PORT, numero della porta
#s.bind, in quest'esempio mettiamo in comunicazione l'ADDR e la porta
#s.listen , in ascolto un dispositivo (siamo noi ad indicarne il numero)
#connection..accept(), recuperiamo le info
#print, è la risposta testuale se la connessione è andata a buon fine
#if/elif , se il client invia 1 otteniamo le info sul OS in esecuzione(usiamo le funzione platform)
#se il client invia 2, il comando os.lisdir,restituisce  i file in una determinata directory
#con 0 il server chiude la connessione
