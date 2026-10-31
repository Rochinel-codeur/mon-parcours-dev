"""Chapitre 2 : listes et boucles (for, while, range, enumerate)."""

import random

from menu import lancer


def parcourir_une_liste():
    """Parcourir une liste de 4 facons"""
    animaux = ["vache", "souris", "levure", "bacterie"]
    for animal in animaux:
        print(animal)
    for i in range(len(animaux)):
        print(animaux[i])
    for i, animal in enumerate(animaux):
        print(f"l'animal {i} est un {animal}")
    i = 0
    while i < len(animaux):
        print(animaux[i])
        i += 1


def jours_de_la_semaine():
    """Jours de la semaine (for puis while sur le week-end)"""
    semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    for jour in semaine:
        print(jour)
    i = 5
    while i < len(semaine):
        print(semaine[i])
        i += 1


def nombres_de_1_a_10():
    """Afficher les nombres de 1 a 10 sur une ligne"""
    for i in range(1, 11):
        print(i, end=" ")
    print()


def nombres_pairs():
    """Construire les nombres pairs a partir des impairs"""
    impairs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    pairs = []
    for i in range(len(impairs)):
        pairs.append(impairs[i] + 1)
    print(pairs)


def moyenne_des_notes():
    """Calculer une moyenne"""
    notes = [14, 9, 6, 8, 12]
    somme = 0
    for note in notes:
        somme = somme + note
    print(f"la moyenne est {somme / len(notes):.2f}")


def produit_des_pairs_consecutifs():
    """Produit de nombres pairs consecutifs"""
    entiers = list(range(2, 21, 2))
    for i in range(len(entiers) - 1):
        print(entiers[i] * entiers[i + 1])


def triangles_et_pyramide():
    """Triangles et pyramide d'etoiles"""
    n = int(input("entrer le nombre de lignes : "))
    for i in range(1, n + 1):
        print("*" * i)
    for i in range(n, 0, -1):
        print("*" * i)
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)
    for i in range(1, n + 1):
        espaces = n - i
        etoiles = 2 * i - 1
        print(" " * espaces + "*" * etoiles)


def parcours_de_matrice():
    """Parcours d'une matrice (for et while)"""
    N = int(input("entrer la dimension de la matrice : "))
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(f"{i:<4d} {j:4d}")

    # meme parcours avec des while
    i = 1
    while i <= N:
        j = 1
        while j <= N:
            print(f"nous sommes a la ligne {i} et a la colonne {j}")
            j += 1
        i += 1


def demi_matrice():
    """Demi-matrice sans la diagonale"""
    N = int(input("entrer la dimension de la matrice : "))
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            print(f"{i} {j}")


def saut_de_puce():
    """Saut de puce (marche aleatoire)"""
    position = 0
    sauts = 0
    while position != 5:
        position += random.choice([-1, 1])
        sauts += 1
    print("le nombre de sauts est :", sauts)


def suite_de_fibonacci():
    """Suite de Fibonacci"""
    n = int(input("entrer le terme n (au moins 2) : "))
    x0, x1 = 0, 1
    for i in range(2, n + 1):
        x0, x1 = x1, x0 + x1
    print(x1)
    print(x1 / x0)  # se rapproche du nombre d'or (1.618...)


if __name__ == "__main__":
    lancer([
        parcourir_une_liste, jours_de_la_semaine, nombres_de_1_a_10, nombres_pairs,
        moyenne_des_notes, produit_des_pairs_consecutifs, triangles_et_pyramide,
        parcours_de_matrice, demi_matrice, saut_de_puce, suite_de_fibonacci,
    ])
