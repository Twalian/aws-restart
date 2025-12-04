personaggio1 : dict[str, str] = {
    "nome" : "Pippo",
    "tipo" : "cane",
    "email" : "pippo@disney.com"
}

personaggio2 : dict[str, str] = {
    "nome" : "Topolino",
    "tipo" : "topo",
    "email" : "topolino@disney.com"
}

personaggi : list[dict] = [personaggio1, personaggio2] 

"""
print(personaggio1["nome"])
print(personaggio1.get("telefono", "telefono non presente"))
"""
personaggio1["telefono"] = "123456789"

#print(personaggio1.get("telefono", "telefono non presente"))

personaggio1["telefono"] = "1234567890"

#print(personaggio1.get("telefono", "telefono non presente"))

for chiave, valore in personaggio1.items() :
    print(f"{chiave} : {valore}")

for x in personaggi :
    del x["tipo"]

print(personaggi)