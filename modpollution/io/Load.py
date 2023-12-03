import os
import requests
from modpollution.io import url_dm, url_da, path_target

class Load:
    """
    Cette classe télécharge les données de concentration mensuelles et annuelles.

    Paramètres:
    -----------
    url_m : (string) chemin vers les données mensuelles
    url_a : (string) chemin vers les données annuelles
    target_name : (string) chemin où on stock les données
    """
    
    def __init__(self, url_m=url_dm,url_a=url_da,target_name=path_target):
        path = path_target
        fname_m = "data_m.json"
        fname_a = "data_a.json"
        data_m = requests.get(url_m)
        data_a = requests.get(url_a)
        with open(os.path.join(path_target,fname_m),'w') as output_file:
            output_file.write(data_m.text)
        with open(os.path.join(path_target,fname_a),'w') as output_file:
            output_file.write(data_a.text)
    