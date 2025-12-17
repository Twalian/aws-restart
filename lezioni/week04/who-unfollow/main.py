from requests import get
import re
import uuid
import datetime
import json

BASE_URL : str = "https://github.com"
END_URL : str = "tab=followers"
PATTERN = r'<a\s+[^>]*href="https://github\.com/([^/]+)\?page=(\d+)&amp;tab=followers"[^>]*>Next</a>'
PATTERN_UTENTE = r'<span class="Link--secondary(?: pl-1)?">([^<]+)</span>'

def save(db_name : str, new_value: dict[str,str]) -> bool:
    db : list[str] = []
    with open(f"db/{db_name}", "r") as f:
        db.extend(json.load(f))
        
    db.append(new_value)

    with open(f"db/{db_name}", "w") as f:
        json.dump(db, f)
        
    return bool

def create_record_object(user_list: list[str]) -> dict[str, str]:
    if not user_list:
        return None
    
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    clean_date = now_utc.isoformat(timespec='milliseconds').replace('+00:00', 'Z')

    return {
        'id': str(uuid.uuid4()),  
        'createdAt': clean_date,  
        'users': user_list,
        'numberOfUsers': len(user_list)
    }

def is_next_button_present(text: str) -> bool:
    if not text:
        raise ValueError("Il testo non può essere vuoto!")
    return bool(re.search(PATTERN, text))
    

def main() -> None:
    print("---Start del programma---")

    controller : bool = False

    counter : int = 0

    #===============
    # Pimo while
    #===============

    while True:

        try:
            nome_utente : str = input("Inserisci lo username del profilo github che vuoi utilizzare o digita exit per uscire: ")

            if not nome_utente:
                raise ValueError("Il nome utente non può essere vuoto!")

            #TODO: il nome exit esiste come profilo
            if nome_utente == "exit":
                break

            print(f"Sto cercando {nome_utente}...")

            response = get(f"{BASE_URL}/{nome_utente}")
            if response.status_code == 404:
                print("Profilo non trovato")
            else:
                print("Profilo trovato!")
                controller = True
                break
        except Exception as e:
                print(f"Errore: {e}")

    #===============
    # Secondo while
    #===============     
        
    while controller:

        counter += 1

        url = f"{BASE_URL}/{nome_utente}?page={counter}&{END_URL}"

        try:
            response = get(url)

            with open(f"tmp/pagina-{counter}.txt", "w") as f:
                f.write(response.text)
                controller = is_next_button_present(response.text)
                print("** File salvato **")
                
        except Exception as e:
            print(f"Errore: {e}")

    lista_utenti : list[str] = []

    for i in range(counter):
        with open(f"tmp/pagina-{i+1}.txt", "r") as f:
            text = f.read()
            lista_utenti.extend(re.findall(PATTERN_UTENTE, text))
        
    save("db.json", create_record_object(lista_utenti))

    print("---Fine programma, arrivederci!---")

if __name__ == "__main__":
    main()

"""
[
    {
        id: uuid
        createdAt: data e ora
        users: []
        numberOfUsers : int
    }
 ]
"""