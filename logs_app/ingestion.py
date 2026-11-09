import json
from collections.abc import Iterator
from datetime import datetime


def lire_fichier(chemin: str) -> Iterator[str]:
    with open(chemin, encoding="utf-8") as f:
        for ligne in f:
            yield ligne.strip()


def lire_plusieurs_fichiers(chemins: list[str]) -> Iterator[str]:
    for chemin in chemins:
        yield from lire_fichier(chemin)


def lire_message(message: str) -> dict | str:
    try:
        return json.loads(message)
    except json.JSONDecodeError:
        return message


def parser_ligne(ligne: str) -> dict | None:
    morceaux = ligne.split(" | ")
    if len(morceaux) != 5:
        return None
    try:
        date = datetime.strptime(morceaux[0], "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None
    return {
        "date": date,
        "niveau": morceaux[1],
        "ip": morceaux[2],
        "utilisateur": morceaux[3],
        "message": lire_message(morceaux[4]),
        "source": (morceaux[2], morceaux[3]),
    }