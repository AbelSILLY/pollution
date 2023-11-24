# %%
import requests
import pandas as pd
import os
import pygal
import matplotlib.pyplot as plt
##### Import des données #####
url="https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_mensuelle_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
response = requests.get(url)
data = response.json()
#### 1er traitement des données ####
data1=[]#liste vide
features=data['features']#on extrait la partie données
for feature in features:
     data1.append(feature['attributes'])
data1
df_raw=pd.DataFrame(data1)
df_raw
df_raw.info()
df=df_raw.dropna()
df.info()#on a perdu à peu près 200 "individus"
df.set_index('date_debut')
# %%
##### Affichage #####
fig, ax = plt.subplots(1, 1, figsize=(10,10))
df.groupby(['nom_dept','nom_poll'])['valeur'].aggregate(lambda x:
                                             x.mean()).plot(ax=ax,kind='bar')
plt.xlabel('Nom Départements et polluants')
plt.ylabel('Observation Concentrations')
plt.title('Moyenne des concentrations observées par départements')
plt.savefig("./vis/con_pol_dep.svg",format='svg')
# On remarque une concentration en O3 plus importante que pour les autres polluants
#### Extraction département polluant ####
df2=pd.DataFrame(df.groupby(['nom_dept','nom_poll'])[['valeur']].mean())
df2=df2.transpose()
#%%
#### Carte ####
fr_chart = pygal.maps.fr.Departments(human_readable=True)
fr_chart.title='Moyenne des concentrations en O3 par départements'
fr_chart.add('In 2022', {
     '09':df2['ARIEGE']['O3'][0], '12':df2['AVEYRON']['O3'][0],
     '30':df2['GARD']['O3'][0], '32':df2['GERS']['O3'][0],
     '31':df2['HAUTE-GARONNE']['O3'][0], '65':df2['HAUTES-PYRENEES']['O3'][0],
     '34':df2['HERAULT']['O3'][0], '66':df2['PYRENEES-ORIENTALES']['O3'][0],
     '81':df2['TARN']['O3'][0], '82':df2['TARN-ET-GARONNE']['O3'][0]
})
#fr_chart.render()
fr_chart.render_in_browser() #pour visualiser dans une fenêtre sur un navigateur web
#fr_chart.render_to_file('./vis/chart_con_dep.svg')#sauvegarde le fichier
## Le Gard, le Tarn et les Pyrénées-Orientales ont une concentration particulièrement élevées