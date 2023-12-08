import os
url_dm = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_mensuelle_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
url_da = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_annuelle_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
url_meteo = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/donnees-synop-essentielles-omm/records?select=tc%2Cnom%2Cdate%2Ctemps_present&where=date%20%3E%3D%20date%272022%27%20AND%20nom_dept%3D%27H%C3%A9rault%27&order_by=date&limit=100"
url_j = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_journaliere_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"

path_target= os.path.join(
    os.path.dirname(os.path.realpath(__file__)),"..","data"
)