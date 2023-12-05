import plotly.express as px
from plotly.offline import plot
import numpy as np

def plotpoll(df):
    """
    Cette fonction affiche la concentration d'un polluant en fonction du temps

    Args:
    df (pd.DataFrame): le data frame des données à afficher
    """
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
        range_y=[0, 90],
        size='valeur'
    )
    fig.show("notebook")

#def plotpollbis(df):