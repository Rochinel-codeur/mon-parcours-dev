# Coordonnees d'une spirale ecrites dans un fichier

import math

teta = 0
r = 0.5

# on ouvre le fichier une seule fois, avant la boucle :
# avec "w", chaque ouverture efface tout ce qui etait deja ecrit
with open("sortie/spirale.dat", "w") as fichier:
    while teta <= 4 * math.pi:
        XA = math.cos(teta) * r
        YA = math.sin(teta) * r
        fichier.write(f"{XA:10.5f} {YA:10.5f}\n")
        teta += 0.1
        r += 0.1

with open("sortie/spirale.dat", "r") as fichier:
    print(fichier.read())
