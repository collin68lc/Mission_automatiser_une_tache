# Récupération des données du site books.toscrape.com

## Déscription
Un script Python qui parcourt l'intégralité du site books.toscrape.com, extrait les informations de chaque livre par catégorie, les enregistre dans des fichiers CSV et télécharge les images de couverture correspondantes.

## Prérequis
    • Python 3.8 ou supérieur 
    • Les bibliothèques suivantes : 
        ◦ requests 
        ◦ beautifulsoup4 
## Installation
    1. Cloner ou télécharger le projet. 
    2. Installer les dépendances : 
bash
pip install requests beautifulsoup4
## Utilisation
Lancer simplement le script depuis un terminal :
bash
python nom_du_script.py
Le script va :
    1. Récupérer la liste des catégories du site. 
    2. Parcourir chaque catégorie et collecter les URLs de tous les livres. 
    3. Extraire les informations de chaque livre. 
    4. Générer un fichier CSV par catégorie. 
    5. Télécharger les images de couverture correspondantes. 