#%%
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime
from collections import defaultdict

# URL de l'API GeoJSON pour Montpellier
url = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_annuelle_poll_princ/FeatureServer/0/query?outFields=*&where=nom_com='MONTPELLIER'&f=geojson"

# Récupérer les données GeoJSON depuis l'API
response = requests.get(url)
data = response.json()

# Extraire les données pertinentes pour Montpellier
features = data['features']
montpellier_data = [feature['properties'] for feature in features]

# Préparer les données pour le tracé
pollutants_per_year = defaultdict(list)

for entry in montpellier_data:
    pollutant = entry['nom_poll']
    concentration = entry['valeur']
    date_debut_timestamp = entry['date_debut']
    year = datetime.utcfromtimestamp(date_debut_timestamp / 1000).year

    pollutants_per_year[pollutant].append((year, concentration))
#%%
year
#%%
# Transformer les données pour le tracé (calculer la concentration moyenne par année)
for pollutant, data in pollutants_per_year.items():
    data.sort(key=lambda x: x[0])

    # Calculer les concentrations moyennes par année
    averages_per_year = defaultdict(float)
    counts_per_year = defaultdict(int)

    for year, concentration in data:
        if concentration is not None:
            averages_per_year[year] += concentration
            counts_per_year[year] += 1

    for year in averages_per_year:
        if counts_per_year[year] > 0:
            averages_per_year[year] /= counts_per_year[year]

    pollutants_per_year[pollutant] = list(averages_per_year.items())
#%%
# Créer un DataFrame pour Plotly Express
df = pd.DataFrame([(pollutant, year, concentration) for pollutant, data in pollutants_per_year.items() for year, concentration in data],
                  columns=['Pollutant', 'Year', 'Concentration'])
df

#%%
# Tracé avec Plotly Express
fig = px.line(df, x='Year', y='Concentration', color='Pollutant', markers=True, line_group='Pollutant',
              labels={'Concentration': 'Concentration', 'Year': 'Année'},
              title='Concentration des polluants à Montpellier par année',
              template='plotly', height=600)
#%%
# Ajouter un curseur pour filtrer les données par année
fig.update_layout(
    xaxis=dict(
        rangeslider=dict(
            visible=True
        ),
        type='linear'  # Assurez-vous que le type d'axe x est 'linear' pour que le curseur fonctionne
    )
)
#%%
# Afficher le tracé interactif
fig.show()

# %%
