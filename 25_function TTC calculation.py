
def calcul_ttc(prix_ht, taux):
    resultat = prix_ht * (1 + taux)
    return resultat

# utilisation de la fonction
prix_ht = float(input("Entrez le prix HT : "))
taux = 0.20   # 20 %

prix_ttc = calcul_ttc(prix_ht, taux)

print("Le prix TTC est :", prix_ttc)