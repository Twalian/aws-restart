# ===============================
#   Services
# =============================== 

import re
from constant import REGEX_SENZA_SPAZI, REGEX_PAROLE_LETTERE, REGEX_FRASI

def get_text_len(text: str) -> int:
    if text is None:
        return 0
    return len(text)

import re
def get_text_len_no_space(text: str) -> int:
    if text is None:
        return 0
    return len(re.findall(REGEX_SENZA_SPAZI, text))

def get_words_len(text: str) -> int:
    if text is None:
        return 0
    return len(re.findall(REGEX_PAROLE_LETTERE, text))

def get_sentences_len(text: str) -> int:
    if text is None:
        return 0
    return len(re.findall(REGEX_FRASI, text))
