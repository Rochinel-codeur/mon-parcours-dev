# Jours de la semaine (for, puis while pour le week-end)

semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

for jour in semaine:
    print(jour)

i = 5
while i < len(semaine):
    print(semaine[i])
    i += 1
