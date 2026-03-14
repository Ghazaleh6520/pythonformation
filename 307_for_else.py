liste=["pierre","Hugo","Jean","Marc"]

for prenom in liste:
    if prenom=="Hugo":
        print("Hugo a été trouvé !")
        break
    else:
        print("Hugo est introuvable...")


#supprimer "Hugo" de la liste et ré-essayer
#le principe de for est de parcourir tous les elements dans une liste