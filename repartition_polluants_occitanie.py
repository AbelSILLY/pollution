import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
import requests

# initialisation d'un dataframe à partir d'un fichier local contenant les géométries (polygone) de l'Occitanie
couche = gpd.read_file("le_chemin_du_fichier\polyg_geom.geojson")

# affichage des 5 premières lignes afin d'avoir un aperçu des données
couche.head()

# initialisation d'un nouveau dataframe à partir d'un URL (ATMO) pour les données de pollutions
geopollu = gpd.read_file("https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_72h_poll_princ/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson")

# affichage du dataframe
geopollu.head()

# ici on reassigne la colone geometry du datafrafe couche au datataframe geopollu et on le renomme polyg_geom
geopollu = geopollu.assign(polyg_geom=couche['geometry'])
geopollu.head()

# geopollu.drop('geometry', axis=1, inplace=True)(cette ligne permet de supprimer la colone geometry du dataframe geopollu)

# première affichage (carte de l'Occitanie)
# ici "polyg_geom" est notre colonne géométrique, "geometry" est aussi une colone géométrique sous forme de points
geopollu = geopollu.set_geometry('polyg_geom')

# Création d'une figure et des axes
fig, ax = plt.subplots(figsize=(7, 6))

# Maintenant, vous pouvez utiliser la colonne géométrique pour le tracé 
geopollu.plot(ax=ax, column='nom_poll',cmap='Spectral', figsize=(7,6), legend=True)

# Ajouter le légende
ax.set_title('Répartition des polluants en Occitanie')
plt.show()

