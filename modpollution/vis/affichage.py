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
        range_x=[tmin, tmax],
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
                  labels={'valeur': 'Concentration', 'date_debt': 'Année'},
                  title=titre, range_y=[vmin-5,vmax+5],
                  template='plotly', height=600)
    fig.update_layout(xaxis=dict(rangeslider=dict(visible=True)))
    fig.show()