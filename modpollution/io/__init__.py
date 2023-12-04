import os
url_dm = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_mensuelle_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
url_da=  "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_annuelle_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
path_target= os.path.join(
    os.path.dirname(os.path.realpath(__file__)),"..","data"
)