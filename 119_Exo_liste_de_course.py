liste_de_course = ["pain", "mayonnaise", "poisson"]

while True:
    print("\n--- MENU ---")
    print("1 - Ajouter un élément")
    print("2 - Retirer un élément")
    print("3 - Afficher la liste")
    print("4 - Vider la liste")
    print("5 - Quitter")

    choix = input("Choisissez une option : ")

    if choix == "1":
        element = input("Quel élément ajouter ? ")
        liste_de_course.append(element)
        print("Élément ajouté.")

    elif choix == "2":
        element = input("Quel élément retirer ? ")
        if element in liste_de_course:
            liste_de_course.remove(element)
            print("Élément retiré.")
        else:
            print("Cet élément n'est pas dans la liste.")

    elif choix == "3":
        print("Liste de courses :", liste_de_course)

    elif choix == "4":
        liste_de_course.clear()
        print("La liste est maintenant vide.")

    elif choix == "5":
        print("Au revoir !")
        break

    else:
        print("Choix invalide.")