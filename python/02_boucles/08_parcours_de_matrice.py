# Parcours d'une matrice avec for, puis avec while

N = int(input("entrer la dimension de la matrice : "))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(f"{i:<4d} {j:4d}")

i = 1
while i <= N:
    j = 1
    while j <= N:
        print(f"nous sommes a la ligne {i} et a la colonne {j}")
        j += 1
    i += 1
