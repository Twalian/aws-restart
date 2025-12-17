r"""
Il commit checker

Problema:

Ogni giorno i partecipanti di un corso devono fare degli esercizi e pushare su github, ma serve un modo per verificare quando è stato l'ultimo push sul repo.

Obiettivo:

Dobbiamo creare un programmino che data una lista di repository, sia in grado di verificare quando è stato l'ultimo commit.

Cosa sappiamo:

è possibile vedere i commit fatti su uno specifico repository a questo URL https://github.com/<nome-utente>/<nome-repository>/commits/<nome-branch>/

Domande:

-Possiamo fare scraping? 
-Ci sono pattern che si ripetono nella pagina web?
-Ci serve una lista di repository. Dove la metto?
-Come salvo il risultato?

-------------------------------

Lista repository:

    Link: https://github.com/Twalian?tab=repositories

    PATTERN: <a href="/Twalian/libreria" itemprop="name codeRepository"> libreria</a> 
    ----> r'<a\s+href="([^"]+)"\s+itemprop="name codeRepository">\s*([^<]+)\s*</a>'


    1. get page
    2. cerco tutte le istanze del pattern
    3. li salvo in una lista
    4 stampo la lista 


Ultimo commit:

    Link: https://github.com/Twalian/aws-restart/commits/main/

"""
from requests import Response, get
from requests.exceptions import  HTTPError, ConnectionError, Timeout, RequestException
import re
from datetime import datetime
from zoneinfo import ZoneInfo

BASE_URL = "https://github.com"

PATTERN_REPOSITORY = (
    r'<a\b[^>]*'
    r'href="[^"]+"'
    r'[^>]*'
    r'itemprop="name codeRepository"'
    r'[^>]*>'
    r'\s*([^<]+?)\s*</a>'
)

PATTERN_COMMIT_DATETIME = r'"committedDate"\s*:\s*"([^"]+)"'

def get_page(url: str) -> Response:

    if url is None:
        raise ValueError("L'URL non può essere vuoto")
    
    try:
        response = get(url)
        response.raise_for_status()
        return response
    
    except HTTPError as e:
        raise HTTPError(f"Errore HTTP {response.status_code} su {url}: {response.reason}"
        ) from e

    except ConnectionError:
        raise ConnectionError(f"Impossibile connettersi a {url}")
    
    except Timeout:
        raise Timeout(f"Timeout nella richiesta a {url}")
    
    except RequestException as e:
        raise RequestException(f"Errore di rete imprevisto: {e}")
    
def find_pattern_and_make_a_list(pattern : str, url : str) -> list[str]:
    tmp_list : list[str] = []
    page_text = get_page(url).text
    tmp_list.extend(re.findall(pattern, page_text))
    return tmp_list
    
def main() -> None:
    
    step_due : bool = False
    step_tre : bool = False
     
    while True:

        try:
            nome_utente : str = input("Inserisci lo username del profilo github che vuoi utilizzare o digita exit per uscire: ")

            if not nome_utente:
                raise ValueError("Il nome utente non può essere vuoto!")

            #TODO: il nome exit esiste come profilo
            if nome_utente == "exit":
                break

            print(f"Sto cercando {nome_utente}...")

            response = get_page(f"{BASE_URL}/{nome_utente}")
            if response.status_code == 404:
                print("Profilo non trovato")
            else:
                print("Profilo trovato!")
                step_due = True
                break
        except Exception as e:
                print(f"Errore: {e}")

    while step_due :
        
        try:
            print("")
            print(f"Lista delle repository di {nome_utente}: ")
            print("")
            repository_list : list[str] = find_pattern_and_make_a_list(PATTERN_REPOSITORY, f"{BASE_URL}/{nome_utente}?tab=repositories")
            print("*"*20)
            for x in range(len(repository_list)) :
                print(f"{x+1}) {repository_list[x]}")
            print("*"*20)
            print("")
            print(f"Di quale repository vuoi verificare l'ultimo commit? (1-{len(repository_list)})")
            scelta_utente : str = input()
            if scelta_utente.isdigit():
                if int(scelta_utente) > 0 and int(scelta_utente) <= len(repository_list):
                    step_tre = True
                    break
                else:
                    print(f"Inserisci solo valori compresi tra 1 e {len(repository_list)}")
            else:
                 print(f"Inserisci solo valori numerici compresi tra 1 e {len(repository_list)}")
        except Exception as e:
                print(f"Errore: {e}")
    
    while step_tre :

        try:
            #TODO: controllare si ci sono più branch e permettere di scegliere
            page_text = get_page(f"{BASE_URL}/{nome_utente}/{repository_list[int(scelta_utente)-1]}/commits/main/").text
            last_commit : str = re.search(PATTERN_COMMIT_DATETIME, page_text)
            
            iso_datetime = last_commit.group(1)  # => '2025-12-17T14:33:36.000+01:00'
    
            # Parsing ISO 8601
            dt_utc = datetime.fromisoformat(iso_datetime.replace("Z", "+00:00"))
                
            # Convertire al fuso orario locale (es. Europa/Roma)
            
            dt_local = dt_utc.astimezone(ZoneInfo("Europe/Rome"))
                
            # Formattare data e ora a piacere
            formatted = dt_local.strftime("%d/%m/%Y %H:%M:%S")

            print(f"L'ultimo commit di {nome_utente} in {repository_list[int(scelta_utente)-1]} è stato {formatted}")
            break
            
        except Exception as e:
                print(f"Errore: {e}")
                break


    
if __name__ == "__main__":
    main()