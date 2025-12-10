# Structure initiale
bibliotheque = []

def ajouter_livre(titre, auteur):
    if titre in bibliotheque:
        print("Livre existe déja dans la biblitheque")
    else:
        bibliotheque.append({"titre": titre, "auteur": auteur})


def afficher_livres():
    pass

def rechercher_livre(titre):
    pass