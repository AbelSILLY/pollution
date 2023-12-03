import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
import folium
from datetime import datetime, timedelta


# Liste des URL à récupérer
urls = [
    "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/fl_emi_occitanie_epci/FeatureServer/6/query?where=1%3D1&outFields=*&outSR=4326&f=json",
    "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/fl_emi_occitanie_epci/FeatureServer/7/query?where=1%3D1&outFields=*&outSR=4326&f=json",
    "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/fl_emi_occitanie_epci/FeatureServer/8/query?where=1%3D1&outFields=*&outSR=4326&f=json",
    "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/fl_emi_occitanie_epci/FeatureServer/9/query?where=1%3D1&outFields=*&outSR=4326&f=json"
]

# Initialisation d'une liste pour stocker les DataFrames
data_frames = []

# Temps d'attente maximal en secondes
timeout_seconds = 60


# Récupération des données JSON de chaque URL puis on les converti en DataFrame
for url in urls:
    start_time = datetime.now()
    response = requests.get(url)
    elapsed_time = datetime.now() - start_time
    
    # Vérification si le temps d'attente maximal est dépassé
    if elapsed_time.total_seconds() > timeout_seconds:
        print("Le téléchargement depuis l'URL {} a pris trop de temps. Passer à l'URL suivante.".format(url))
        continue

    data = response.json()
    features = data.get('features', [])
    if features:
        df = pd.json_normalize(features)
        data_frames.append(df)

        # Concaténation des DataFrames en un seul
final_df = pd.concat(data_frames, ignore_index=True)

# Liste des années à tracer
annees = [2016, 2017, 2018, 2019]

# Création d'un graphique pour chaque année
# la boucle for ici parcours la liste annees et crée un graphique pour chaque années
fig1, axs1 = plt.subplots(4, 1, figsize=(10, 16))
for i, annee in enumerate(annees):
    df_annee = final_df[final_df['attributes.annee_inv'] == annee]
    axs1[i].bar(df_annee.index, df_annee['attributes.nox_kg'], label='NOx')
    axs1[i].bar(df_annee.index, df_annee['attributes.co_kg'], label='CO', alpha=0.5)
    axs1[i].set_title('Concentration de gaz pour l\'année {}'.format(annee))
    axs1[i].set_xlabel('Index')
    axs1[i].set_ylabel('Concentration de gaz')
    axs1[i].legend()

plt.tight_layout()

plt.show()