# IO (Input-Output)
IO est la section contenant la classe Load chargée de télécharger les données de pollution et météo. Cette classe est donc indispensable si l'on souhaite utiliser modpollution sans cloner ce dépot.
A l'aide du package 'requests' les données sont récupérées via url et stockées dans des fichiers dans la section data.
Parmi les données de pollution on retrouve:

- Des données de concentration de polluants annuelles sur les 5 dernières années.
- Des données de concentration de polluants mensuelles sur l'année dernière.
- Des données de concentration de polluants journalières sur l'année dernière.
- Des données de concentration de polluants horaires sur le mois dernier.

Une première approche a été d'importer les données depuis l'API ATMO sous format JSON, mais ces données se sont révélées très incomplètes, ce qui nous a poussé à nous tourner vers les données sous format csv.

Parmi les données météo on retrouve:

- Les données météo sur Montpellier sur l'année 2022.
- Les données météo sur Toulouse sur l'année 2022.
- Les données météo sur le département Hautees-Pyrénées sur l'année 2022.

Nous aurions aimé utiliser plus de données météo sur certaines villes mais le site à disposition ne le permettait pas.
