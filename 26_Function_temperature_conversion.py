def fahrenheit_vers_celsius(f):
    c = (f - 32) * 5 / 9
    return c

# utilisation de la fonction
temperature_f = float(input("Entrez la température en Fahrenheit : "))

temperature_c = fahrenheit_vers_celsius(temperature_f)

print("La température en Celsius est :", temperature_c)