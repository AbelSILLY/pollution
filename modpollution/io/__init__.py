import os
url_meteo_mtp = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/donnees-synop-essentielles-omm/exports/csv?lang=fr&refine=nom_reg%3A%22Occitanie%22&refine=nom%3A%22MONTPELLIER%22&qv1=(date%3A%5B2022-09-30T22%3A00%3A00Z%20TO%202023-11-01T22%3A59%3A59Z%5D)&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B"
url_meteo_toul = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/donnees-synop-essentielles-omm/exports/csv?lang=fr&refine=nom_reg%3A%22Occitanie%22&refine=nom%3A%22TOULOUSE-BLAGNAC%22&qv1=(date%3A%5B2022-09-30T22%3A00%3A00Z%20TO%202023-11-01T22%3A59%3A59Z%5D)&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B"

url_mcsv= 'https://opendata.arcgis.com/api/v3/datasets/3acfa2aa5c0346a18ba7749c6885e503_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1'
url_acsv = 'https://opendata.arcgis.com/api/v3/datasets/e0f26f918c504608b10d128f65ce0efc_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1'
url_jcsv = 'https://opendata.arcgis.com/api/v3/datasets/2ab16a5fb61f42c1a689fd9cc466383f_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1'
url_30jcsv = 'https://opendata.arcgis.com/api/v3/datasets/cf38a358d3794f119a20f250973c0e34_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1'


path_target= os.path.join(
    os.path.dirname(os.path.realpath(__file__)),"..","data"
)