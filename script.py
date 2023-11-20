import requests
import pandas as pd
import os
import pygal
import matplotlib.pyplot as plt
url="https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_mensuelle_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
response = requests.get(url)
data = response.json()
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
#### 1ère figure ####
fig, ax = plt.subplots(1, 1, figsize=(5, 5))
df.groupby(['nom_poll'])['valeur'].aggregate(lambda x:
                                             x.mean()).plot(ax=ax,kind='bar')
plt.xlabel('Nom Polluants')
plt.ylabel('Observation Concentrations')
plt.title('Moyenne des concentrations observées par polluants')
plt.savefig("./vis/con_pol.svg",format='svg')
#### 2ème figure ####
fig2, ax2 = plt.subplots(1, 1, figsize=(5,5))
df.groupby(['nom_dept'])['valeur'].aggregate(lambda x:
                                             x.mean()).plot(ax=ax2,kind='bar')
plt.xlabel('Nom Départements')
plt.ylabel('Observation Concentrations')
plt.title('Moyenne des concentrations observées par départements')
plt.savefig("./vis/con_dep.svg",format='svg')
#### 3ème figure ####
fig3, ax3 = plt.subplots(1, 1, figsize=(10,10))
df.groupby(['nom_dept','nom_poll'])['valeur'].aggregate(lambda x:
                                             x.mean()).plot(ax=ax3,kind='bar')
plt.xlabel('Nom Départements et polluants')
plt.ylabel('Observation Concentrations')
plt.title('Moyenne des concentrations observées par départements')
plt.savefig("./vis/con_pol_dep.svg",format='svg')

#### Carte ####
fr_chart = pygal.maps.fr.Departments(human_readable=True)
fr_chart.title='Moyenne des concentrations par départements'
fr_chart.add('In 2022', {
     '09':24.044737, '12':30.248485, '30':27.981081, '32':16.600000,
     '31':25.598969, '65':16.850467, '34':30.191860, '66':25.998305,
     '81':17.986047, '82':25.969388
})
#fr_chart.render()
fr_chart.render_in_browser() #pour visualiser dans une fenêtre sur un navigateur web
fr_chart.render_to_file('./vis/chart_con_dep.svg')#sauvegarde le fichier