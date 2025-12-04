strighe : list[str | int] = ["Pippo", 1]

strighe.append("Pluto")

strighe.append("Minnie")

#print(strighe)
#print(len(strighe))

"""
for x in strighe : 
    print(x)
"""
deleted_values : list[str | int] = []

value_to_check : str = "Pluto"

is_value_in_the_list : bool = value_to_check in strighe

if is_value_in_the_list == True :

    index_value_to_delete : int = strighe.index("Pluto")
    deleted_value = strighe.pop(index_value_to_delete)
    deleted_values.append(deleted_value)
else :
    print(f"{value_to_check} non esiste nella lista {strighe}")

#deleted_value = strighe.pop(1)

print("*"*30)
print(strighe)
print(deleted_values)



