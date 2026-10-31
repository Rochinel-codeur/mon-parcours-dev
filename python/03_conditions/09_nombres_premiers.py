# Nombres premiers inferieurs a 100 (avec break)

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
