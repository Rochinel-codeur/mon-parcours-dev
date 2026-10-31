"""Chapitre 3 : tests et conditions (if, elif, else, break, continue)."""

from menu import lancer


def jours_de_la_semaine():
    """Au travail ou au repos ?"""
    semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    for jour in semaine:
        if jour in ["lundi", "mardi", "mercredi", "jeudi"]:
            print("Au travail")
        elif jour == "vendredi":
            print("chouette")
        else:
            print("Au repos")


def brin_complementaire():
    """Brin d'ADN complementaire"""
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


def minimum_d_une_liste():
    """Trouver le minimum sans min()"""
    liste = [8, 4, 6, 1, 5]
    plus_petit = liste[0]
    for i in liste:
        if i < plus_petit:
            plus_petit = i
    print(plus_petit)


def frequence_des_acides_amines():
    """Frequence des acides amines"""
    sequence = ["R", "A", "W", "W", "A", "W", "A", "R", "W", "W", "R", "A", "G"]
    numR = numW = numA = numG = 0
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


def notes_et_mention():
    """Minimum, maximum, moyenne et mention"""
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


def nombres_pairs_et_impairs():
    """Pairs < 10 et impairs > 10"""
    for i in range(21):
        if i % 2 == 0 and i < 10:
            print(i)
        elif i % 2 != 0 and i > 10:
            print(i)


def conjecture_de_syracuse():
    """Conjecture de Syracuse"""
    n = int(input("entrer le nombre de depart : "))
    print(n)
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        print(n)


def helice_alpha():
    """Acides amines en helice alpha"""
    acides = [[48.6, 53.4], [-124.9, 156.7], [-66.2, -30.8],
              [-58.8, -43.1], [-73.9, -40.6], [-53.7, -37.5],
              [-80.6, -26.0], [-68.5, 135.0], [-64.9, -23.5],
              [-66.9, -45.5], [-69.6, -41.0], [-62.7, -37.5],
              [-68.2, -38.3], [-61.2, -49.1], [-59.7, -41.1]]
    for phi, psi in acides:
        if -87 < phi < -27 and -77 < psi < -17:
            print(f"[{phi}, {psi}] est en helice")
        else:
            print(f"[{phi}, {psi}] n'est pas en helice")


def nombres_premiers():
    """Nombres premiers inferieurs a 100 (avec break)"""
    nombres = 0
    for i in range(2, 100):
        premier = True
        for j in range(2, i):
            if i % j == 0:
                premier = False
                break
        if premier:
            nombres += 1
    print(f"le nombre de nombres premiers est {nombres}")


def deviner_un_nombre():
    """L'ordinateur devine ton nombre (dichotomie)"""
    print("choisis un nombre entre 1 et 100 dans ta tete")
    minimum = 1
    maximum = 100
    trouve = False
    tentatives = 0
    while not trouve:
        milieu = (minimum + maximum) // 2
        tentatives += 1
        print(f"le nombre que je choisis est le {milieu}")
        reponse = input("est-ce que c'est plus petit (-), plus grand (+) ou egal (=) ? ")
        if reponse == "-":
            maximum = milieu - 1
        elif reponse == "+":
            minimum = milieu + 1
        elif reponse == "=":
            trouve = True
        else:
            print("reponse invalide")
    print(f"le nombre est {milieu} et le nombre de tentatives est {tentatives}")


if __name__ == "__main__":
    lancer([
        jours_de_la_semaine, brin_complementaire, minimum_d_une_liste,
        frequence_des_acides_amines, notes_et_mention, nombres_pairs_et_impairs,
        conjecture_de_syracuse, helice_alpha, nombres_premiers, deviner_un_nombre,
    ])
