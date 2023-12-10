import os
import requests
from modpollution.io import url_meteo_hp,url_meteo_mtp,url_meteo_toul, path_target, url_mcsv, url_acsv,url_jcsv, url_30jcsv

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
    
    def __init__(self,url_30j_csv = url_30jcsv ,url_jcsv=url_jcsv,
                 url_mcsv=url_mcsv,url_acsv=url_acsv,
                 url_meteo_toul=url_meteo_toul,url_meteo_mtp=url_meteo_mtp,
                 url_meteo_hp=url_meteo_hp,path_target=path_target):
        fname_mcsv = 'data_m.csv'
        fname_acsv='data_a.csv'
        fname_jcsv='data_j.csv'
        fname_30j = 'data_30j.csv'
        fname_meteo_mtp = "data_meteo_mtp.csv"
        fname_meteo_toul = "data_meteo_toul.csv"
        fname_meteo_hp = "data_meteo_hp.csv"

        #### données pollution ####
        data_mcsv = requests.get(url_mcsv)
        data_acsv = requests.get(url_acsv)
        data_jcsv = requests.get(url_jcsv)
        data_30j = requests.get(url_30j_csv)
        
        #### données météo ####
        meteo_mtp = requests.get(url_meteo_mtp)
        meteo_toul = requests.get(url_meteo_toul)
        meteo_hp = requests.get(url_meteo_hp)
        ##### import csv pollution #####
        with open(os.path.join(path_target,fname_mcsv),'wb') as output_file:
            output_file.write(data_mcsv.content)
        with open(os.path.join(path_target,fname_acsv),'wb') as output_file:
            output_file.write(data_acsv.content)
        with open(os.path.join(path_target,fname_jcsv),'wb') as output_file:
            output_file.write(data_jcsv.content)
        with open(os.path.join(path_target,fname_30j),'wb') as output_file:
            output_file.write(data_30j.content)
        
        #### imoprt csv météo #####
        with open(os.path.join(path_target,fname_meteo_mtp),'wb') as output_file:
            output_file.write(meteo_mtp.content)
        with open(os.path.join(path_target,fname_meteo_toul),'wb') as output_file:
            output_file.write(meteo_toul.content)
        with open(os.path.join(path_target,fname_meteo_hp),'wb') as output_file:
            output_file.write(meteo_hp.content)
        