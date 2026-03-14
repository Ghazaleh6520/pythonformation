carte = 20
plein = 10
reduit = 7

places = 0

while (carte + (places * reduit)) > (places * plein):
  places += 1
  print(places)

places = places + 1
print(f"Avec une carte a {carte}€, Il faut acheter au moins {places} places")