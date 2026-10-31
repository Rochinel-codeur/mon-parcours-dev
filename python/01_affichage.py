"""Chapitre 1 : affichage, variables et formatage avec les f-strings."""

from menu import lancer


def premiers_print():
    """Premiers print et operations"""
    print("chat")
    print("souris")
    print(1 / 1)
    # print(int("deux"))  -> ValueError : "deux" n'est pas un nombre


def repetition_de_chaines():
    """Multiplier une chaine"""
    A = "A"
    X = "GC"
    print(A * 20 + " " + X * 20)


def f_strings():
    """Formater des variables avec une f-string"""
    a = "salut"
    b = 102
    c = 10.318
    print(f"{a} {b} {c:.2f}")


def pourcentage_gc():
    """Pourcentage de GC avec differentes precisions"""
    per_GC = ((4500 + 2575) / 14800) * 100
    print(f"Le pourcentage de GC est de {per_GC:<6.0f}%")
    print(f"Le pourcentage de GC est de {per_GC:<6.1f}%")
    print(f"Le pourcentage de GC est de {per_GC:<6.2f}%")
    print(f"Le pourcentage de GC est de {per_GC:<6.3f}%")


def division_euclidienne():
    """Division euclidienne (// et %)"""
    X = int(input("entrer le numerateur : "))
    Y = int(input("entrer le denominateur : "))
    print(f"{X // Y} + {X % Y}/{Y}")


if __name__ == "__main__":
    lancer([premiers_print, repetition_de_chaines, f_strings, pourcentage_gc, division_euclidienne])
