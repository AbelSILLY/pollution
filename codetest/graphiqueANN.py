import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# URL de l'API GeoJSON
url = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_annuelle_poll_princ/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"

# Obtenir les données GeoJSON depuis l'API
response = requests.get(url)
data = response.json()

# Convertir les données GeoJSON en un DataFrame pandas
features = data['features']
data_list = []

for feature in features:
    properties = feature['properties']
    data_list.append(properties)

df_polluants = pd.DataFrame(data_list)

# Convertir les colonnes de date au format datetime64[ns]
df_polluants['date_debut'] = pd.to_datetime(df_polluants['date_debut'], unit='ms')
df_polluants['date_fin'] = pd.to_datetime(df_polluants['date_fin'], unit='ms')

# Ajouter une colonne 'annee' en extrayant l'année de la colonne 'date_debut'
df_polluants['annee'] = df_polluants['date_debut'].dt.year

# Créer un graphique à barres empilées avec les années sur l'axe des abscisses
plt.figure(figsize=(16, 8))
sns.barplot(x='annee', y='valeur', hue='nom_poll', data=df_polluants, palette='Set1', ci=None)

plt.title('Quantité de chaque polluant pour toutes les années')
plt.xlabel('Année')
plt.ylabel('Quantité de polluants')
plt.legend(title='Polluant', loc='upper right')
plt.show()
