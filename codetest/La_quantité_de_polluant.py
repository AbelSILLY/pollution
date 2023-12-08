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

# Assurez-vous que la colonne géométrique est correctement définie
geopollu = geopollu.set_geometry('polyg_geom')

# Supprimez les lignes avec des géométries nulles
geopollu = geopollu.dropna(subset=['polyg_geom'])

# Création d'une figure et des axes
fig, ax = plt.subplots(figsize=(7, 7))

# On trace le GeoDataFrame
geopollu.plot(ax=ax, color='lightgrey', edgecolor='green')

# On ajoute des cercles proportionnels à la quantité de polluant
for idx, row in geopollu.iterrows():
    if row['polyg_geom']:
        ax.plot(row.polyg_geom.centroid.x, row.polyg_geom.centroid.y, 'ro', markersize=row['valeur'] * 0.1)
        # Ajouter le nom du département
        ax.text(row.polyg_geom.centroid.x, row.polyg_geom.centroid.y, row['nom_dept'], fontsize=8)


# Ajouter le légende
ax.set_title('La quantité de polluant')
plt.show()

# Enregistrer le plot en tant que fichier SVG
fig.savefig('La_quantité_de_polluant.svg', format='svg')