from collections.abc import Iterable, Iterator

from logs_app.ingestion import parser_ligne


def normaliser(log: dict) -> dict:
    log["niveau"] = log["niveau"].strip().upper()
    log["utilisateur"] = log["utilisateur"].strip().lower()
    log["resume"] = f"[{log['niveau']}] {log['utilisateur']} depuis {log['ip']}"
    return log


def pipeline(lignes: Iterable[str]) -> Iterator[dict]:
    logs = map(parser_ligne, lignes)
    logs = filter(None, logs)
    logs = map(normaliser, logs)
    logs = filter(lambda log: log["niveau"] in ("INFO", "WARNING", "ERROR", "CRITICAL"), logs)
    return logs


def router(element: object) -> str:
    match element:
        case str():
            return f"Texte brut : {element}"
        case {"code": code}:
            return f"Erreur applicative, code {code}"
        case (ip, utilisateur):
            return f"Connexion de {utilisateur} depuis {ip}"
        case _:
            return "Format inconnu"