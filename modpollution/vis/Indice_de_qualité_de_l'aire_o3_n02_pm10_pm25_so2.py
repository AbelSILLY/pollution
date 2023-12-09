import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
import requests

# initialisation d'un dataframe à partir d'un fichier local contenant les géométries (polygone) de l'Occitanie
couche = gpd.read_file("C:\\Users\\BossdiDibosS\\Desktop\\pollution\\modpollution\\data\\polyg_geom.geojson")

# Définir l'URL
url = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/Indice_quotidien_de_qualité_de_l’air_pour_les_collectivités_territoriales_en_Occitanie/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"
# url = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_72h_poll_princ/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"

# Effectuer une requête pour récupérer les données GeoJSON
response = requests.get(url)
data = response.json()

# Créer un GeoDataFrame à partir des données GeoJSON
gdf = gpd.GeoDataFrame.from_features(data['features'])

# gdf = gdf.merge(couche[['geometry']], left_index=True, right_index=True, suffixes=('', '_couche'))
# geopollu = gdf.rename(columns={'geometry_couche': 'polyg_geom'})

# On assigne les colones 'geometry' et 'nom_officiel_departement' au geodataframe gdf
gdf = gdf.assign(geometry=couche['geometry'])
gdf = gdf.assign(nom_officiel_departement=couche['nom_officiel_departement'])

# Afficher les premières lignes du GeoDataFrame
gdf.head()


# Créer une figure avec deux sous-plots côte à côte
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Plot 1 : Carte avec la colonne 'code_o3'
axs[0].set_title('Carte - Code O3')
gdf.plot(column='code_o3', cmap='Spectral', linewidth=0.8, ax=axs[0], edgecolor='0.8', legend=True)

# Ajouter des étiquettes pour chaque département
for x, y, label in zip(gdf.geometry.centroid.x, gdf.geometry.centroid.y, gdf['nom_officiel_departement']):
    axs[0].annotate(label, xy=(x, y), xytext=(3, 3), textcoords='offset points')

# Plot 2 : Carte avec la colonne 'code_pm10'
axs[1].set_title('Carte - Code PM10')
gdf.plot(column='code_pm10', cmap='Spectral', linewidth=0.8, ax=axs[1], edgecolor='0.8', legend=True)

# Ajouter des étiquettes pour chaque département
for x, y, label in zip(gdf.geometry.centroid.x, gdf.geometry.centroid.y, gdf['nom_officiel_departement']):
    axs[1].annotate(label, xy=(x, y), xytext=(3, 3), textcoords='offset points')

# Ajuster l'espacement entre les sous-plots
plt.tight_layout()

# Afficher les plots
plt.show()


# Créer une figure avec deux sous-plots côte à côte
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Plot 1 : Carte avec la colonne 'code_no2'
axs[0].set_title('Carte - code no2')
gdf.plot(column='code_no2', cmap='Spectral', linewidth=0.8, ax=axs[0], edgecolor='0.8', legend=True)

# Ajouter des étiquettes pour chaque département
for x, y, label in zip(gdf.geometry.centroid.x, gdf.geometry.centroid.y, gdf['nom_officiel_departement']):
    axs[0].annotate(label, xy=(x, y), xytext=(3, 3), textcoords='offset points')

# Plot 2 : Carte avec la colonne 'code_pm25'
axs[1].set_title('Carte - code pm25')
gdf.plot(column='code_pm25', cmap='Spectral', linewidth=0.8, ax=axs[1], edgecolor='0.8', legend=True)

# Ajouter des étiquettes pour chaque département
for x, y, label in zip(gdf.geometry.centroid.x, gdf.geometry.centroid.y, gdf['nom_officiel_departement']):
    axs[1].annotate(label, xy=(x, y), xytext=(3, 3), textcoords='offset points')

# Ajuster l'espacement entre les sous-plots
plt.tight_layout()

# Afficher les plots
plt.show()


gdf = gdf.set_geometry('geometry')
# Création d'une figure et des axes
fig, ax = plt.subplots(1, 1, figsize=(5, 5))

# On trace les départements avec différentes couleurs en fonction de la quantité de polluant
ax.set_title('Carte - code so2')
gdf.plot(column='code_so2', cmap='Spectral', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
# gdf.plot(column='code_pm10', cmap='Spectral', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# On ajouter des étiquettes pour chaque département
for x, y, label in zip(gdf.geometry.centroid.x, gdf.geometry.centroid.y, gdf['nom_officiel_departement']):
    ax.annotate(label, xy=(x, y), xytext=(3, 3), textcoords='offset points')