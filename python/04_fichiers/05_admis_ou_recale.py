# Admis ou recale : ecrire un fichier de resultats

with open("data/notes.txt", "r") as notes, open("sortie/resultats.txt", "w") as resultats:
    for ligne in notes:
        note = float(ligne)
        if note >= 10:  # >= et pas > : avec 10/20 on est admis
            resultats.write(f"{note} admis\n")
        else:
            resultats.write(f"{note} recalé\n")

with open("sortie/resultats.txt", "r") as resultats:
    print(resultats.read())
