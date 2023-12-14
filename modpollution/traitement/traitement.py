import pandas as pd
import json
from datetime import datetime
import modpollution

def as_df(data_path_target):
    """
    Cette fonction retourne un (pandas) data frame prêt pour l'affichage
    Args :
    data_path_target (str or path like object): le chemin vers les données
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

def as_df_csv(data_path_target,annee):
   """
   Cette fonction retourne un (pandas) data frame prêt pour l'affichage
   Args :
   annee (bool): True si df désigne un dataframe relatif à des données annuelles, False sinon
   data_path_target (str or path like object): le chemin vers les données
   """
   df = pd.read_csv(data_path_target,encoding='UTF-8-SIG')
   df = df.dropna()
   df = modpollution.modif_date_csv(df,annee)
   return df


def as_df_meteo(data_path_target):
   """
   Renvoie une data frame à partir des données météo
   Args:
   data_path_target (str or path like object): le chemin vers les données
   """
   df = pd.read_csv(data_path_target,delimiter=';')
   df = modpollution.modif_date_meteo(df)
   df = df[['Date','Température (°C)','Vitesse du vent moyen 10 mn','Nebulosité totale','Nom','department (name)']]
   df = df.dropna()
   return df

def modif_date(df):
   """
   Modifie le format de date d'un data frame

   Args:
   df (pd.DataFrame): le dataframe à modifier

   returns:
   pd.DataFrame: dataframe avec le bon format de date
   """
   df['date_debut'] = pd.to_datetime(df['date_debut'], unit='ms').dt.strftime('%Y-%m')
   return df


def modif_date_meteo(df):
   """
   Modifie le format de date des fichiers météo
   Args:
   df (pd.DataFrame): le dataframe à modifier
   returns:
   pd.DataFrame: le dataframe avec le bon format de date
   """
   df['Date'] = pd.to_datetime(df['Date'],utc = True)
   df['Date'] = df['Date'].dt.strftime('%Y-%m-%d %H:%M:%S')
   df = df.sort_values(by = 'Date')
   return df

def modif_date_csv(df,annee):
   """
   Modifie le format de date des fichiers météo avec un format différent selon le type de dataframe
   Args:
   df (pd.DataFrame): le dataframe à modifier
   annee (bool): True si df désigne un dataframe relatif à des données annuelles, False sinon
   returns:
   pd.DataFrame: le dataframe avec le bon format de date
   """
   df['date_debut'] = pd.to_datetime(df['date_debut'],utc = True)
   if annee == True:
      df['date_debut'] = df['date_debut'].dt.strftime('%Y-%m-%d')
   else:
      df['date_debut'] = df['date_debut'].dt.strftime('%Y-%m-%d %H:%M:%S')
   df = df.sort_values(by = 'date_debut')
   return df

def modif_date2(df):
   """
   Modifie le format de date d'un data frame, passe du format timestamp au format AAAA-MM

   Args:
   df (pd.DataFrame): le dataframe à modifier

   returns:
   pd.DataFrame: dataframe avec le bon format de date
   """
   df['date_debut'] = pd.to_datetime(df['date_debut'], unit='ms').dt.strftime('%Y-%m')


def extraire_donnees_station(donnees, station):
    """
    Extrait les données pour une station spécifique.
    Par la même occasion on extrait les données d'une ville (une station étant rattachée à une ville)

    Args:
        donnees (pd.DataFrame): Le jeu de données contenant les données de pollution.
        station (str): Le nom de la station.

    Returns:
        pd.DataFrame: Données extraites avec les colonnes : 'Date', 'Polluant', 'Concentration (µg/m³)', 'Station'.
    """
    df = donnees.loc[(donnees["nom_station"] == station), ["nom_poll", "valeur", "date_debut", "nom_station"]]
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
   df = donnees.loc[(donnees["nom_poll"] == polluant), ["nom_com","nom_dept","nom_poll", "valeur", "date_debut", "nom_station"]]
   return df

def extraire_donnees_villes(donnees, ville):
    """
   Extrait les données relatives à une ville particulière.

   Args:
   donnees (pd.DataFrame): le dataframe contenant les données
   ville (str) : la ville que l'on souhaite extraire

   Returns:
   pd.DataFrame: Données extraites avec les colonnes :'Département' 'Date', 'Polluant', 'Concentration (µg/m³)', 'Ville'
   """
    df = donnees.loc[(donnees["nom_com"] == ville), ["nom_dept","nom_com",'nom_poll','valeur','date_debut','nom_station']]
    return df

def extraire_donnees_depart(donnees, departement):
    """
   Extrait les données relatives à un département particulier.

   Args:
   donnees (pd.DataFrame): le dataframe contenant les données
   departement (str) : le département que l'on souhaite extraire

   Returns:
   pd.DataFrame: Données extraites avec les colonnes : 'Date', 'Polluant', 'Concentration (µg/m³)', 'Ville'
   """
    df = donnees.loc[(donnees["nom_dept"] == departement), ["nom_dept","nom_com",'nom_poll','valeur','date_debut','nom_station']]
    return df


def mean_df(df):
    """
    Renvoie un dataframe avec les moyennes des concentrations des polluants.
    Args:
    df (pd.DataFrame) : le dataframe contenant les données
    
    Returns:
    pd.DataFrame
    """
    df = pd.DataFrame(df.groupby(['date_debut','nom_poll'])['valeur'].mean())
    df = df.reset_index() #"annule" le groupby
    return df

def mean_by_dep(df):
    """
    Renvoie un dataframe avec les moyennes des concentrations des polluants par station.
    Args:
    df (pd.DataFrame) : le dataframe contenant les données
    
    Returns:
    pd.DataFrame
    """
    df = pd.DataFrame(df.groupby(['date_debut','nom_poll','nom_station'])['valeur'].mean())
    df = df.reset_index() #"annule" le groupby
    return df

