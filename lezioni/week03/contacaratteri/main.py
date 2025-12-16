# REGEX REFERENCE:
# ================

# Pattern                 | Descrizione
# ------------------------|--------------------------------------------
# .                       | Tutti i caratteri (con re.DOTALL include \n)
# \S                      | Caratteri senza spazi
# [a-zA-ZÀ-ÿ]             | Solo lettere (incluse accentate)
# \w+                     | Parole (lettere, numeri, underscore)
# [a-zA-ZÀ-ÿ]+            | Parole solo lettere (incluse accentate)
# [^.!?]+[.!?]+           | Frasi (testo seguito da punteggiatura)
# testo.split('\\n\\n')   | Paragrafi (separati da riga vuota)

# ===============================
#   Regex Patterns
# ===============================

# REGEX_TUTTI_CARATTERI = r'.'           # Tutti i caratteri (usare con re.DOTALL)
# REGEX_SENZA_SPAZI = r'\S'              # Caratteri esclusi gli spazi
# REGEX_SOLO_LETTERE = r'[a-zA-ZÀ-ÿ]'   # Solo lettere, incluse accentate
# REGEX_PAROLE = r'\w+'                  # Parole (lettere, numeri, underscore)
# REGEX_PAROLE_LETTERE = r'[a-zA-ZÀ-ÿ]+' # Parole composte solo da lettere
# REGEX_FRASI = r'[^.!?]+[.!?]+'         # Frasi terminate da . ! ?

"""
- dove si trova il testo?
    -il testo viene preso da un file
    -i file vengono mostrati a video dalla console
-voglio contare i caratteri di un testo
    -con spazi e senza spazi
    -numero di parole
    -numero di frasi
    -numero di paragrafi
    -determinare il tempo di lettura
    -verificare ripetizioni di parole o lettere specifiche
-dove voglio mostrare il risultato?
    -console
    -scriverlo su un file
"""

from ui.console import print_risultato
from data.services import get_text_len, get_text_len_no_space, get_words_len, get_sentences_len
from data.repository import get_data_from_server
from constant import URL
    
def main() -> None:
    try:
        #file_path : str = "text.txt"
        #content : str = get_file_content(file_path)
        content: str = get_data_from_server(URL)
        print(get_text_len(content), "caratteri")
        print(get_text_len_no_space(content), "caratteri senza spazi")
        print(get_words_len(content), "parole")
        print(get_sentences_len(content), "frasi")
    except ValueError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"{e}")

if __name__ == "__main__":
    main()