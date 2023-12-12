import plotly.express as px
from plotly.offline import plot
import numpy as np

def plotpoll(df):
    """
    Cette fonction affiche la concentration d'un polluant en fonction du temps

    Args:
    df (pd.DataFrame): le data frame des données à afficher
    """
    vmin=np.min(df['valeur'])
    vmax=np.max(df['valeur'])
    tmin = np.min(df["date_debut"])
    tmax=  np.max(df["date_debut"])
    fig = px.scatter(
        df,
        x = "date_debut",
        y = "valeur",
        animation_frame = 'date_debut',
        animation_group = 'nom_poll',
        color="nom_poll",
        range_x=[tmin, tmax],#pour bien se placer sur le graphe
        range_y=[vmin-5, vmax+5],
        size='valeur'
    )
    fig.show("notebook")

def plotpollline(df,color,titre):
    """
    Affiche la concentration d'un polluant en fonction du temps sous forme de linechart.
    Le curseur permet de naviguer sur le graphe à travers le temps.
    Args:
    df (pd.DataFrame): le data frame des données à afficher
    color (str): ce que l'on veut distinguer sur le graphe
    titre (str): titre du graphe
    """
    vmin=np.min(df['valeur'])
    vmax=np.max(df['valeur'])
    tmin = np.min(df["date_debut"])
    tmax=  np.max(df["date_debut"])
    fig = px.line(df, x='date_debut', y='valeur', color=color, markers=True, line_group='nom_poll',
                  labels={'valeur': 'Concentration', 'date_debut': 'Année'},
                  title=titre, range_y=[vmin-5,vmax+5],
                  template='plotly'
                  )
    fig.update_layout(xaxis=dict(rangeslider=dict(visible=True)))
    fig.show()

def plotmeteo(df,y,titre):
    """
    Affiche la température ou la vitesse du vent en fonction du temps. 
    Args:
    df (pd.DataFrame): le data frame des données à afficher
    x (str): ordonnées ('Température °C' ou 'Vitesse du vent moyen 10 mn' )
    """
    vmin=np.min(df[y])
    vmax=np.max(df[y])
    fig= px.line(df, x='Date',y=y,markers=True,
                 labels={'Température (°C)': 'Température', 'Date': 'Date'},title=titre,
                 range_y=[vmin-5,vmax+5],template='plotly'
                 )
    fig.update_layout(xaxis=dict(rangeslider=dict(visible=True)))
    fig.show()

def plotville(ville):
    """
    Affiche l'évolution de la moyenne des concentrations des principaux polluants sur 5 ans pour une ville donnée
    Args:
    ville : la ville que l'on étudie (en majuscule)
    """
    import requests
    import pandas as pd
    import plotly.express as px
    from datetime import datetime
    from collections import defaultdict

    # URL de l'API GeoJSON
    url = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_annuelle_poll_princ/FeatureServer/0/query?outFields=*&where=nom_com='"+ville+"'&f=geojson"

    # Récupérer les données GeoJSON depuis l'API
    response = requests.get(url)
    data = response.json()

    # Extraire les données pertinentes pour Toulouse
    features = data['features']
    toulouse_data = [feature['properties'] for feature in features]

    # Préparer les données pour le tracé
    pollutants_per_year = defaultdict(list)

    for entry in toulouse_data:
        pollutant = entry['nom_poll']
        concentration = entry['valeur']
        date_debut_timestamp = entry['date_debut']
        year = datetime.utcfromtimestamp(date_debut_timestamp / 1000).year

        pollutants_per_year[pollutant].append((year, concentration))

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

    # Créer un DataFrame pour Plotly Express
    df = pd.DataFrame([(pollutant, year, concentration) for pollutant, data in pollutants_per_year.items() for year, concentration in data],
                  columns=['Pollutant', 'Year', 'Concentration'])

    # Tracé avec Plotly Express
    fig = px.line(df, x='Year', y='Concentration', color='Pollutant', markers=True, line_group='Pollutant',
              labels={'Concentration': 'Concentration', 'Year': 'Année'},
              title='Concentration des polluants à '+ ville+' par année',
              template='plotly', height=600)

    # Personnaliser le tracé pour ressembler à Matplotlib
    fig.update_traces(
    line=dict(width=1),  # Épaisseur de la ligne
    marker=dict(size=8)   # Taille des marqueurs
    )

    # Ajouter un curseur pour filtrer les données par année
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(
                visible=True
            ),
            type='linear'  # Assurez-vous que le type d'axe x est 'linear' pour que le curseur fonctionne
        )
    )

    # Afficher le tracé interactif
    fig.show()

def plotdep(departement,titre):
    """
    Affiche l'évolution des moyennes des concentrations des polluants d'un département au cours des 5 dernières années.
    Args:
    departement (str): nom du département à afficher (en majuscule)
    """
    import requests
    import pandas as pd
    import plotly.express as px
    from datetime import datetime
    from collections import defaultdict

    # URL de l'API GeoJSON
    url = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_annuelle_poll_princ/FeatureServer/0/query?outFields=*&where=nom_dept='"+departement+"'&f=geojson"

    # Récupérer les données GeoJSON depuis l'API
    response = requests.get(url)
    data = response.json()

    # Extraire les données pertinentes pour l'Hérault
    features = data['features']
    herault_data = [feature['properties'] for feature in features]

    # Préparer les données pour le tracé
    pollutants_per_year = defaultdict(list)

    for entry in herault_data:
        pollutant = entry['nom_poll']
        concentration = entry['valeur']
        date_debut_timestamp = entry['date_debut']
        year = datetime.utcfromtimestamp(date_debut_timestamp / 1000).year

        pollutants_per_year[pollutant].append((year, concentration))

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

    # Créer un DataFrame pour Plotly Express
    df = pd.DataFrame([(pollutant, year, concentration) for pollutant, data in pollutants_per_year.items() for year, concentration in data],
                    columns=['Pollutant', 'Year', 'Concentration'])

    # Tracé avec Plotly Express
    fig = px.line(df, x='Year', y='Concentration', color='Pollutant', markers=True, line_group='Pollutant',
                labels={'Concentration': 'Concentration', 'Year': 'Année'},
                title=titre,
                template='plotly', height=600)

    # Personnaliser le tracé pour ressembler à Matplotlib
    fig.update_traces(
        line=dict(width=1),  # Épaisseur de la ligne
        marker=dict(size=8)   # Taille des marqueurs
    )

    # Ajouter un curseur pour filtrer les données par année
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(
                visible=True
            ),
            type='linear'  # Assurez-vous que le type d'axe x est 'linear' pour que le curseur fonctionne
        )
    )

    # Afficher le tracé interactif
    fig.show()
