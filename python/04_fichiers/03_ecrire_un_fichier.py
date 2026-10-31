# Ecrire dans un fichier

animaux = ["hibou", "cheval", "oie", "lapin"]
with open("sortie/animaux_ecrits.txt", "w") as fichier:
    for animal in animaux:
        fichier.write(f"{animal}\n")

# recopier un fichier en ajoutant une etoile devant chaque ligne
with open("data/animaux.txt", "r") as source, open("sortie/animaux_etoiles.txt", "w") as copie:
    for ligne in source:
        copie.write("* " + ligne)

with open("sortie/animaux_etoiles.txt", "r") as fichier:
    print(fichier.read())
