import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go 
import matplotlib.pyplot as plt
import pandas as pd
from modpollution import *

def horaire(df):
    """
    Cette fonction affiche la concentration des polluants en fonction des heures de la journée

    Args:
    df (pd.DataFrame): le data frame des données à afficher
    """
    df.rename(columns={"nom_poll":"polluants"}, inplace=True)
    df["heure"]=df.index.hour
    df_polar = (
        df.groupby(["polluants","heure"])["valeur"]
        .mean()
        .reset_index()
    )
    df_polar = df_polar.astype({"heure":str}, copy = False)
    fig = px.line_polar(
        df_polar,
        r = "valeur",
        theta="heure",
        color= "polluants",
    )
    return fig

def graph_horaire(donnees, station):
    fig = horaire(donnees, station)
    fig.update_layout(title="Concentration horaire des polluants au cours des derniers mois")
    fig.show()