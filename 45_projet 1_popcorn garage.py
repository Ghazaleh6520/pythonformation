films = [
    "Matrix",
    "Dracula",
    "Scream",
    "Saw",
    "Hook",
    "Zorro",
    "Batman",
    "Watchman",
    "Avatar",
    "ET"
]

# convertir tous les films en minuscules
films = [film.lower() for film in films]

films_trouves = []
score = 0
erreurs = 0

print("Liste des films à trouver :")
print(films)
print()

while True:
    proposition = input("Entre un nom de film : ").lower()

    if proposition in films_trouves:
        print("Déjà trouvé")

    elif proposition in films:
        films_trouves.append(proposition)
        score += 1
        print("Bravo !")
        print("Score :", score)

    else:
        erreurs += 1
        print("Erreur :", erreurs, "/3")

    if erreurs == 3:
        print("Game Over")
        break

    if score == len(films):
        print("Bravo ! Tous les films trouvés")
        break
