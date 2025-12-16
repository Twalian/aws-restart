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
    
def mostra_domanda(domanda : str, domanda_attuale : int, domande_totali : int) -> None:
    """
    Questa funzione restituisce la domanda e le optioni di risposta
    """
    print(f"Domanda {domanda_attuale} di {domande_totali}")
    print(domanda)

def print_statistiche(statistiche : dict[str, int]) -> None :
    print("")
    print("--- Il tuo punteggio ---")
    print(f"Risposte corrette: {statistiche["risposte_esatte"]}")
    print(f"Risposte sbagliate: {statistiche["risposte_errate"]}")    