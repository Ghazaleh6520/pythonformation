chemin="C:/Users/ghazaleh.eidivandi/OneDrive - Interpublic/Desktop/Python_formation/fichier.txt"

#autre méthode:
with open(chemin,"r",encoding="utf-8")as f:
    contenu=f.read()#essayer avec et sans repr()
    print(contenu)
    f.seek(0) #Remet le curseur au début
    contenu2=f.readlines()
    print(contenu2)
    f.seek(0) #Remet le curseur au début
    contenu3=f.read().splitlines() #enlèveles \n(retour à la ligne
    print(contenu3)