from requests import get
import re

BASE_URL : str = "https://github.com"
END_URL : str = "tab=followers"
PATTERN = r'<a\s+[^>]*href="https://github\.com/([^/]+)\?page=(\d+)&amp;tab=followers"[^>]*>Next</a>'

def is_next_button_present(text: str) -> bool:
    if not text:
        raise ValueError("Il testo non può essere vuoto!")
    return bool(re.search(PATTERN, text))
    

def main() -> None:
    print("---Start del programma---")

    nome_utente : str = input("Inserisci lo username del profilo github che vuoi utilizzare: ")
    print(f"Stai cercando: {nome_utente}")

    controller : bool = True
    counter : int = 1
    
    while controller:

        url = f"{BASE_URL}/{nome_utente}?page={counter}&{END_URL}"

        try:
            response = get(url)

            if response.status_code == 404:
                print("Profilo non trovato")
                break

            with open(f"tmp/pagina-{counter}.txt", "w") as f:
                f.write(response.text)
                controller = is_next_button_present(response.text)
                print("** File salvato **")
                counter += 1
                
        except Exception as e:
            print(f"Errore: {e}")
    print("** Fine while, tutti i file sono stati scaricati! **")

if __name__ == "__main__":
    main()