# Calculer une moyenne

notes = [14, 9, 6, 8, 12]
somme = 0
for note in notes:
    somme = somme + note
print(f"la moyenne est {somme / len(notes):.2f}")
