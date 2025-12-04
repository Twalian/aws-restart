#!/usr/bin/env python3 
"""
Comando di sopra serve per fare avviare il file da terminale senza bisogno di richiamare ogni volta python3.
Bisogna però dare anche al file il permesso di esecuzione da terminale con il comando " chmod +x nomefile.py " (possiamo verificare che ci sia la x con " ls -la "). Poi per lanciare il file da terminale si fa " ./nomefile.py "
"""

"""
Creare una lista server contenente: ["web01", "db01", "cache01"]
Aggiungere "backup01" alla fine
Inserire "proxy01" all'inizio (indice 0)
Rimuovere "cache01"
Stampare la lista finale e la sua lunghezza

Output Atteso:
['proxy01', 'web01', 'db01', 'backup01']
Numero server: 4 
"""

server_list : list[str] = ["web01", "db01", "cache01"]

server_list.append("backup01")

server_list.insert(0, "proxy01")

server_list.remove("cache01")

print(server_list)

print(len(server_list))