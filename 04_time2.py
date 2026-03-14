
import time

#jour et mois en francais ( a mettre au début):
import locale

#temps écoulé depuis le 1er janvier 1970
#temps détaillé
print(time.localtime())

#afficher le jour de la semaine
print(time.strftime("%A %d %b %Y"))
print(time.strftime("format, time object"))

print("the date is", time.strftime("%d"),time.strftime("%A"))

      
