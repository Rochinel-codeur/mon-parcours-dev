"""Chapitre 6 : modules (sys.argv) - compter les lignes d'un fichier.

Utilisation : python 06_compter_lignes.py data/animaux.txt
"""

import sys

if len(sys.argv) != 2:
    sys.exit("Erreur : entrer un seul argument (le nom du fichier)")

nom_fichier = sys.argv[1]
taille = 0

with open(nom_fichier, "r") as filin:
    for ligne in filin:
        taille += 1
print(taille)
