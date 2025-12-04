"""
Creare una lista voti contenente: ["A", "B", "A", "C", "B", "A", "D", "B", "C", "A"]
Creare un dizionario vuoto conteggio
Iterare sulla lista voti e contare quante volte appare ogni voto nel dizionario
Stampare il dizionario finale
Suggerimento: Usare conteggio.get(voto, 0) per gestire chiavi mancanti.

Output Atteso:
Conteggio voti: {'A': 4, 'B': 3, 'C': 2, 'D': 1}

"""

voti : list[str] = ["A", "B", "A", "C", "B", "A", "D", "B", "C", "A"]

conteggio : dict[str, int] = {}

conteggio["A"] = 0
conteggio["B"] = 0
conteggio["C"] = 0
conteggio["D"] = 0

for v in voti :
    if v == "A" :
        conteggio["A"] += 1
    elif v == "B" :
        conteggio["B"] += 1
    elif v == "C" :
        conteggio["C"] += 1
    else :
        conteggio["D"] += 1

print(f"Conteggio voti: {conteggio}")
