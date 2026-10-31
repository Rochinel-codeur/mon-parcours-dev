# Trouver le plus petit element sans utiliser min()

liste = [8, 4, 6, 1, 5]
plus_petit = liste[0]
for i in liste:
    if i < plus_petit:
        plus_petit = i
print(plus_petit)
