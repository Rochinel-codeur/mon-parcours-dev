# Brin d'ADN complementaire

n = int(input("entrer la longueur de la chaine : "))
nucleotide = []
for i in range(n):
    base = input(f"entrer la base N° {i + 1} : ")
    if base == "A":
        nucleotide.append("T")
    elif base == "T":
        nucleotide.append("A")
    elif base == "C":
        nucleotide.append("G")
    elif base == "G":
        nucleotide.append("C")
print(nucleotide)
