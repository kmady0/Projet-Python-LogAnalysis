import json


def lire_fichier(chemin):
    with open(chemin, encoding="utf-8") as f:
        for ligne in f:
            yield ligne.strip()


def lire_plusieurs_fichiers(chemins):
    for chemin in chemins:
        yield from lire_fichier(chemin)


def lire_message(message):
    try:
        return json.loads(message)
    except json.JSONDecodeError:
        return message


def parser_ligne(ligne):
    morceaux = ligne.split(" | ")
    if len(morceaux) != 5:
        return None
    return {
        "date": morceaux[0],
        "niveau": morceaux[1],
        "ip": morceaux[2],
        "utilisateur": morceaux[3],
        "message": lire_message(morceaux[4]),
        "source": (morceaux[2], morceaux[3]),
    }