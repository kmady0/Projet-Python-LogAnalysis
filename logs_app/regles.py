from collections.abc import Callable

from logs_app.analyse import comparer_blacklist, detecter_force_brute, ips_actives, ips_en_erreur
from logs_app.audit import audit


def regle_force_brute(logs: list[dict], seuil: int = 3, **autres) -> set[str]:
    return detecter_force_brute(logs, seuil)


def regle_erreurs(logs: list[dict], **autres) -> set[str]:
    return ips_en_erreur(logs)


def regle_blacklist(logs: list[dict], **autres) -> frozenset[str]:
    return comparer_blacklist(ips_actives(logs))["dangereuses_connectees"]


def apply_security_rules(*args: Callable, **kwargs) -> dict:
    rapport = {}
    for regle in args:
        rapport[regle.__name__] = regle(**kwargs)
    audit(locals(), "apply_security_rules")
    return rapport