import os
url_dm = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_mensuelle_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
url_da = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_annuelle_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
url_dacsv = 'https://opendata.arcgis.com/api/v3/datasets/e0f26f918c504608b10d128f65ce0efc_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1'
url_meteo = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/donnees-synop-essentielles-omm/records?select=tc%2Cnom%2Cdate%2Ctemps_present&where=date%20%3E%3D%20date%272022%27%20AND%20nom_dept%3D%27H%C3%A9rault%27&order_by=date&limit=100"
url_dj = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_journaliere_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
url_djcsv = 'https://opendata.arcgis.com/api/v3/datasets/2ab16a5fb61f42c1a689fd9cc466383f_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1'
url_dah = 'https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_72h_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'

url_dmcsv= 'https://opendata.arcgis.com/api/v3/datasets/3acfa2aa5c0346a18ba7749c6885e503_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1'
url_dacsv = 'https://opendata.arcgis.com/api/v3/datasets/e0f26f918c504608b10d128f65ce0efc_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1'
url_djcsv = 'https://opendata.arcgis.com/api/v3/datasets/2ab16a5fb61f42c1a689fd9cc466383f_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1'



path_target= os.path.join(
    os.path.dirname(os.path.realpath(__file__)),"..","data"
)