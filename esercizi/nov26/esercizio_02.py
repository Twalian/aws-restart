# ESERCIZIO 2

import sys
import psutil

print("Che statistica vuoi visualizzare?")

print("1 - Versione di Python")

print("2 - Percorso dell'eseguibile di Python")

print("3 - Spazio disco totale")

print("4 - Percentuale RAM usata")

print("5 - Numero di CPU logiche")

print("6 - Piattaforma sistema operativo")


answer = input("Inserisci la risposta (1-6): ")

if answer.isdigit() :
	if int(answer) == 1 :
		print("La versione di Python è " + (sys.version))
 		
	elif int(answer) == 2 :
		print("Il percorso dell'eseguibile di Python è " + (sys.executable))
	elif int(answer) == 3 :
		print("Lo spazio disco totale è " + str(psutil.disk_usage('/').total))
	elif int(answer) == 4 :
		print("La percentuale RAM usata è " + str(psutil.virtual_memory().percent))
	elif int(answer) == 5 :
		print("Il numero di CPU logiche è " + str(psutil.cpu_count()))
	elif int(answer) == 6 :
		print("La piattaforma del sistema operativo è " + (sys.platform))
	else : 
		print("Inserisci un numero compreso tra 1 e 6")
else :
	print("Inserisci solo valori numerici (1-6)")
