import sys

def leggi_file(file_path : str) -> str :
    with open(file_path, "r") as file :
        content = file.read()
        return content
    #print(len(content))

def estrai_index(content : str) -> int :
    return content.index("£")
   
def estrai_domanda(content : str, index : int) -> str:
    return content[0:index]

def estrai_risposta(content : str, index : int) -> str:
    return content[index+1:]
    
def mostra_domanda(domanda : str) -> None:
    """
    Questa funzione restituisce la domanda e le optioni di risposta
    """
    print(domanda)
    
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
        return "Risposta sbagliata!"
    
def is_risposta_esatta(scelta : str, risposta_esatta : str) -> bool :
    """
    Questa funzione restituisce True se la risposta dell'utente è corretta
    """
    if scelta.upper() == risposta_esatta:
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

def estrai_lista_domande(file_path : str) -> list[str] :
    lista_domande : list[str] = []
    with open("domande.txt", "r") as f:
        for i in f :
            lista_domande.append(i.strip())
    return lista_domande


def genera_statistiche(risultato_finale : list[dict[str, str |bool ]]) -> dict[str, int] :
    statistica : dict[str, int] = {}

    risposte_esatte : int = 0
    risposte_sbagliate : int = 0

    for i in risultato_finale:
        

        if i["risposta_corretta"] :
            risposte_esatte += 1
        else:
            risposte_sbagliate += 1

    statistica["risposte_esatte"] = risposte_esatte
    statistica["risposte_errate"] = risposte_sbagliate

    return statistica

def main()  :

    lista_domande: list[str] = []
    risultato_finale : list[dict[str, str | bool]] = []
    domanda_e_risposta : dict[str, str] = {"domanda" : None, "risposta" : None }
    lista_domande = estrai_lista_domande("domande.txt")

    counter_domanda_corrente : int = 0
    lista_domande_lenght : int = len(lista_domande)
    
    feedback : str = ""
    is_risposta_corretta = False
    
    while counter_domanda_corrente < lista_domande_lenght :
        risultato : dict[str, str | bool] = {}
        content : str = leggi_file(F"domande_risposte/{lista_domande[counter_domanda_corrente]}")
        index : int = estrai_index(content)
        domanda_e_risposta["domanda"] = estrai_domanda(content, index)
        domanda_e_risposta["risposta"] = estrai_risposta(content, index)

        mostra_domanda(domanda_e_risposta["domanda"])
        risposta_da_validare : str = raccogli_risposta()
        risposta_validata : bool = valida_scelta(risposta_da_validare)

        if risposta_validata :
            is_risposta_corretta = is_risposta_esatta(risposta_da_validare, domanda_e_risposta["risposta"])
            feedback = genera_feedback(is_risposta_corretta)
            risultato["domanda"] = lista_domande[counter_domanda_corrente]
            risultato["risposta_corretta"] = is_risposta_corretta
            risultato_finale.append(risultato)
            counter_domanda_corrente += 1
        else:
            feedback = "Inserisci solo la risposta tra le optioni elencate"
        
        mostra_feedback(feedback)

    statistiche = genera_statistiche(risultato_finale)

    print(f"Risposte corrette: {statistiche["risposte_esatte"]}")
    print(f"Risposte sbagliate: {statistiche["risposte_errate"]}")    
    
         
#Entry point del nostro programma
main()