# Structure de départ (Personne 1)
def main():
    print(f"""=== MENU DU RESTAURANT ===
    
------ Entrees ------

{afficher_entrees()}

-- Plats Principaux --

{afficher_plats_principaux()}

------ Desserts ------

{afficher_desserts()}""")
# Les autres ajouteront leur code ici

def afficher_entrees():
    return ("entrees")

def afficher_plats_principaux():

    return("plats principaux")


def afficher_entrees():
    return("""
~Salade César classique~
    Croûtons maison, parmesan frais, vinaigrette crémeuse.
~Bruschetta~
    Tomates fraîches, basilic, huile d'olive, servie sur pain grillé.
~Soupe crémeuse de légumes~
    Velouté léger, parfait pour commencer sans être trop lourd.
""")


def afficher_desserts():
    return("""-Tarte au Sucre
-Croustade aux pommes
-Creme glacée""")

        
if __name__ == "__main__":
    main()



