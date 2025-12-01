# Esercizio numero pari
"""
def numero_pari(numero : int) -> bool :
        if numero%2 ==  0 :
                return True
        else :
                return False

numero : int = int(input("Inserisci un numero: "))

if numero_pari(numero) :
        print("Il numero inserito è pari")
else :
        print("Il numero inserito è dispari")
"""

# Esercizio calcolo sconto
"""
def calcola_sconto(prezzo : float, eta : int) -> float :

	sconto : int
	
	if eta < 18 :
		sconto = 20
	elif eta > 18 and eta >= 65 :
		sconto = 30
	else :
		sconto = 0

	return prezzo - (prezzo*sconto/100)

prezzo : float = float(input("Inserisci il prezzo dell'articolo: "))

eta : int = int(input("Inserisci la tua età: "))

print(f"Il prezzo finale è: {calcola_sconto(prezzo, eta)}€")
"""
# Esercizio valutazione temperatura
"""
def valuta_temperatura(gradi : float) -> str :

	if gradi < 15 :
		return "Fa freddo"
	elif gradi > 15 and gradi < 25 :
		return "Il clima è mite"
	elif gradi > 25 and gradi < 45 :
		return "Fa caldo"
	else :
		return "Mi dispiace ma il riscaldamento globale è fuori controllo, la fine è vicina!"


gradi : float = float(input("Quanti gradi ci sono? "))

print(valuta_temperatura(gradi))
"""
# Esercizio stampa tabellina
"""
def stampa_tabellina(numero : int) -> None :
	for n in range(1, 11) :
		print(numero*n)

numero : int = int(input("Inserisci un numero per visualizzare la tabellina: "))

stampa_tabellina(numero)
"""
# Disegna rettangolo

def disegna_rettangolo_intero(larghezza: int, altezza: int) -> None:
    for a in range(altezza):
        print("|" * larghezza)

larghezza: int = int(input("Inserisci la larghezza: "))
altezza: int = int(input("Inserisci l'altezza: "))

print(" ")

disegna_rettangolo_intero(larghezza, altezza)

print(" ")

def disegna_rettangolo_contorno(larghezza: int, altezza: int) -> None:
    print("|" * larghezza)
    for n in range(altezza - 2):
        print("|" + " " * (larghezza - 2) + "|")
    print("|" * larghezza)

disegna_rettangolo_contorno(larghezza, altezza)
