"""Chapitre 5 : dictionnaires et tuples."""

from menu import lancer


def moyenne_des_notes():
    """Moyenne des notes d'un dictionnaire"""
    dico_notes = {
        "math": 14, "programmation": 12,
        "anglais": 16, "biologie": 10,
        "sport": 19,
    }
    # moyenne sans la biologie
    somme = 0
    i = 0
    for matiere, note in dico_notes.items():
        if matiere == "biologie":
            continue
        somme += note
        i += 1
    print(f"la moyenne sans la biologie est {somme / i}")

    print(f"la moyenne generale est {sum(dico_notes.values()) / len(dico_notes)}")


def composition_d_une_sequence():
    """Compter les acides amines d'une sequence"""
    sequence = "AGWPSGGASAGLAILWGASAIM"
    composition = {}
    for acide in sequence:
        if acide in composition:
            composition[acide] += 1
        else:
            composition[acide] = 1
    print(composition)


def convertir_des_secondes():
    """Convertir des secondes en heures, minutes, secondes"""
    secondes = int(input("entrer le nombre de secondes a convertir : "))
    heures = secondes // 3600
    secondes = secondes - heures * 3600
    minutes = secondes // 60
    secondes = secondes - minutes * 60
    print(f"cela correspond a {heures} heures {minutes} minutes et {secondes} secondes")


def convertir_des_jours():
    """Convertir des jours en annees, mois, jours"""
    jours = int(input("entrer le nombre de jours a convertir : "))
    annees = jours // 365
    jours = jours - annees * 365
    mois = jours // 30
    jours = jours - mois * 30
    print(f"cela correspond a {annees} ans {mois} mois et {jours} jours")


def proprietes_des_acides_amines():
    """Proprietes des acides amines d'une sequence"""
    aa2prop = {"A": "a", "V": "a", "L": "a", "G": "a", "I": "a", "M": "a",
               "W": "a", "F": "a", "P": "a",
               "S": "p", "C": "p", "N": "p", "Q": "p", "T": "p", "Y": "p",
               "D": "-", "E": "-",
               "K": "+", "R": "+", "H": "+"}
    sequence = "SNADVVYEKQMLYLYVLSGIGG"
    proprietes = ""
    for acide in sequence:
        if acide in aa2prop:
            proprietes += aa2prop[acide]
    print(sequence)
    print(proprietes)


def liste_de_tuples():
    """Parcourir une liste de tuples"""
    liste = [("chien", 3), ("chat", 4), ("souris", 16)]
    for animal, nombre in liste:
        print(animal, nombre)


if __name__ == "__main__":
    lancer([
        moyenne_des_notes, composition_d_une_sequence, convertir_des_secondes,
        convertir_des_jours, proprietes_des_acides_amines, liste_de_tuples,
    ])
