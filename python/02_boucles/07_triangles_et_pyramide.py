# Triangles et pyramide d'etoiles

n = int(input("entrer le nombre de lignes : "))

for i in range(1, n + 1):
    print("*" * i)

for i in range(n, 0, -1):
    print("*" * i)

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

for i in range(1, n + 1):
    espaces = n - i
    etoiles = 2 * i - 1
    print(" " * espaces + "*" * etoiles)
