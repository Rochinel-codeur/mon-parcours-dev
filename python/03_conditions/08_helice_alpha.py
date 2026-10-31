# Acides amines en helice alpha

acides = [[48.6, 53.4], [-124.9, 156.7], [-66.2, -30.8],
          [-58.8, -43.1], [-73.9, -40.6], [-53.7, -37.5],
          [-80.6, -26.0], [-68.5, 135.0], [-64.9, -23.5],
          [-66.9, -45.5], [-69.6, -41.0], [-62.7, -37.5],
          [-68.2, -38.3], [-61.2, -49.1], [-59.7, -41.1]]

for i in range(len(acides)):
    phi = acides[i][0]
    psi = acides[i][1]
    if (-27 > phi > -87) and (-17 > psi > -77):
        print(f"{acides[i]} est en helice")
    else:
        print(f"{acides[i]} n'est pas en helice")
