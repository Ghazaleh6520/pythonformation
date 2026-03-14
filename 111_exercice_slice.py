liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]

nombre_element_dans_la_liste = len(liste)
print(nombre_element_dans_la_liste)
# Les trois premiers employés ("Maxime", "Martine" et "Christopher")
trois_premiers = liste[:3]
print(trois_premiers)
# Les trois derniers employés ("Carlos", "Michael" et "Éric")
trois_derniers = liste[3:]
print(trois_derniers)
# Tous les employés sauf le premier et le dernier
liste_milieu = liste[1:-1]
print(liste_milieu)
# Le premier et le dernier employé 
premier_dernier = liste[::nombre_element_dans_la_liste-1]
print(premier_dernier)


