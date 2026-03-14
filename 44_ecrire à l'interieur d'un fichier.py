chemin="fichier2.txt" #selon votre OS

with open(chemin,"w") as f:
    #on écrase write
    f.write("Bonjour2")

with open(chemin,"a") as f:
    #on ajouté add
    f.write("\nholiday")
