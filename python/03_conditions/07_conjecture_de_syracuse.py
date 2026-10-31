# Conjecture de Syracuse

n = int(input("entrer le nombre de depart : "))
print(n)
while n != 1:
    if n % 2 == 0:
        # n est pair : n // 2 donne un entier (8), alors que n / 2 donnerait 8.0
        n = n // 2
    else:
        n = n * 3 + 1
    print(n)
