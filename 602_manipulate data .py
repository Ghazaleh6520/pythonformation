import pandas as pd  # Convention d'import

# Charger le fichier CSV
df = pd.read_csv("departement.csv")

# Supprimer les doublons
df = df.drop_duplicates()

# Remplacer les valeurs manquantes par la moyenne (pour une colonne numérique)
# df['densite'] = df['densite'].fillna(df['densite'].mean())

# Vérifier les valeurs manquantes restantes
print("\nValeurs manquantes après nettoyage :")
print(df.isnull().sum())