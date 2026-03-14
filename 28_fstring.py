#ne modifiez pas les vairables ci-dessous
protocole="https://"
nom_du_site="docstring"
extension="fr"
page="glossaire"


#modfiez le code à partir d'ici
#résultat attendu: https://www.docstring.fr/glossaire
URL = f"{protocole}WWW.{nom_du_site}.{extension}/{page}/"
print(URL)