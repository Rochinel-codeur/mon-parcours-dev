"""Petit menu commun : chaque chapitre liste ses exercices et on choisit lequel lancer."""


def lancer(exercices):
    while True:
        print("\nExercices disponibles :")
        for i, exercice in enumerate(exercices, start=1):
            print(f"  {i}. {exercice.__doc__}")
        print("  0. Quitter")

        choix = input("Ton choix : ")
        if choix == "0":
            break
        if choix.isdigit() and 1 <= int(choix) <= len(exercices):
            print()
            exercices[int(choix) - 1]()
        else:
            print("Choix invalide")
