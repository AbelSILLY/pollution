import requests
import pandas as pd
import plotly.express as px
from datetime import datetime
from collections import defaultdict

# URL of the GeoJSON API for Montpellier
url = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_annuelle_poll_princ/FeatureServer/0/query?outFields=*&where=nom_com='MONTPELLIER'&f=geojson"

# Get GeoJSON data from the API
response = requests.get(url)
data = response.json()

# Extract relevant data for Montpellier
features = data['features']
montpellier_data = [feature['properties'] for feature in features]

# Prepare data for plotting
pollutants_per_year = defaultdict(list)

for entry in montpellier_data:
    pollutant = entry['nom_poll']
    concentration = entry['valeur']
    date_debut_timestamp = entry['date_debut']
    year = datetime.utcfromtimestamp(date_debut_timestamp / 1000).year

    pollutants_per_year[pollutant].append((year, concentration))

# Transform data for plotting (calculate average concentration per year)
for pollutant, data in pollutants_per_year.items():
    data.sort(key=lambda x: x[0])

    # Calculate average concentrations per year
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

# Create a DataFrame for Plotly Express
df = pd.DataFrame([(pollutant, year, concentration) for pollutant, data in pollutants_per_year.items() for year, concentration in data],
                  columns=['Pollutant', 'Year', 'Concentration'])

# Plotting with Plotly Express
fig = px.line(df, x='Year', y='Concentration', color='Pollutant', markers=True, line_group='Pollutant',
              labels={'Concentration': 'Concentration', 'Year': 'Année'},
              title='Concentration des polluants à Montpellier par année',
              template='plotly', height=600)

# Show the interactive plot
fig.show()
