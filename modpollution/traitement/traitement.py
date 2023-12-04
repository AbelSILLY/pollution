import pandas as pd
import json
from datetime import datetime
def as_df(data_path_target):
    """
    Cette fonction retourne un (pandas) data frame prêt pour l'affichage
    Args :
    data_path_target (str or path like object): le chemin vers les données
    fname (str) : nom du fichier
    """
    with open(data_path_target) as f:
     data = json.load(f)
    
    features = data['features']
    data_list = []

    for feature in features:
        data_list.append(feature['attributes'])

    df_raw = pd.DataFrame(data_list)
    df = df_raw.dropna()
    return df


def extraire_donnees_pollution(donnees, station):
    """
    Extrait les données pour une station spécifique, y compris les polluants, les valeurs et les dates.

    Args:
        donnees (pd.DataFrame): Le jeu de données contenant les données de pollution.
        station (str): Le nom de la station.

    Returns:
        pd.DataFrame: Données extraites avec les colonnes : 'Date', 'Polluant', 'Concentration (µg/m³)'.
    """
    
    df = donnees.loc[(donnees["nom_station"] == station), ["nom_poll", "valeur", "date_debut", "nom_station"]]
    date  = df["date_debut"] / 1000
    nrows = date.shape[0]
    for i in range(nrows):
       date.iloc[i] = datetime.utcfromtimestamp(date.iloc[i]).strftime('%Y-%m-%d %H:%M:%S')
    
    date = pd.DataFrame(date)
    df["date_debut"] = date
    df = df.rename(columns={'date_debut': 'Date', 'nom_poll': 'Polluant', 'Concentration': 'valeur', 'Station': 'nom_station'})
    return df