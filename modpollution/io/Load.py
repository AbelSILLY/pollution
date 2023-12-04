import os
import requests
from modpollution.io import url_dm, url_da, url_j, url_meteo, path_target

class Load:
    """
    Cette classe télécharge les données de concentration mensuelles et annuelles.

    Paramètres:
    -----------
    url_m : (string) chemin vers les données mensuelles
    url_a : (string) chemin vers les données annuelles
    url_j : (string) chemin vers les données journalières
    target_name : (string) chemin où on stock les données
    """
    
    def __init__(self, url_m=url_dm,url_a=url_da,url_meteo=url_meteo,target_name=path_target):
        path = path_target
        fname_m = "data_m.json"
        fname_a = "data_a.json"
        fname_j = "data_j.json"
        fname_meteo = "data_meteo.json"
        data_m = requests.get(url_m)
        data_a = requests.get(url_a)
        data_j = requests.get(url_j)
        meteo = requests.get(url_meteo)
        with open(os.path.join(path_target,fname_m),'w') as output_file:
            output_file.write(data_m.text)
        with open(os.path.join(path_target,fname_a),'w') as output_file:
            output_file.write(data_a.text)
        with open(os.path.join(path_target,fname_meteo),'w') as output_file:
            output_file.write(meteo.text)
        with open(os.path.join(path_target,fname_j),'w') as output_file:
            output_file.write(data_j.text)
    