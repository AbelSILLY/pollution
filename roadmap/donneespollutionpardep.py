# %%
import requests
import json
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Fonction pour récupérer les données depuis l'URL
def get_data(url):
    response = requests.get(url)
    data = response.json()
    return data

# Fonction pour extraire les données nécessaires
def extract_data(features):
    department_pollution_counts = defaultdict(lambda: defaultdict(int))

    for feature in features:
        properties = feature.get('properties', {})
        
        # Extraction des données
        code_zone = properties.get('code_zone')
        code_pol = properties.get('code_pol')
        etat = properties.get('etat')

        # Comptage des occurrences de chaque type de polluant par département et par état
        department_pollution_counts[code_zone][(code_pol, etat)] += 1

    return department_pollution_counts

# Fonction pour afficher les données dans un graphique radar
def plot_radar_chart(department_pollution_counts):
    departments = list(department_pollution_counts.keys())
    pollutants_states = list(set((p, s) for counts in department_pollution_counts.values() for p, s in counts.keys()))

    # Trouver le nombre maximal de types de polluants parmi tous les départements
    max_pollutants = max(len(department_pollution_counts[dept]) for dept in departments)

    # Remplir les départements avec moins de types de polluants pour avoir le même nombre que le maximum
    for dept in departments:
        while len(department_pollution_counts[dept]) < max_pollutants:
            department_pollution_counts[dept][f"dummy_pollutant_{len(department_pollution_counts[dept])}"] = 0

    num_pollutants_states = len(pollutants_states)
    angles = np.linspace(0, 2 * np.pi, num_pollutants_states, endpoint=False)

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.set_xticks(angles)
    ax.set_xticklabels([f"{p}, {s}" for p, s in pollutants_states])

    for department in departments:
        counts = [department_pollution_counts[department].get((pollutant, state), 0) for pollutant, state in pollutants_states]
        ax.scatter(angles, counts, label=f'Département {department}')

    # Ajout des légendes
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    ax.set_title('Occurrences de polluants par département et par état')

    # Affichage du graphique
    plt.show()

if __name__ == "__main__":
    # URL des données
    url = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/epipol_occitanie/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"

    # Récupérer les données depuis l'URL
    data = get_data(url)

    # Extraire les données nécessaires
    department_pollution_counts = extract_data(data.get('features', []))

    # Filtrer les départements avec moins de 3 types de polluants pour éviter les erreurs
    department_pollution_counts = {dept: counts for dept, counts in department_pollution_counts.items() if len(counts) >= 3}

    # Afficher les données dans un graphique radar avec des points
    plot_radar_chart(department_pollution_counts)

