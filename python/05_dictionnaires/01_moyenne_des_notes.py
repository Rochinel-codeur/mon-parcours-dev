# Moyennes des notes d'un dictionnaire

dico_notes = {
    "math": 14, "programmation": 12,
    "anglais": 16, "biologie": 10,
    "sport": 19
}

# moyenne sans la biologie
somme = 0
i = 0
for matiere, note in dico_notes.items():
    if matiere == "biologie":
        continue
    somme += note
    i += 1
print(f"la moyenne sans la biologie est {somme / i}")

# moyenne de toutes les matieres
somme1 = 0
j = 0
for note in dico_notes.values():
    somme1 += note
    j += 1
print(f"la moyenne generale est {somme1 / j}")
