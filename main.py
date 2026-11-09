from logs_app.analyse import comparer_blacklist, compter_par, ips_actives
from logs_app.audit import audit
from logs_app.ingestion import lire_plusieurs_fichiers
from logs_app.regles import apply_security_rules, regle_blacklist, regle_erreurs, regle_force_brute
from logs_app.transformation import pipeline, router

FICHIERS = ["data/logs1.txt", "data/logs2.txt"]


def main() -> None:
    print("=== 1. Ingestion et transformation ===")
    lignes = lire_plusieurs_fichiers(FICHIERS)
    logs = list(pipeline(lignes))
    print(f"{len(logs)} logs valides")

    print("\n=== 2. Routage des formats (match-case) ===")
    for log in logs:
        print(router(log["message"]), "|", router(log["source"]))

    print("\n=== 3. Statistiques ===")
    print("Par niveau :", compter_par(logs, "niveau"))
    print("Par utilisateur :", compter_par(logs, "utilisateur"))

    print("\n=== 4. Blacklist ===")
    for nom, ips in comparer_blacklist(ips_actives(logs)).items():
        print(f"{nom} : {sorted(ips)}")

    print("\n=== 5. Moteur de regles ===")
    rapport = apply_security_rules(regle_force_brute, regle_erreurs, regle_blacklist, logs=logs, seuil=3)
    for nom, resultat in rapport.items():
        print(f"{nom} : {sorted(resultat)}")

    audit(globals(), "main.py")
    print("\nRapport d'audit ecrit dans audit.txt")


if __name__ == "__main__":
    main()