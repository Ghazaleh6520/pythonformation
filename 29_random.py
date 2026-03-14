import random #importer le module random
nombre_hasard=random.randint(1,50)

#choisir aléatoirement un élément d'un tableau
mon_tableau = [1,2,3,4,5]
element_aleatoire=random.choice(mon_tableau)

print(element_aleatoire)