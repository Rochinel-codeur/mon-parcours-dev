# Se deplacer dans un fichier avec tell et seek

with open("data/animaux.txt", "r") as fichier:
    print(fichier.readline(), end="")
    position = fichier.tell()
    print(fichier.read())
    fichier.seek(position)  # on revient juste apres la premiere ligne
    print(fichier.read())
