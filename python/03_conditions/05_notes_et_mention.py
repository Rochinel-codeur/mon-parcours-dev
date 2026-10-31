# Minimum, maximum, moyenne et mention

liste = [14, 9, 13, 15, 12]
somme = 0
for i in liste:
    somme += i
print(min(liste))
print(max(liste))

moyenne = somme / len(liste)
if moyenne < 12:
    print(f"la moyenne obtenue est {moyenne} et la mention est passable")
elif moyenne < 14:
    print(f"la moyenne obtenue est {moyenne} et la mention est assez-bien")
else:
    print(f"la moyenne obtenue est {moyenne} et la mention est bien")
