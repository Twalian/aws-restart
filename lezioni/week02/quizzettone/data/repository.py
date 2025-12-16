from typing import TextIO

def get_file(file_path: str) -> TextIO :
    """Recupera un oggetto IO (input output) di tipo testuale da un file specifico"""
    return open (file_path, "r")

def send_questions(file_path: str) -> TextIO :
    return open (file_path, "w")
