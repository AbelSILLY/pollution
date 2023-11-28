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

NOx = final_df['attributes.nox_kg'].sum()#somme du polluant NOx
CO = final_df['attributes.co_kg'].sum()
SO2 = final_df['attributes.so2_kg'].sum()
covnm = final_df['attributes.covnm_kg'].sum()
NH3 = final_df['attributes.nh3_kg'].sum()
CO2 = final_df['attributes.co2_t'].sum()

#vecteur des sommes des polluants
vect_pollu = [NOx,CO,SO2,covnm,NH3,CO2]

polluants = ["attributes.nox_kg",
             "attributes.co_kg",
             "attributes.so2_kg",
             "attributes.covnm_kg",
            "attributes.nh3_kg",
            "attributes.co2_t"]

              
#création d'un graphique en camembert
plt.pie(vect_pollu, labels = polluants, autopct='%1.1f%%')
plt.title("La concentracion des principaux polluants entre 2016 et 2019")

# On enregistre en formats svg
plt.savefig("La concentracion des principaux polluants entre 2016 et 2019.svg",format = 'svg')

#on affiche le grafique
plt.show()