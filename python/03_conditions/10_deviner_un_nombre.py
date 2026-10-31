# L'ordinateur devine ton nombre (recherche par dichotomie)

print("choisis un nombre entre 1 et 100 dans ta tete")
minimum = 1
maximum = 100
trouve = False
tentatives = 0

while trouve == False:
    milieu = (minimum + maximum) // 2
    tentatives += 1
    print(f"le nombre que je choisis est le {milieu}")
    reponse = input("est-ce que c'est plus petit (-), plus grand (+) ou egal (=) ? ")
    if reponse == "-":
        maximum = milieu - 1
    elif reponse == "+":
        minimum = milieu + 1
    elif reponse == "=":
        trouve = True
    else:
        print("reponse invalide")

print(f"le nombre est {milieu} et le nombre de tentatives est {tentatives}")
