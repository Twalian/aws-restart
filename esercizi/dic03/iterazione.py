"""
Creare un dizionario utenti con le seguenti coppie:
"alice": "admin"
"bob": "user"
"charlie": "guest"
Iterare sul dizionario e stampare ogni coppia nel formato: "Username: alice, Ruolo: admin"
Verificare se "bob" è una chiave presente
Stampare tutte le chiavi (usernames)
Stampare tutti i valori (ruoli)

Output Atteso:
Username: alice, Ruolo: admin
Username: bob, Ruolo: user
Username: charlie, Ruolo: guest
bob presente: True
Usernames: dict_keys(['alice', 'bob', 'charlie'])
Ruoli: dict_values(['admin', 'user', 'guest'])

"""
utenti : dict[str, str] = {"alice" : "admin", "bob" : "user", "charlie" : "guest"}

for c,v in utenti.items() :
    print(f"Username: {c}, Ruolo: {v}")

bob_here : bool = "bob" in utenti

print(f"bob presente: {bob_here}")

print(f"Usernames: {utenti.keys()}")

print(f"Ruoli: {utenti.values()}")


