import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Récupérer les données depuis l'URL
url = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/epipol_occitanie/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"
response = requests.get(url)
data = response.json()

# Créer un DataFrame Pandas à partir des données GeoJSON
features = data.get('features', [])
data_list = []

for feature in features:
    properties = feature.get('properties', {})
    geometry = feature.get('geometry', {})
    coordinates = geometry.get('coordinates', [])
    lib_zone = properties.get('lib_zone', '')
    etat = properties.get('etat', '')

    data_list.append({'lib_zone': lib_zone, 'etat': etat, 'coordinates': tuple(coordinates)})

df = pd.DataFrame(data_list)

# Filtrer les lignes où l'état est "ALERTE"
df_alertes = df[df['etat'] == 'ALERTE']

# Compter le nombre d'alertes par département
alertes_counts = df_alertes['lib_zone'].value_counts()

# Visualiser le nombre d'alertes par département avec annotations
plt.figure(figsize=(12, 6))
ax = sns.countplot(x='lib_zone', data=df_alertes, palette='viridis')
plt.title('Nombre d\'Alertes par Département')
plt.xlabel('Département')
plt.ylabel("Nombre d'Alertes")
plt.xticks(rotation=45, ha='right')

# Ajouter les annotations (nombre d'alertes) au-dessus de chaque colonne
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='baseline', fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')

# Afficher le graphique sans l'enregistrer
plt.show()
