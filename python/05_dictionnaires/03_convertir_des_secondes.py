# Convertir des secondes en heures, minutes et secondes

secondes = int(input("entrer le nombre de secondes a convertir : "))
heures = secondes // 3600
secondes = secondes - heures * 3600
minutes = secondes // 60
secondes = secondes - minutes * 60
print(f"cela correspond a {heures} heures {minutes} minutes et {secondes} secondes")
