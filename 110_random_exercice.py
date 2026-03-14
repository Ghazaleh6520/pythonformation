import random
element_aleatoire=random.randint(0,10)


a=random.randrange(5)#est généré alréatoirement
print(a)

b=random.randrange(6)#est généré alréatoirement

if b > a:
    print("le nombre b est plus grand que le nombre a")

elif a > b:
    print("le nombre a est plus grand que le nombre b")
elif a==b:
    print("les chiffres sont egaux")
else:
    print("le cas non existant")