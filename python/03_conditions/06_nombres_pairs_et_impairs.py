# Nombres pairs inferieurs a 10 et impairs superieurs a 10

for i in range(21):
    if (i % 2 == 0) and (i < 10):
        print(i)
    elif (i % 2 != 0) and (i > 10):
        print(i)
