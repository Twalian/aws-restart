from data.repository import get_file

def get_domanda(file_path : str) -> str :
    with get_file(file_path) as file :
        content = file.read()
        return content 
    
def get_lista_domande(file_path : str) -> list[str] :
    lista_domande : list[str] = []
    with get_file(file_path) as f:
        for i in f :
            lista_domande.append(i.strip())
    return lista_domande


def estrai_index(content : str) -> int :
    return content.index("£")
   
def estrai_domanda(content : str, index : int) -> str:
    return content[0:index]

def estrai_risposta(content : str, index : int) -> str:
    return content[index+1:]

def valida_scelta(scelta: str) -> bool:
    """
    Questa funzione prende un valore di tipo stringa e verifica che la risposta sia una delle opzioni tra A, B, C e D. 
    Se la risposta è una stringa vuota, restituisce false, idem se la risposta non è una di quelle sopra elencate.
    """
    scelta_tmp = scelta.upper()
    return scelta_tmp in ["A", "B", "C", "D"]

def is_risposta_esatta(scelta: str, risposta_esatta: str) -> bool:
    return scelta.upper() == risposta_esatta

def naviga_tra_le_domande(contatore_domanda_attuale : int, domande_totali : int) -> int :

    navigazione : bool = True

    navigazione_prima_domanda : bool = False

    while navigazione :

        print("<-- P (Domanda precedente)  ***  (Domanda successiva) S --> ")
        scelta_utente : str = input(f"Oppure inserisci il numero della domanda che vuoi visualizzare (1 - {domande_totali}): ")
        
        if scelta_utente.upper() == "P" :

            if contatore_domanda_attuale == 0 :

                print("")
                print("*"*30)
                print("Nessuna domanda precedente!")
                print("*"*30)
                print("")

                navigazione_prima_domanda = True

                while navigazione_prima_domanda :

                    scelta_utente = input("R (Ripeti prima domanda)  ***  (Domanda successiva) S --> ")

                    if scelta_utente.upper() == "S" :
                        contatore_domanda_attuale += 1
                        return contatore_domanda_attuale

                    elif scelta_utente.upper() == "R" :
                        contatore_domanda_attuale == 0
                        return contatore_domanda_attuale

                    else:
                        print("") 
                        print("Inserisci solo R o S")
                        print("")
                               
            else :
                contatore_domanda_attuale -= 1
                return contatore_domanda_attuale
            
        elif scelta_utente.upper() == "S" :

            if contatore_domanda_attuale < domande_totali :
                contatore_domanda_attuale += 1
                if contatore_domanda_attuale == domande_totali :
                    print("")
                    print("*"*30)
                    print("Domande terminate!")
                    print("*"*30)
            return contatore_domanda_attuale
        
        elif int(scelta_utente) > 0 and int(scelta_utente) <= domande_totali :
            contatore_domanda_attuale = int(scelta_utente)-1
            return contatore_domanda_attuale

        else :
            print("")
            print(f"Inserisci solo P, S o valori compresi tra 1 e {domande_totali}")
            print("")
    
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

def calcola_percentuale(parte: int, totale: int) -> float:
    """Calcola la percentuale (0-100) date due quantità."""
    if totale == 0:
        return 0.0
    return (parte / totale) * 100

def verifica_superamento(percentuale: float, soglia: float = 60.0) -> bool:
    """Restituisce True se la percentuale è maggiore o uguale alla soglia."""
    return percentuale >= soglia

def recupera_dati_domanda(nome_file: str) -> dict[str, str]:
    """Gestisce il parsing di ogni domanda"""
    content: str = get_domanda(f"domande_risposte/{nome_file}")
    index: int = estrai_index(content)
    return {
        "domanda" : estrai_domanda(content, index),
        "risposta" : estrai_risposta(content, index)
    }

def aggiorna_lista_risultati(lista_risultati: list, nuovo_risultato: dict, indice: int) -> None:
    """Aggiorna la lista dei risultati gestendo sia l'inserimento che la modifica."""
    if indice < len(lista_risultati):
        lista_risultati[indice] = nuovo_risultato
    else:
        lista_risultati.append(nuovo_risultato)
