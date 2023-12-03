import requests
import pandas as pd
import matplotlib.pyplot as plt
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

# Plotting
for pollutant, data in pollutants_per_year.items():
    years, concentrations = zip(*data)
    plt.plot(years, concentrations, marker='o', linestyle='-', linewidth=1, label=pollutant)

plt.title('Concentration des polluants à Montpellier par année')
plt.xlabel('Année')
plt.ylabel('Concentration')
plt.legend(title='Pollutant', loc='upper right')
plt.show()
