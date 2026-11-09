from collections import defaultdict

BLACKLIST: frozenset[str] = frozenset({"10.0.0.5", "45.33.12.8", "1.1.1.1"})


def ips_en_erreur(logs: list[dict]) -> set[str]:
    ips = set()
    for log in logs:
        if log["niveau"] in ("ERROR", "CRITICAL"):
            ips.add(log["ip"])
    return ips


def ips_actives(logs: list[dict]) -> set[str]:
    ips = set()
    for log in logs:
        ips.add(log["ip"])
    return ips


def comparer_blacklist(actives: set[str]) -> dict:
    return {
        "union": BLACKLIST | actives,
        "dangereuses_connectees": BLACKLIST & actives,
        "non_suspectes": actives - BLACKLIST,
        "un_seul_groupe": BLACKLIST ^ actives,
    }


def compter_par(logs: list[dict], cle: str) -> dict[str, int]:
    compteur = defaultdict(int)
    for log in logs:
        compteur[log[cle]] += 1
    return dict(compteur)


def detecter_force_brute(logs: list[dict], seuil: int = 3) -> set[str]:
    suspects = set()
    for ip in ips_actives(logs):
        echecs = 0
        i = 0
        while i < len(logs):
            log = logs[i]
            i += 1
            if log["ip"] != ip:
                continue
            if log["message"] == "Mot de passe incorrect":
                echecs += 1
            else:
                echecs = 0
            if echecs >= seuil:
                print(f"ALERTE : force brute depuis {ip}")
                suspects.add(ip)
                break
        else:
            print(f"OK : aucune attaque depuis {ip}")
    return suspects