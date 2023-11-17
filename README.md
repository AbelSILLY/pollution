
#Projet de Groupe HAX712X

## Lien du site

[https://jeannevivierum.github.io/pollution/](https://jeannevivierum.github.io/pollution/)

## Packages utilisés

### NumPy

NumPy est une bibliothèque qui permet de manipuler des matrices ou tableaux multidimensionnels ainsi que des fonctions mathématiques opérant sur ces tableaux. Elle permet de notamment de créer directement un tableau depuis un fichier ou, au contraire, de sauvegarder un tableau dans un fichier. C'est l'une des bibliothèques les plus connues sur python et elle est particulièrement utilisée en DataSciences.

### Pandas

La bibliothèque Pandas fournit des outils pour lire et écrire des données depuis et vers différents formats, en particulier des fichiers CSV (qui nous intéressent particulièrement). Elle permet aussi un alignement intelligent des données et gestion des données manquantes, un alignement des données basé sur des chaînes de caractères, et de trier les données selon divers critères.

### Matplotlib

La bibliothèque Matplotlib est destinée à tracer et visualiser des données sous forme de graphiques. Elle permet de nombreux exports au format matriciel (PNG, JPEG...) et vectoriel (PDF, SVG...). Elle est notamment utilisée sur des serveurs d’application web.

### Pytest

Nous utiliserons la librairie Pytest afin d'effectuer des tests automatisés pour s'assurer que notre code fonctionne.

### OS

Nous utiliserons la librairie OS afin d'éviter les conflits entre nos systèmes d'exploitation vis à vis de l'utilisation de fichiers communs comme les jeux de données par exemple.

### Pooch

Pooch permet de gérer un répertoire de données en téléchargeant les fichiers de données depuis un serveur et en les enregistrant localement. Les principales qualités de pooch sont qu'on peut télécharger une donnée seulement si nécessaire, qu'elle vérifie l'intégrité des données télechargées et est souvent utilisée pour vérifier qu'un fichier doit être mis à jour. Cette bibliothèque contient un moyen de dézipper et décompresser les données pendant le téléchargement, ce qui nous fera gagner du temps.

## Descrpition des données utilisées

### ATMO

### WeatherForcast

### RTE

Sur l'application éCO2mix gérée par RTE (responsable du transport de l'électricité), nous avons remarqué que les données concernant la production d'électricité en France étaient découpées par région. Nous savons que la production d'électricité est à l'origine d'émissions de CO2 et donc de pollution atmosphérique. Bien que les principaux moyens de production en Occitanie soient neutres en carbonne (nucléaire, barrages, solaire et éolien) il arrive qu'il soit nécessaire de consommer des énergies fossiles. Nous aimerions donc extraire les données concernant la production électrique en Occitanie, afin de les mettre en relation avec la pollution de l'air dans cette même région.
