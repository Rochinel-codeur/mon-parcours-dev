# Parcourir une liste de 4 facons

animaux = ["vache", "souris", "levure", "bacterie"]

for animal in animaux:
    print(animal)

for i in range(len(animaux)):
    print(animaux[i])

for i, animal in enumerate(animaux):
    print(f"l'animal {i} est un {animal}")

i = 0
while i < len(animaux):
    print(animaux[i])
    i += 1
