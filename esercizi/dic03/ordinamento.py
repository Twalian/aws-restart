"""
Creare una lista prezzi contenente: [45.5, 12.0, 78.3, 23.1, 56.7]
Creare una copia ordinata della lista (usando sorted())
Trovare il prezzo minimo e massimo
Verificare se 23.1 è nella lista
Contare quanti prezzi sono maggiori di 50

Output Atteso:
Prezzi originali: [45.5, 12.0, 78.3, 23.1, 56.7]
Prezzi ordinati: [12.0, 23.1, 45.5, 56.7, 78.3]
Minimo: 12.0
Massimo: 78.3
23.1 presente: True
Prezzi > 50: 2

"""

prezzi_u : list[float] = [45.5, 12.0, 78.3, 23.1, 56.7]

prezzi_o : list[float] = sorted(prezzi_u)

print(prezzi_o)

print(min(prezzi_o))

print(max(prezzi_o))

"""
counter : int = 0

for p in prezzi_o :
    if p > 50 :
        counter += 1

print(counter)
"""

is_here : bool = 23.1 in prezzi_o

print(is_here)

print(sum(1 for p in prezzi_o if p > 50))