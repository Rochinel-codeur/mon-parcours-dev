# Compter les lignes d'un fichier passe en argument (module sys)
# Utilisation, depuis le dossier 06_modules :
#   python3 01_compter_lignes.py ../04_fichiers/data/animaux.txt

import sys

if len(sys.argv) != 2:
    sys.exit("Erreur : entrer un seul argument (le nom du fichier)")

nom_fichier = sys.argv[1]
taille = 0

with open(nom_fichier, "r") as filin:
    for ligne in filin.readlines():
        taille += 1
    print(taille)
