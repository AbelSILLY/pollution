import requests
import json
import plotly.graph_objects as go
from datetime import datetime

# Remplacez l'URL par celle que vous avez fournie
url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/donnees-synop-essentielles-omm/records?limit=100&refine=nom%3A%22MONTPELLIER%22"

# Effectuer la requête HTTP
response = requests.get(url)

# Gérer les erreurs
if response.status_code == 200:
    # Charger les données JSON
    weather_data = response.json()

    # Préparer les données pour le graphique
    months_data = {i: {"sunshine_hours": [], "temperature": []} for i in range(1, 13)}  # Inclure tous les mois

    for result in weather_data["results"]:
        # Convertir la date au format datetime
        date = datetime.fromisoformat(result["date"].split("+")[0])

        month = date.month

        # Accumuler les heures d'ensoleillement et les températures pour chaque mois
        if "vv" in result:
            sunshine_hours = result["vv"] / 3600  # vv est en secondes, convertir en heures
            months_data[month]["sunshine_hours"].append(sunshine_hours)
        else:
            months_data[month]["sunshine_hours"].append(0)

        if "t" in result:
            temperature = result["t"] - 273.15  # Convertir la température de Kelvin à Celsius
            months_data[month]["temperature"].append(temperature)
        else:
            months_data[month]["temperature"].append(0)

    # Calculer les moyennes pour chaque mois
    average_sunshine_hours = [sum(data["sunshine_hours"]) / len(data["sunshine_hours"]) if data["sunshine_hours"] else 0 for data in months_data.values()]
    average_temperature = [sum(data["temperature"]) / len(data["temperature"]) if data["temperature"] else 0 for data in months_data.values()]

    # Convertir la plage en liste avec juillet et août
    x_values = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Créer le graphique interactif avec plotly
    fig = go.Figure()

    # Ajouter la trace pour l'ensoleillement à l'axe de gauche
    fig.add_trace(go.Scatter(x=x_values, y=average_sunshine_hours, mode='lines+markers', name='Ensoleillement', yaxis='y', line=dict(color='green')))

    # Ajouter la trace pour la température à l'axe de droite
    fig.add_trace(go.Scatter(x=x_values, y=average_temperature, mode='lines+markers', name='Température', yaxis='y2', line=dict(color='red')))

    # Ajuster les propriétés du layout pour les deux axes
    fig.update_layout(
        title="Moyenne de la quantité d'ensoleillement et de la température par mois",
        xaxis=dict(title="Mois de l'année"),
        yaxis=dict(title="Ensoleillement (heures)", color='green'),
        yaxis2=dict(title="Température (°C)", color='red', overlaying='y', side='right'),
        showlegend=True
    )

    fig.show()

else:
    print(f"Échec de la requête avec le code d'état {response.status_code}")
    print(response.text)  # Affiche le contenu de la réponse pour déboguer





