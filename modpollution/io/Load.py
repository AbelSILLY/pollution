import os
import requests
from modpollution.io import url_meteo_mtp, path_target, url_dmcsv, url_dacsv,url_djcsv, url_d30jcsv

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
    
    def __init__(self,url_30j_csv = url_d30jcsv,url_jcsv=url_djcsv,url_mcsv=url_dmcsv,url_acsv=url_dacsv,url_meteo=url_meteo_mtp,target_name=path_target):
        path = path_target
        fname_mcsv = 'data_m.csv'
        fname_acsv='data_a.csv'
        fname_jcsv='data_j.csv'
        fname_30j = 'data_30j.csv'
        fname_meteo_mtp = "data_meteo_mtp.csv"

        
        data_mcsv = requests.get(url_mcsv)
        data_acsv = requests.get(url_acsv)
        data_jcsv = requests.get(url_jcsv)
        data_30j = requests.get(url_30j_csv)
        
        meteo_mtp = requests.get(url_meteo)
        
        with open(os.path.join(path_target,fname_mcsv),'wb') as output_file:
            output_file.write(data_mcsv.content)
        with open(os.path.join(path_target,fname_acsv),'wb') as output_file:
            output_file.write(data_acsv.content)
        with open(os.path.join(path_target,fname_jcsv),'wb') as output_file:
            output_file.write(data_jcsv.content)
        with open(os.path.join(path_target,fname_30j),'wb') as output_file:
            output_file.write(data_30j.content)
        
        with open(os.path.join(path_target,fname_meteo_mtp),'wb') as output_file:
            output_file.write(meteo_mtp.content)
        #with open(os.path.join(path_target,fname_30j),'w') as output_file:
        #    output_file.write(data_30j.text)
