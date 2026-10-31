# Demi-matrice sans la diagonale

N = int(input("entrer la dimension de la matrice : "))
for i in range(1, N):
    for j in range(i + 1, N + 1):
        print(f"{i} {j}")
