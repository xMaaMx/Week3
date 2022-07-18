def perimetro (): #la funziona verrà eseguita richiamandola, senza uscire dal programma.
				      #l'utente in base al suo input numerico,selezionerà l'operazione da effettuare.
		print ("il programma calcola il perimetro di una figura geometrica"      )
		print ("""
		- Quadrato >>1
		- Rettangolo >>2
		- Cerchio >> 3"""   )

#inizio esercizio
		pigreco = 3.14 #creata una variabile per non ripetere il valore numerico del pigreco durante l'esercizio.(ottimizzazione del codice)

		print ("Inserire la scelta:" )
		scelta = int (input ("  "))
		if scelta == 1:
			print ("Hai selezionato il perimetro del Quadrato")
			lato = float(input("Inserisci il valore del lato del quadrato"     ))
			print ("il perimetro del quadrato, avente lato"    ,lato, "è:", lato *4)
		elif scelta == 2:
			print ("Hai selezionato il perimetro del rettangolo"      )
			base = float (input("Inserisci il valore della base"    ))
			altezza = float (input("Inserisci il valore della base"    ))
			print ("Il perimetro del Rettangolo, avente base", base, "e altezza", altezza, "è:",base *2 + 2*altezza)
		elif scelta == 3:
			print ("Hai selezionato il perimetro del raggio "     )
			raggio = float(input("Inserisci il valore del raggio"     ))
			perimetro =( (raggio*raggio)*pigreco)
			print("Il perimetro del cerchio é dato da  : "     ,raggio, "per " ,raggio, "per" ,pigreco," ed è uguale a:"   , perimetro)
		else:
			print ("Inserire una scelta valida"   )

perimetro();
#in questo modo richiamiamo la funzione iniziale del perimetro.
#RELAZIONE
#uso del float: non sapendo effettivamente se l'input dell'utente avrà un valore di numero intero o decimale,
#con il float ovviamo al problema.Poichè ci garantisce la scrittura di un valore con appunto i decimali.
#legenda: if = prima opzione di scelta / elif = ulteriori opzioni di scelta / else = se le condizioni  prima di esse non si dovessero avverare

