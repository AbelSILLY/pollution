import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go 
import matplotlib.pyplot as plt
import pandas as pd
from modpollution import *

#def horaire(df):
#    """
#    Cette fonction affiche la concentration des polluants en fonction des heures de la journée
#
#    Args:
#    df (pd.DataFrame): le data frame des données à afficher
#    """
#    df.rename(columns={"nom_poll":"polluants"}, inplace=True)
#    df["heure"]=df.date_debut
#    df_polar = (
#        df.groupby(["polluants","heure"])["valeur"]
#        .mean()
#        .reset_index()
#    )
#    df_polar = df_polar.astype({"heure":str}, copy = False)
#    fig = px.line_polar(
#        df_polar,
#        r = "valeur",
#        theta="heure",
#        color= "polluants",
#    )
#    return fig





# def horaire(df):
#    """
#    Cette fonction affiche la concentration des polluants en fonction des heures de la journée
#
#    Args:
#    df (pd.DataFrame): le data frame des données à afficher
#    """
#    df.rename(columns={"nom_poll": "polluants"}, inplace=True)
#    df["heure"] = pd.to_datetime(df.date_debut).dt.hour
#    df_polar = (
#        df.groupby(["polluants", "heure"])["valeur"]
#        .mean()
#        .reset_index()
#    )
#
#    # Ajuster les données pour que chaque heure soit représentée par une fraction du cercle
#    df_polar["theta"] = (df_polar["heure"] / 24) * 360
#    df_polar = df_polar.sort_values(by="theta")
#
#    fig = px.line_polar(
#        df_polar,
#        r="valeur",  # Utiliser les valeurs comme axe radial
#        theta="theta",
#        color="polluants",
#        line_close=True,
#        range_r=[df_polar["valeur"].min(), df_polar["valeur"].max()],
#        title="Concentration des polluants en fonction des heures",
#    )
#
#    fig.update_layout(
#        polar=dict(
#            radialaxis=dict(
#                type="linear",
#                tickmode='auto',
#                nticks=5,
#            )
#        )
#    )
#
#    return fig

# Exemple d'utilisation
# Remplacez df_par_votre_dataframe par le nom de votre dataframe
# horaire(df_par_votre_dataframe).show()


import plotly.express as px
import pandas as pd
import numpy as np

def horaire(df):
    """
    Cette fonction affiche la concentration des polluants en fonction des heures de la journée

    Args:
    df (pd.DataFrame): le data frame des données à afficher
    """
    df.rename(columns={"nom_poll": "polluants"}, inplace=True)
    df["heure"] = pd.to_datetime(df.date_debut).dt.hour
    df_polar = (
        df.groupby(["polluants", "heure"])["valeur"]
        .mean()
        .reset_index()
    )

    # Ajuster les données pour que chaque heure soit représentée par une fraction du cercle
    df_polar["theta"] = (df_polar["heure"] / 24) * 360
    df_polar = df_polar.sort_values(by=["polluants", "theta"])

    fig = px.line_polar(
        df_polar,
        r="valeur",  # Utiliser les valeurs comme axe radial
        theta="theta",
        line_close=True,
        color="polluants",  # Utiliser différentes couleurs pour chaque polluant
        range_r=[df_polar["valeur"].min(), df_polar["valeur"].max() * 1.2],  # Ajuster l'échelle pour une meilleure visibilité
        title="Concentration des polluants en fonction des heures",
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                type="linear",
                tickmode='auto',
                nticks=5,
            )
        )
    )

    return fig


def graph_horaire(donnees, station):
    df = extraire_donnees_station(donnees, station)
    fig = horaire(df)
    fig.update_layout(title="Concentration horaire des polluants au cours des derniers mois")
    fig.show()
