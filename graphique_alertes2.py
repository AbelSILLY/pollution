import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
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
    date_ech = properties.get('date_ech', '')
    
    # Ajout des informations sur les polluants responsables (à ajuster si ces informations sont disponibles)
    code_pol = properties.get('code_pol', '')
    lib_pol = properties.get('lib_pol', '')

    # Vérifier si la date est présente
    if date_ech:
        date_ech = datetime.fromtimestamp(date_ech / 1000).strftime('%m/%d/%Y')  # Format mois/jour/année (américain)

    data_list.append({'lib_zone': lib_zone, 'etat': etat, 'date_ech': date_ech, 'coordinates': tuple(coordinates),
                      'code_pol': code_pol, 'lib_pol': lib_pol})

df = pd.DataFrame(data_list)

# Filtrer les lignes où l'état est "ALERTE"
df_alertes = df[df['etat'] == 'ALERTE']

# Ajouter une colonne avec les dates pour les alertes
df_alertes['date_ech'] = pd.to_datetime(df_alertes['date_ech'], errors='coerce')
df_alertes['month_year'] = df_alertes['date_ech'].dt.to_period('M')

# Créer un graphique à barres empilées avec délimitations entre les départements
plt.figure(figsize=(16, 8))
sns.countplot(x='lib_zone', hue='month_year', data=df_alertes, palette='viridis', dodge=True)
plt.title('Nombre d\'Alertes par Département et par Mois')
plt.xlabel('Département')
plt.ylabel("Nombre d'Alertes")
plt.xticks(rotation=45, ha='right')

# Ajouter des délimitations entre les départements
for i in range(len(df_alertes['lib_zone'].unique())):
    plt.axvline(x=i - 0.5, color='black', linestyle='--', linewidth=1)

# Afficher le graphique sans l'enregistrer
plt.show()
