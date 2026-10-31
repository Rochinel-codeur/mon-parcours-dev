# Proprietes des acides amines d'une sequence

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
