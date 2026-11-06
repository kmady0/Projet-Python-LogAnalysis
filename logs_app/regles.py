from logs_app.analyse import comparer_blacklist, detecter_force_brute, ips_actives, ips_en_erreur
from logs_app.audit import audit

def regle_force_brute(logs, seuil=3, **autres):
    return detecter_force_brute(logs, seuil)


def regle_erreurs(logs, **autres):
    return ips_en_erreur(logs)


def regle_blacklist(logs, **autres):
    return comparer_blacklist(ips_actives(logs))["dangereuses_connectees"]


def apply_security_rules(*args, **kwargs):
    rapport = {}
    for regle in args:
        rapport[regle.__name__] = regle(**kwargs)
    audit(locals(), "apply_security_rules")
    return rapport