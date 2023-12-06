import requests
import pandas as pd
import matplotlib.pyplot as plt

# URL du service ArcGIS REST
url = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_annuelle_poll_princ/FeatureServer/0/query?outFields=*&where=1%3D1&f=json"

# Envoyer la requête GET
response = requests.get(url)

# Vérifier si la requête a réussi (statut 200)
if response.status_code == 200:
    # Analyser les données GeoJSON
    data = response.json()

    # À partir de l'examen des données, ajustez la clé nécessaire
    features = data.get("features", [])

    # Créer une liste de dictionnaires à partir des données
    data_list = [feature.get("attributes", {}) for feature in features]

    # Créer un DataFrame pandas
    df = pd.DataFrame(data_list)

    # Ajouter une colonne pour l'année en utilisant la date de début
    df['date_debut'] = pd.to_datetime(df['date_debut'])
    df['annee'] = df['date_debut'].dt.year

    # Agréger les données par année, département et polluant
    aggregated_data = df.groupby(['annee', 'nom_dept', 'nom_poll']).agg({'valeur': 'sum'}).reset_index()

    # Créer un graphique à barres
    fig, ax = plt.subplots(figsize=(12, 8))

    for polluant in aggregated_data['nom_poll'].unique():
        polluant_data = aggregated_data[aggregated_data['nom_poll'] == polluant]
        for annee in polluant_data['annee'].unique():
            annee_data = polluant_data[polluant_data['annee'] == annee]
            label = f"{polluant} - {annee}"
            ax.bar(annee_data['nom_dept'], annee_data['valeur'], label=label)

    ax.set_xlabel('Départements')
    ax.set_ylabel('Quantité totale')
    ax.set_title('Quantité totale de chaque polluant par département et par année')
    ax.legend()
    plt.xticks(rotation=45, ha='right')  # Rotation des étiquettes pour une meilleure lisibilité
    plt.show()

else:
    print("La requête a échoué avec le statut :", response.status_code)
