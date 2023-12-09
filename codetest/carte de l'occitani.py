#!/usr/bin/env python
# coding: utf-8

# # Carte interractive de l'occitanie

# In[3]:


import folium

# Créer une carte centrée sur Montpellier
c = folium.Map(location=[43.61, 3.88], zoom_start=10)

# Ajouter des marqueurs pour Montpellier et Juvignac
folium.Marker([43.61, 3.88], popup='Montpellier').add_to(c)

# Afficher la carte
c


# In[4]:


c.save('Montpellier_map.html')


# In[ ]:




