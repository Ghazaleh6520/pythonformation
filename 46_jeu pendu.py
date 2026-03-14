import random
import unicodedata


def enlever_accents(texte):
    """Remplace les caractères accentués par leurs équivalents sans accent."""
    texte_normalise = unicodedata.normalize("NFD", texte)
    return "".join(c for c in texte_normalise if unicodedata.category(c) != "Mn")


def charger_mots(fichier):
    """
    Lit un fichier texte (1 mot par ligne), enlève les accents,
    met en minuscules et garde seulement les mots de 6 lettres ou plus.
    """
    mots_valides = []

    with open(fichier, "r", encoding="utf-8") as f:
        for ligne in f:import random

# ouvrir le fichier et lire les mots
with open("mots.txt", "r", encoding="utf-8") as f:
    mots = f.read().splitlines()

# garder seulement les mots de 6 lettres ou plus
mots_valides = []
for mot in mots:
    if len(mot) >= 6:
        mots_valides.append(mot.lower())

# choisir un mot au hasard
mot = random.choice(mots_valides)

lettres_trouvees = []
lettres_choisies = []
erreurs = 0

while erreurs < 10:

    # afficher le mot masqué
    affichage = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            affichage += lettre + " "
        else:
            affichage += "_ "

    print("\nMot :", affichage)

    lettre = input("Entrez une lettre : ").lower()

    # vérifier entrée
    if len(lettre) != 1 or not lettre.isalpha():
        print("Entrez une seule lettre")
        continue

    if lettre in lettres_choisies:
        print("Déjà choisi")
        continue

    lettres_choisies.append(lettre)

    if lettre in mot:
        lettres_trouvees.append(lettre)
        print("Bonne lettre !")
    else:
        erreurs += 1
        print("Erreur :", erreurs, "/10")

    # vérifier victoire
    gagne = True
    for lettre in mot:
        if lettre not in lettres_trouvees:
            gagne = False

    if gagne:
        print("\nMot :", mot)
        print("Gagné !")
        break

if erreurs == 10:
    print("\nGame Over")
    print("Le mot était :", mot)