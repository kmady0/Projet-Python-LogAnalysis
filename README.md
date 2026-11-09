# Projet Python ING3 : analyse de logs

Plateforme en ligne de commande qui lit, filtre, transforme et analyse des fichiers de logs, sans les charger entièrement en mémoire. Elle détecte notamment les attaques par force brute et les IP présentes dans une liste noire.

## Structure

    data/                  fichiers de logs de test
    logs_app/
        ingestion.py       Module 1 : lecture (yield, yield from) et parsing
        transformation.py  Module 2 : filter, map, lambda, match-case
        analyse.py         Module 3 : set, frozenset, defaultdict, force brute
        regles.py          Module 4 : moteur de règles (*args, **kwargs)
        audit.py           Module 4 : audit avec globals() et locals()
    main.py                point d'entrée du pipeline
    rapportprojet.ipynb    rapport de démonstration

## Installation

    git clone https://github.com/kmady0/Projet-Python-LogAnalysis.git
    cd Projet-Python-LogAnalysis
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt

## Utilisation

Lancer le pipeline complet :

    python main.py

Ouvrir le rapport :

    jupyter notebook rapportprojet.ipynb