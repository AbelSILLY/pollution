import os
import requests
from modpollution.io import url_dm, url_da, url_dj, url_meteo, path_target, url_dah, url_dmcsv, url_dacsv,url_djcsv

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
    
    def __init__(self,url_jcsv=url_djcsv,url_j=url_dj,url_mcsv=url_dmcsv, url_m=url_dm,url_a=url_da,url_acsv=url_dacsv,url_meteo=url_meteo,target_name=path_target,url_ah=url_dah):
        path = path_target
        fname_m = "data_m.json"
        fname_mcsv = 'data_m.csv'
        fname_a = "data_a.json"
        fname_acsv='data_a.csv'
        fname_j = "data_j.json"
        fname_jcsv='data_j.csv'
        fname_ah = 'data_ah.json'
        fname_meteo = "data_meteo.json"
        data_m = requests.get(url_m)
        data_mcsv = requests.get(url_mcsv)
        data_a = requests.get(url_a)
        data_acsv = requests.get(url_acsv)
        data_j = requests.get(url_j)
        data_jcsv=requests.get(url_jcsv)
        meteo = requests.get(url_meteo)
        data_ah = requests.get(url_ah)
        with open(os.path.join(path_target,fname_m),'w') as output_file:
            output_file.write(data_m.text)
        with open(os.path.join(path_target,fname_mcsv),'w') as output_file:
            output_file.write(data_mcsv.text)
        with open(os.path.join(path_target,fname_a),'w') as output_file:
            output_file.write(data_a.text)
        with open(os.path.join(path_target,fname_acsv),'w') as output_file:
            output_file.write(data_acsv.text)
        with open(os.path.join(path_target,fname_meteo),'w') as output_file:
            output_file.write(meteo.text)
        with open(os.path.join(path_target,fname_j),'w') as output_file:
            output_file.write(data_j.text)
        with open(os.path.join(path_target,fname_jcsv),'w') as output_file:
            output_file.write(data_jcsv.text)
        with open(os.path.join(path_target,fname_ah),'w') as output_file:
            output_file.write(data_ah.text)
    