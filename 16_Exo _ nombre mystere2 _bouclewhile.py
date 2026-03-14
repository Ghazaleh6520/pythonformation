import random

nombre_mystere = random.randint (0,100) 
nombre_choisi = 0


while nombre_choisi != nombre_mystere:
    nombre_choisi= int(input("Entrez un nombre:"))
    if nombre_choisi > nombre_mystere:
        print("trop haut")
    elif nombre_choisi < nombre_mystere:
         print("trop bas")


print("fin")
