# Compter les acides amines d'une sequence

sequence = "AGWPSGGASAGLAILWGASAIM"
composition = {}
for acide in sequence:
    if acide in composition:
        composition[acide] += 1
    else:
        composition[acide] = 1
print(composition)
