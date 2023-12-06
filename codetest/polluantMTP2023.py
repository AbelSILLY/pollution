import requests
import json
import pandas as pd
import plotly.express as px
from datetime import datetime

url = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_mensuelle_poll_princ/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"

# Envoyer une requête GET à l'URL
response = requests.get(url)

# Vérifier si la requête a réussi (statut 200)
if response.status_code == 200:
    # Charger les données JSON
    data = response.json()

    # Liste des polluants que vous voulez visualiser
    polluants = ['NO2', 'NOX', 'PM2.5', 'NO', 'PM10', 'O3']

    # Créer un DataFrame pandas à partir des données
    df = pd.DataFrame()

    # Parcourir toutes les entités
    for feature in data['features']:
        nom_polluant = feature['properties']['nom_poll']
        nom_com = feature['properties']['nom_com']

        # Vérifier si le polluant fait partie de ceux que vous voulez visualiser et si la ville est Montpellier
        if nom_polluant in polluants and nom_com == 'MONTPELLIER':
            date_debut_timestamp = feature['properties']['date_debut'] / 1000  # Convertir en secondes
            date_debut = datetime.utcfromtimestamp(date_debut_timestamp)

            # Filtrer les données pour les mois de janvier à novembre 2023
            if date_debut.year == 2023 and date_debut.month in range(1, 12):
                date_debut_str = date_debut.strftime('%Y-%m')
                valeur_polluant = feature['properties']['valeur']

                # Ajouter les données au DataFrame
                df = pd.concat([df, pd.DataFrame({nom_polluant: [valeur_polluant]}, index=[date_debut_str])])

    # Convertir les colonnes de dates en format de date pandas
    df.index = pd.to_datetime(df.index)

    # Trier les données par date
    df = df.sort_index()

    # Grouper par mois et calculer la moyenne
    df_moyenne_mensuelle = df.resample('M').mean()

    # Utiliser Plotly Express pour créer un graphe interactif
    fig = px.line(df_moyenne_mensuelle, x=df_moyenne_mensuelle.index, y=polluants,
                  labels={'value': 'Moyenne de la quantité de polluant', 'index': 'Mois de l\'année 2023'},
                  title='Évolution de la moyenne mensuelle de polluants à Montpellier en 2023')

    # Faire pivoter les étiquettes d'axe x pour une meilleure lisibilité
    fig.update_layout(xaxis=dict(tickangle=45, tickmode='array', tickvals=df_moyenne_mensuelle.index))

    # Afficher le graphe interactif
    fig.show()

else:
    print(f"La requête a échoué avec le statut : {response.status_code}")
