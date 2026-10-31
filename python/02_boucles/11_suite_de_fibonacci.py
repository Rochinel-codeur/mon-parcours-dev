# Suite de Fibonacci

n = int(input("entrer le terme n (au moins 2) : "))
x0 = 0
x1 = 1
for i in range(2, n + 1):
    x0, x1 = x1, x0 + x1
print(x1)
print(x1 / x0)  # se rapproche du nombre d'or (1.618...)
