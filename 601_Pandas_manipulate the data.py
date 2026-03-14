import pandas as pd  # Convention d'import

# Charger le fichier CSV
df = pd.read_csv("departement.csv")

# Afficher les 5 premières lignes
print("Aperçu des données :")
print(df.head())

# Résumé des colonnes et types de données
print("\nRésumé des colonnes :")
print(df.info())

# Statistiques descriptives (si les colonnes sont numériques)
print("\nStatistiques descriptives :")
print(df.describe())
