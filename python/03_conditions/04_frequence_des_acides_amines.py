# Frequence des acides amines

sequence = ["R", "A", "W", "W", "A", "W", "A", "R", "W", "W", "R", "A", "G"]

numR = 0
numW = 0
numA = 0
numG = 0
for i in sequence:
    if i == "R":
        numR += 1
    elif i == "W":
        numW += 1
    elif i == "A":
        numA += 1
    elif i == "G":
        numG += 1

print(f"le pourcentage d'alanine est : {numA / len(sequence) * 100:.1f}%")
print(f"le pourcentage d'arginine est : {numR / len(sequence) * 100:.1f}%")
print(f"le pourcentage de tryptophane est : {numW / len(sequence) * 100:.1f}%")
print(f"le pourcentage de glycine est : {numG / len(sequence) * 100:.1f}%")
