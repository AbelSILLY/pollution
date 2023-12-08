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

# ici "polyg_geom" est notre colonne géométrique
geopollu = geopollu.set_geometry('polyg_geom')

# On supprimez les lignes avec des géométries nulles
geopollu = geopollu.dropna(subset=['polyg_geom'])

# Création d'une figure et des axes
fig, ax = plt.subplots(1, 1, figsize=(12, 8))

# On trace les départements avec différentes couleurs en fonction de la quantité de polluant
geopollu.plot(column='valeur', cmap='Spectral', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# On ajouter des étiquettes pour chaque département
for x, y, label in zip(geopollu.geometry.centroid.x, geopollu.geometry.centroid.y, geopollu['nom_dept']):
    ax.annotate(label, xy=(x, y), xytext=(3, 3), textcoords='offset points')
 
# On ajoute l'unité des polluants
ax.text(0.5, -0.05, f"Unité: {geopollu['unite'].iloc[0]}", ha='center', va='center', transform=ax.transAxes, fontsize=12)

plt.title('Quantité de polluant par département')
plt.show()

# Enregistrer le plot en tant que fichier SVG
fig.savefig('Quantité_de_polluant_par_département.svg', format='svg')