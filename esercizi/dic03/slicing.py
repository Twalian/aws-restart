"""
Creare una lista temperature contenente: [15, 18, 22, 25, 28, 30, 27, 24, 20]
Stampare la prima temperatura
Stampare l'ultima temperatura
Stampare le temperature dalla posizione 2 alla 5 (esclusa)
Stampare tutte le temperature con step 2 (saltando una ogni due)

Output Atteso:
Prima temperatura: 15
Ultima temperatura: 20
Temperature [2:5]: [22, 25, 28]
Ogni due: [15, 22, 28, 27, 20]

"""

temperature : list[int] = [15, 18, 22, 25, 28, 30, 27, 24, 20]

print(f"Prima temperatura: {temperature[0]}")
print(f"Ultima temperatura: {temperature[-1]}")

temperature_range : list[int] = []

for t in range(2, 5) :
    temperature_range.append(temperature[t])
print(f"Temeperature (2-5): {temperature_range}")

temperature_pari : list[int] = []

for t in range(0, len(temperature), 2) :
    temperature_pari.append(temperature[t])
print(f"Temeperature (ogni 2): {temperature_pari}")    