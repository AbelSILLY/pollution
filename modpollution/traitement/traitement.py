import pandas as pd
import json

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
