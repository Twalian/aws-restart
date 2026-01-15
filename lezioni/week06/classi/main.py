"""
class Formina:
    def __init__(self, nome_forma):
        self.forma = nome_forma

biscotto1 = Formina("cuoricino")
biscotto2 = Formina("stellina")

print(biscotto1.forma)
print(biscotto2.forma)
"""
class Persona:
    def __init__(self, nome: str, cognome: str, isEdgemonyStudent: bool):
        self.nome = nome
        self.cognome = cognome
        self.isEdgemonyStudent = isEdgemonyStudent

    def print_isEdgemonyStudent(self) -> None:
        print(f"{self.nome} {self.cognome}: {self.isEdgemonyStudent}")

class Corso:
    def __init__(self, nome: str):
        self.nome = nome
        self.partecipanti = []
    
    def addPartecipante(self, p: Persona) -> bool:
        if p.isEdgemonyStudent:
            self.partecipanti.append(f"{p.nome} {p.cognome}")
            return True
        else:
            return False

persona1 = Persona("Pippo", "Disney", True)
persona2 = Persona("Topolino", "Disney", False)
persona3 = Persona("Minnie", "Disney", True)

corso1 = Corso("Edgemony")

ar = [persona1, persona2, persona3]

print(corso1.partecipanti)

for p in ar:
    print(corso1.addPartecipante(p))

print(corso1.partecipanti)
