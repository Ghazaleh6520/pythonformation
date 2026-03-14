
import random
import string

# demander la longueur du mot de passe
longueur = int(input("Longueur du mot de passe : "))

# lettres + chiffres
caracteres = string.ascii_letters + string.digits

# caractères spéciaux UTF-8
caracteres_speciaux = "éèàçùô€£¥§@#&!*?"

# ajouter les caractères spéciaux
caracteres += caracteres_speciaux

# générer le mot de passe
mot_de_passe = ""

for i in range(longueur):
    mot_de_passe += random.choice(caracteres)

print("Mot de passe généré :", mot_de_passe)