# ESERCIZIO 01

print("="*30)
print("Quiz")
print("="*30)

question1 = "Qual è il tuo cibo preferito?"

answer1 : str = "Pizza"
answer2 : str = "Sushi"
answer3 : str = "Pasta"
answer4 : str = "Hamburger"

print(f"""
{question1}

1 - {answer1}

2 - {answer2}

3 - {answer3}

4 - {answer4}
""")

answer : str = input("Inserisci la risposta (1-4): ")

match answer:
	case "1" :
		result = f"Il cibo scelto è: {answer} - {answer1}"
	case "2"|"3"|"4" :
		result = f"Cambia idea!"
	case _ :
		result = ("Inserisci un numero compreso tra 1 e 4")

print(result)

"""

print("Qual è il tuo cibo preferito?")
 
print("1 - Pizza")

print("2 - Sushi")

print("3 - Pasta")

print("4 - Hamburger")

answer : str = input("Inserisci la risposta (1-4): ")

if answer.isdigit() :
	if int(answer) == 1 :
		print("Margherita, diavola, parmigiana, qualsiasi gusto scegli la pizza è sempre deliziosa!") 
	elif int(answer) == 2 :
		print("Che bontà, quando sei super affamato non c'è niente di meglio di un bell all u can eat!")
	elif int(answer) == 3 :
		print("Team pasta lunga o corta? Io adoro gli spaghetti!")
	elif int(answer) == 4 :
		print("Hamburger e patatine, che coppia perfetta!")
	else :
		print("Inserisci un numero compreso tra 1 e 4")
else :
	print("Inserisci il numero corrisponte all'optione scelta")
"""
