# Moyenne des notes lues dans un fichier

notes = []
with open("data/notes.txt", "r") as fichier:
    for ligne in fichier:
        notes.append(float(ligne))

somme = 0
for note in notes:
    somme = somme + note
print(f"la moyenne est : {somme / len(notes):.2f}")
