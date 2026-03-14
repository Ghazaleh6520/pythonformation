# permets de stocker des données sous forme de clé : valeur
dictionnaire={"prenom":"jacques","age":"25"}
"""
Imbricable comme les listes
les clés sont unique ( imposable d'avoir 2 clef " prenom" par exemple)
pour accéder à la valeur:
"""
print(dictionnaire["prenom"])

# ou
dictionnaire.get("prenom")#retourne une erreur si la clé n'existe pas