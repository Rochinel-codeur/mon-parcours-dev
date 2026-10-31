"""Chapitre 4 : lire et ecrire des fichiers (open, with, read, readline, seek)."""

import math
from pathlib import Path

from menu import lancer

DATA = Path(__file__).parent / "data"
SORTIE = Path(__file__).parent / "sortie"


def lire_un_fichier():
    """Lire un fichier : readlines, read et readline"""
    with open(DATA / "animaux.txt", "r") as fichier:
        for ligne in fichier.readlines():
            print(ligne, end="")

    with open(DATA / "animaux.txt", "r") as fichier:
        print(fichier.read())

    with open(DATA / "animaux.txt", "r") as fichier:
        ligne = fichier.readline()
        while ligne != "":
            print(ligne, end="")
            ligne = fichier.readline()


def revenir_en_arriere():
    """Se deplacer dans un fichier avec tell et seek"""
    with open(DATA / "animaux.txt", "r") as fichier:
        print(fichier.readline(), end="")
        position = fichier.tell()
        print(fichier.read())
        fichier.seek(position)  # on revient juste apres la premiere ligne
        print(fichier.read())


def ecrire_un_fichier():
    """Ecrire dans un fichier"""
    SORTIE.mkdir(exist_ok=True)
    animaux = ["hibou", "cheval", "oie", "lapin"]
    with open(SORTIE / "animaux_ecrits.txt", "w") as fichier:
        for animal in animaux:
            fichier.write(f"{animal}\n")

    # recopier un fichier en ajoutant une etoile devant chaque ligne
    with open(DATA / "animaux.txt", "r") as source, open(SORTIE / "animaux_etoiles.txt", "w") as copie:
        for ligne in source:
            copie.write("* " + ligne)

    with open(SORTIE / "animaux_etoiles.txt", "r") as fichier:
        print(fichier.read())


def moyenne_des_notes():
    """Moyenne des notes d'un fichier"""
    notes = []
    with open(DATA / "notes.txt", "r") as fichier:
        for ligne in fichier:
            notes.append(float(ligne))
    print(f"la moyenne est : {sum(notes) / len(notes):.2f}")


def admis_ou_recale():
    """Admis ou recale : ecrire un fichier de resultats"""
    SORTIE.mkdir(exist_ok=True)
    with open(DATA / "notes.txt", "r") as notes, open(SORTIE / "resultats.txt", "w") as resultats:
        for ligne in notes:
            note = float(ligne)
            if note >= 10:
                resultats.write(f"{note} admis\n")
            else:
                resultats.write(f"{note} recalé\n")

    with open(SORTIE / "resultats.txt", "r") as resultats:
        print(resultats.read())


def spirale():
    """Coordonnees d'une spirale dans un fichier"""
    SORTIE.mkdir(exist_ok=True)
    teta = 0
    r = 0.5
    # on ouvre le fichier une seule fois, sinon "w" efface tout a chaque tour
    with open(SORTIE / "spirale.dat", "w") as fichier:
        while teta <= 4 * math.pi:
            XA = math.cos(teta) * r
            YA = math.sin(teta) * r
            fichier.write(f"{XA:10.5f} {YA:10.5f}\n")
            teta += 0.1
            r += 0.1

    with open(SORTIE / "spirale.dat", "r") as fichier:
        print(fichier.read())


if __name__ == "__main__":
    lancer([lire_un_fichier, revenir_en_arriere, ecrire_un_fichier, moyenne_des_notes, admis_ou_recale, spirale])
