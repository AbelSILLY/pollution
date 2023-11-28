import requests
import matplotlib.pyplot as plt

# Récupérer les données depuis l'URL
url = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/epipol_occitanie/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"
response = requests.get(url)
data = response.json()

# Analyser les données GeoJSON
features = data['features']

# Créer des structures de données pour stocker les informations nécessaires
department_data = {}

# Parcourir les entités (features) dans le GeoJSON
for feature in features:
    properties = feature['properties']

    # Extraire les informations pertinentes
    department = properties['lib_zone']
    pollution_level = properties['etat']

    # Stocker les informations dans la structure de données
    if department in department_data:
        department_data[department].append(pollution_level)
    else:
        department_data[department] = [pollution_level]

# Préparer les données pour le graphique
departments = list(department_data.keys())
occurrence_counts = [len(levels) for levels in department_data.values()]

# Créer un graphique en barres
fig, ax = plt.subplots()
bars = ax.bar(departments, occurrence_counts, color='skyblue')

# Ajouter des étiquettes aux barres
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

plt.xlabel('Département')
plt.ylabel('Nombre total d\'occurrences de pollution')
plt.title('Occurrences de Pollution par Département en Occitanie')
plt.xticks(rotation=45, ha='right')  # Rotation des étiquettes d'axe x pour une meilleure lisibilité
plt.tight_layout()

# Afficher le graphique sans l'enregistrer
plt.show()
