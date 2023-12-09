# fichier test
#%%
import modpollution


modpollution.Load()

donnees = modpollution.as_df('./modpollution/data/data_30j.json')
station = 'Agathois-Piscénois - Périurbain'
modpollution.graph_horaire(donnees,station)
# %%
