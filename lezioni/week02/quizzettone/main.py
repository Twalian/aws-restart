def mostra_domanda() -> None:
    """
    Questa funzione restituisce la domanda e le optioni di risposta
    """
    print(
"""
Chi parteciperà a Sanremo?"

A. Nayt
B. La Nina
C. Nilla Pizzi
D. Rocco Papaleo
""")
    
def raccogli_risposta() -> str:
    """
    Questa funzione si occupa solamente di restituire l'input dell'utente.
    Il controllo avverrà in un'altra funzione.
    """
    return input("Inserisci la tua scelta: ")

def valida_scelta(scelta: str) -> bool:
    """
    Questa funzione prende una un valore di tipo stringa e controlla che sia una delle possibili risposte.
    """
    scelta_tmp = scelta.upper()
    if scelta_tmp == "A" or scelta_tmp == "B" or scelta_tmp == "C" or scelta_tmp == "D" :
        return True
    else:
        return False
    
risposta_da_validare : str = raccogli_risposta()
risposta_validata : bool = valida_scelta(risposta_da_validare)
print(risposta_validata)