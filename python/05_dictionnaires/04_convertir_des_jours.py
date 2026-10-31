# Convertir des jours en annees, mois et jours

jours = int(input("entrer le nombre de jours a convertir : "))
annees = jours // 365
jours = jours - annees * 365
mois = jours // 30
jours = jours - mois * 30
print(f"cela correspond a {annees} ans {mois} mois et {jours} jours")
