from data.services import (
    get_domanda,
    get_lista_domande, 
    valida_scelta, 
    is_risposta_esatta,
    estrai_domanda,
    estrai_index,
    estrai_risposta, 
    genera_statistiche,
    naviga_tra_le_domande,
)
from ui.console import (
    mostra_feedback, 
    mostra_domanda, 
    genera_feedback, 
    raccogli_risposta,
)

def main()  :

    lista_domande: list[str] = []
    risultato_finale : list[dict[str, str | bool]] = []
    domanda_e_risposta : dict[str, str] = {"domanda" : None, "risposta" : None }
    lista_domande = get_lista_domande("domande.txt")

    counter_domanda_corrente : int = 0
    lista_domande_lenght : int = len(lista_domande)
    
    feedback : str = ""
    is_risposta_corretta = False
    
    while counter_domanda_corrente < lista_domande_lenght :
        
        risultato : dict[str, str | bool] = {}
        content : str = get_domanda(F"domande_risposte/{lista_domande[counter_domanda_corrente]}")
        index : int = estrai_index(content)
        domanda_e_risposta["domanda"] = estrai_domanda(content, index)
        domanda_e_risposta["risposta"] = estrai_risposta(content, index)

        mostra_domanda(domanda_e_risposta["domanda"], counter_domanda_corrente+1, lista_domande_lenght)
        risposta_da_validare : str = raccogli_risposta()
        risposta_validata : bool = valida_scelta(risposta_da_validare)

        if risposta_validata :
            is_risposta_corretta = is_risposta_esatta(risposta_da_validare, domanda_e_risposta["risposta"])
            feedback = genera_feedback(is_risposta_corretta)
            risultato["domanda"] = lista_domande[counter_domanda_corrente]
            risultato["risposta_corretta"] = is_risposta_corretta

            if counter_domanda_corrente < len(risultato_finale) :
                risultato_finale[counter_domanda_corrente] = risultato
            else:
                risultato_finale.append(risultato)

            #mostra_feedback(feedback)
            print("")
            counter_domanda_corrente = naviga_tra_le_domande(counter_domanda_corrente, lista_domande_lenght)  
        else:
            feedback = "Inserisci solo la risposta tra le optioni elencate"
            mostra_feedback(feedback)
           
    statistiche = genera_statistiche(risultato_finale)

    print("")
    print("--- Il tuo punteggio ---")
    print(f"Risposte corrette: {statistiche["risposte_esatte"]}")
    print(f"Risposte sbagliate: {statistiche["risposte_errate"]}")
         
#Entry point del nostro programma
main()