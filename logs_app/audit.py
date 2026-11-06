def audit(portee, titre, fichier="audit.txt"):
    with open(fichier, "a", encoding="utf-8") as f:
        f.write(f"=== Audit : {titre} ===\n")
        for nom, valeur in portee.items():
            if nom.startswith("__"):
                continue
            f.write(f"{nom} : {type(valeur).__name__}\n")
        f.write("\n")