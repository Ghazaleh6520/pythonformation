chemin="C:/Users/ghazaleh.eidivandi/OneDrive - Interpublic/Desktop/Python_formation/fichier.txt"
#mode r:read
f = open(chemin,"r")
print(f)

#lire le contenu
contenu=f.read()
print(contenu)

#fermer le fichier
f.close()