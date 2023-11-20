import requests
import folium
from datetime import datetime
from IPython.display import display
import os

# Récupérer les données depuis l'URL
url = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/epipol_occitanie/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"
response = requests.get(url)
data = response.json()

# Créer une carte centrée sur une position approximative en Occitanie
m = folium.Map(location=[43.6, 1.4], zoom_start=8)

# Créer un dictionnaire pour stocker le nombre d'alertes et les dates associées à chaque point
alerts_by_location = {}

# Ajouter des marqueurs rouges pour chaque alerte avec le nombre d'alertes et toutes les dates
features = data.get('features', [])
for feature in features:
    properties = feature.get('properties', {})
    geometry = feature.get('geometry', {})
    coordinates = geometry.get('coordinates', [])
    etat = properties.get('etat', '')
    date_ech = properties.get('date_ech', '')
    lib_zone = properties.get('lib_zone', '')

    # Vérifier si l'état est une alerte et si la date est présente
    if etat == 'ALERTE' and date_ech:
        date_str = datetime.fromtimestamp(date_ech / 1000).strftime('%m/%d/%Y')

        # Ajouter le nombre d'alertes et la date au dictionnaire associé aux coordonnées
        if tuple(coordinates) in alerts_by_location:
            alerts_by_location[tuple(coordinates)]['count'] += 1
            alerts_by_location[tuple(coordinates)]['dates'].append(date_str)
        else:
            alerts_by_location[tuple(coordinates)] = {'count': 1, 'dates': [date_str], 'lib_zone': lib_zone}

# Ajouter des marqueurs pour chaque point avec une taille de marqueur variable en fonction du nombre d'alertes
for coordinates, alert_info in alerts_by_location.items():
    count = alert_info['count']
    lib_zone = alert_info['lib_zone']
    dates = "<br>".join(alert_info['dates'])

    # La taille du marqueur est définie par le nombre d'alertes
    radius = count * 2  # Vous pouvez ajuster le facteur de multiplication pour obtenir la taille désirée

    popup_text = f"Nombre d'alertes : {count}<br>Dates : {dates}<br>Département : {lib_zone}"
    
    # Créer le marqueur avec une taille variable
    folium.CircleMarker(location=[coordinates[1], coordinates[0]], radius=radius, popup=popup_text, color='red', fill=True).add_to(m)

# Enregistrer la carte sur le bureau avec le nom "carteA.html"
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
map_path = os.path.join(desktop_path, "carteA.html")

# Enregistrer la carte sur le bureau
m.save(map_path)

# Afficher le chemin d'accès au fichier enregistré
print(f"La carte a été enregistrée sur votre bureau : {map_path}")

# Afficher la carte dans le notebook
display(m)
