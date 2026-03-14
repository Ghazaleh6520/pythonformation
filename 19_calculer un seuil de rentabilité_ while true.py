a=20 #prix de la carte
b=10 #prix normal d'une place
c=7 #prix réduit avec la carte

#resultat final attendu: après combien de places la carte d'abonnement est rentable?

places = 0

while True:
    places += 1
    
    prix_sans_carte = places * b
    prix_avec_carte = a + places * c
    
    if prix_avec_carte < prix_sans_carte:
        break

print("La carte devient rentable après", places, "places.")