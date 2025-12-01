# Esercizio Quiz v2


def mostra_menu() -> None:
    question1 = "Qual è il tuo cibo preferito?"

    answer1: str = "Pizza"
    answer2: str = "Sushi"
    answer3: str = "Pasta"
    answer4: str = "Hamburger"

    print(f"""
	{question1}

	1 - {answer1}

	2 - {answer2}

	3 - {answer3}

	4 - {answer4}
	""")


def raccogli_risposta() -> int:
    while True:
        answer: str = input("Inserisci la risposta (1-4): ")

        if answer.isdigit():
            return int(answer)
        else:
            print("Inserisci un numero")


def valida_scelta(scelta: int) -> bool:
    if scelta >= 1 and scelta <= 4:
        return True
    else:
        return False


def genera_feedback(scelta: int) -> str:
    if scelta == 1:
        return "Margherita, diavola, parmigiana, qualsiasi gusto scegli la pizza è sempre deliziosa!"
    elif scelta == 2:
        return "Che bontà, quando sei super affamato non c'è niente di meglio di un bell all u can eat!"
    elif scelta == 3:
        return "Team pasta lunga o corta? Io adoro gli spaghetti!"
    else:
        return "Hamburger e patatine, che coppia perfetta!"


def mostra_feedback(messaggio: str) -> None:
    print(messaggio)


mostra_menu()
while True:
    answer: int = raccogli_risposta()
    if valida_scelta(answer):
        mostra_feedback(genera_feedback(answer))
        break
    else:
        print("Inserisci solo numeri compresi tra 1 e 4")
