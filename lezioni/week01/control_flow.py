
"""

answer : str = input("Hai la patente?")

if (answer.lower() == "yes") or (answer.lower() == "si") :
	print("Puoi guidare")
elif (answer.lower() == "no"):
	print("Non puoi guidare")
else:
	print("inserisci solo yes o no")

"""
"""

answer =  input("Quanti anni hai?")

if answer.isdigit() :

	if int(answer) >= 18 :
		print("Puoi guidare")
	else:
		print("Non puoi guidare")
else:
	print("Inserisci un numero")

"""

answer =  input("Quanti anni hai?")

if answer.isdigit() :
	result = "Puoi guidare" if int(answer) >= 18 else "Non puoi guidare"
	print(result)
else:
        print("Inserisci un numero")
