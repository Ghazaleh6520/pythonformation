a=int(input("Entrez un nombre"))
b=int(input("Entrez un nombre"))
print("choissisez le type d'operation")
print("1 addition")
print("2 soustraction")
print("3 multiplication")
print("4 division")

type_operation = input("entrez un type d'operation ( 1 2 3 ou 4) ")

if type_operation == ("1"):
    print ( a+b )

if type_operation == ("2"):
    print( a-2 )

if  type_operation == ( "3"):
    print ( a*b )
else:
    print( a/b )




