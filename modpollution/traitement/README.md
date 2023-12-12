# Traitement:
Traitement est la section contenant toutes les fonctions chargées de passer des données brutes à des dataframe que l'on peut visualiser.
On distingue deux types de fonctions de traitements suivant si l'on traite des données météo ou de pollutions.
Parmis les fonctions de traitement on retrouve:

- Des fonction 'as_df*' (les plus importantes) pour obtenir les dataframes de bases.
- Des fonctions d'extraction pour obtenir les données d'un polluant,d'une ville ou autre.
- Des fonctions de moyennes que l'on utilisera suivant ce que l'on veut afficher.

A noter que certaines de ces fonctions étaient prévues pour travailler avec des fichier JSON, que nous avons abandonné par la suite. Nous n'avons toutefois pas supprimé les fonctions car nous nous réservons la possibilité de réutiliser ce type de fichiers.

## Axes d'améliorations

Au vu du nombre de fonction et de l'importance de cette section on pourrait implémenter une classe relative aux dataframe de données pollutions ou météo. La classe s'initialiserait avec les fonction 'as_df' et on les fonctions définies dans le suites seraient relatives à ces classes.