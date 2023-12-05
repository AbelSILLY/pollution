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

def modif_date(df):
   """
   Modifie le format de date d'un data frame

   Args:
   df (pd.DataFrame): le dataframe à modifier

   returns:
   pd.DataFrame: dataframe avec le bon format de data
   """
   #df['date_debut'] = pd.to_datetime(df['date_debut'], unit='ms').dt.strftime('%Y-%m')
   date = df['date_debut'] / 1000
   nrows = date.shape[0]
   for i in range(nrows):
      date.iloc[i]  = datetime.utcfromtimestamp(date.iloc[i]).strftime('%Y-%m-%d %H:%M:%S')
   df['date_debut'] = date
   return df


def modif_date2(df):
   """
   Modifie le format de date d'un data frame, passe du format timestamp au format AAAA-MM

   Args:
   df (pd.DataFrame): le dataframe à modifier

   returns:
   pd.DataFrame: dataframe avec le bon format de data
   """
   #df['date_debut'] = pd.to_datetime(df['date_debut'], unit='ms').dt.strftime('%Y-%m')
   date = df['date_debut'] / 1000
   nrows = date.shape[0]
   for i in range(nrows):
      date.iloc[i]  = datetime.utcfromtimestamp(date.iloc[i]).strftime('%Y-%m')
   df['date_debut'] = date
   df = df.sort_values(by = 'date_debut')
   return df

def extraire_donnees_station(donnees, station):
    """
    Extrait les données pour une station spécifique, y compris les polluants, les valeurs et les dates.
    Par la même occasion on extrait les données d'une ville (une station étant rattachée à une ville)

    Args:
        donnees (pd.DataFrame): Le jeu de données contenant les données de pollution.
        station (str): Le nom de la station.

    Returns:
        pd.DataFrame: Données extraites avec les colonnes : 'Date', 'Polluant', 'Concentration (µg/m³)', 'Station'.
    """
    df = donnees.loc[(donnees["nom_station"] == station), ["nom_poll", "valeur", "date_debut", "nom_station"]]
    #df = df.rename(columns={'date_debut': 'Date','nom_station': 'Station'})
    return df

def extraire_polluant(donnees,polluant):
   """
   Extrait les données relatives à un polluant particulier.

   Args:
   donnees (pd.DataFrame): le dataframe contenant les données
   polluant (str) : le polluant que l'on souhaite extraire

   Returns:
   pd.DataFrame: Données extraites avec les colonnes : 'Date', 'Polluant', 'Concentration (µg/m³)', 'Station'
   """
   df = donnees.loc[(donnees["nom_poll"] == polluant), ["nom_poll", "valeur", "date_debut", "nom_station"]]
   #df = df.rename(columns={'date_debut': 'Date', 'nom_poll': 'Polluant', 'Concentration': 'valeur', 'Station': 'nom_station'})
   return df