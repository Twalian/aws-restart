print("="*20)
print("WHILE")
print("="*20)

pass_corretta: str = "1234"
pass_input : str = ""

"""

while pass_input != pass_corretta : 
	pass_input = input("Inserisci la password: ")
print("Password corretta")

"""

while True : 
	pass_input = input("Inserisci la password: ")
	if pass_input == pass_corretta :
		print("Password corretta")
		break
	else :
		print("Password errata!")
		
