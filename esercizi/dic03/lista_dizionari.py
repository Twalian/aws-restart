"""
Creare una lista prodotti contenente 4 dizionari, ognuno con chiavi "nome", "prezzo", "quantita":
{"nome": "Laptop", "prezzo": 899.99, "quantita": 5}
{"nome": "Mouse", "prezzo": 25.50, "quantita": 50}
{"nome": "Tastiera", "prezzo": 75.00, "quantita": 30}
{"nome": "Monitor", "prezzo": 299.99, "quantita": 15}
Iterare sulla lista e stampare solo i prodotti con prezzo superiore a 100
Calcolare il valore totale dell'inventario (prezzo × quantità per ogni prodotto)

Output Atteso:
Prodotti > 100€:
- Laptop: €899.99
- Monitor: €299.99

Valore totale inventario: 12524.8€
"""

products : list[dict[str, str | int | float]] = [
    {"nome": "Laptop", "prezzo": 899.99, "quantita": 5},
    {"nome": "Mouse", "prezzo": 25.50, "quantita": 50},
    {"nome": "Tastiera", "prezzo": 75.00, "quantita": 30},
    {"nome": "Monitor", "prezzo": 299.99, "quantita": 15}
]

inventario : float = 0

print("I prodotti con un prezzo superiore a 100€ sono: ")
for product in products:
    inventario += product["prezzo"] * product["quantita"]
    print(f"{product["nome"]} : {product["prezzo"]}€") if product["prezzo"] > 100 else None

print(f"Il totale dell'inventario è {inventario}€")