# Saut de puce (marche aleatoire)

import random

position = 0
sauts = 0
while position != 5:
    deplacement = random.choice([-1, 1])
    position += deplacement
    sauts += 1
print("le nombre de sauts est :", sauts)
