"""
def blocco_1(nome : str) -> None:
	print("="*40)
	print(f"Ciao {nome}")
	print("="*40)

utente = input("Come ti chiami? ")

blocco_1(utente)



def blocco_2(nome : str) -> str:
	return f"Ciao {nome}"

utente : str = input("Come ti chiami? ")

#print(blocco_2(utente))

saluto : str = blocco_2(utente)

print(saluto)

"""

utente : str = input("Come ti chiami? ")

def stampa_divisore(simbolo : str, valore: int) -> str :
	return(f"{simbolo}"*valore)

def saluto(nome) -> str :
	simbolo : str = input("Scegli un simbolo: ")
	numero : int = int(input("Scegli un numero: "))
	divisore = stampa_divisore(simbolo, numero)
	return f"{divisore}\nCiao {nome}\n{divisore}"

print(saluto(utente))
