import json

chemin = r"C:\Users\ghazaleh.eidivandi\OneDrive - Interpublic\Desktop\Python_formation\Json.fichier"

# écrire une liste dans le fichier JSON
with open(chemin, "w") as f:
    json.dump(["Bonjour", list(range(10))], f, indent=4)


# lire le fichier
with open(chemin, "r") as f:
    liste = json.load(f)

print(liste)