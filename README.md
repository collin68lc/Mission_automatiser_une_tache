Pour executer le programme il faut d'abord créer l'environement virtuel en tapant les lignes suivantes dans le terminal (vérifiez que vous êtes dans le dossier où se trouve le programme):
python -m venv env ou python3 -m venv env 

Une fois l'environnement créé il faut taper la ligne de commande suivante pour l'activer:
source env/bin/activate si vous travaillez avec Linux ou Mac
env\Scripts\activate.bat si vous êtes sous Windows

Si l'environnement est bine activé vous verrez apparaitre (env) au début ou à la fin de la ligne de commande.

Une fois l'environnement installer il faudra installer les différents package se trouvant dans le fichier requirements.txt à l'aide de la fonction pip install ou pip install -r requirements.txt qui installera automatiquement tous les package présent dans le fichier requirements.txt

Lorsque les package sont installé vous pouvez lancer le programme