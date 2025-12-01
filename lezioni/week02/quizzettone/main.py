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
    
def genera_feedback(is_corretta : bool) -> str:
    """
    Questa funzione restituisce una stringa con un feedback personalizzato, indicando all'utente se ha risposto correttamente o meno. Questa funzione viene eseguita solo se la funzione di validazione valida_scelta() restituisce true
    """
    if is_corretta == True:
        return "Risposta corretta!"
    else:
        return "Risposta sbagliata, ritenta!"
    
def is_risposta_esatta(scelta : str) -> bool :
    """
    Questa funzione restituisce True se la risposta dell'utente è corretta
    """
    if scelta.upper() == "A":
        return True
    else:
        return False

def mostra_feedback(messaggio: str) -> None:
    """
    Restituisce il feedback formattato nella maniera desiderata
    """
    symbol : str = "*"*30
    print(f"""
{symbol}
{messaggio}
{symbol}
          """)
    

def main() :

    is_risposta_corretta = False

    while True :
        mostra_domanda()    
        risposta_da_validare : str = raccogli_risposta()
        risposta_validata : bool = valida_scelta(risposta_da_validare)
    
        if risposta_validata == True : 
            is_risposta_corretta = is_risposta_esatta(risposta_da_validare)
            feedback = genera_feedback(is_risposta_corretta)
        else:
            feedback = "Inserisci solo la risposta tra le optioni elencate"

        mostra_feedback(feedback)

        if is_risposta_corretta == True :
            break
         

#Entry point del nostro programma
main()