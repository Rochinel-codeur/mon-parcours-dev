# Lire un fichier avec readlines, read et readline
# A lancer depuis le dossier 04_fichiers : python3 01_lire_un_fichier.py

with open("data/animaux.txt", "r") as fichier:
    lignes = fichier.readlines()
    for ligne in lignes:
        print(ligne, end="")

with open("data/animaux.txt", "r") as fichier:
    print(fichier.read())

with open("data/animaux.txt", "r") as fichier:
    ligne = fichier.readline()
    while ligne != "":
        print(ligne, end="")
        ligne = fichier.readline()
