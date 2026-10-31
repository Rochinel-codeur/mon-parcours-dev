# Construire les nombres pairs a partir des impairs

impairs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
pairs = []
for i in range(len(impairs)):
    pairs.append(impairs[i] + 1)
print(pairs)
