# Structure initiale
bibliotheque = []

def ajouter_livre(titre, auteur):
    if titre in bibliotheque:
        print("Livre existe déja dans la biblitheque")
    else:
        bibliotheque.append({"titre": titre, "auteur": auteur})


def afficher_livres():
    print(bibliotheque)

def rechercher_livre(titre):
    pass

choix_utilisateur = 0

menu_principal = """
Choisissez une fonction:
1- Ajouter un livre
2- Afficher les livres
3- Rechercher un livre
4- Quitter
"""

while True:
    print(menu_principal)
    choix_utilisateur = input("Entrez un choix de 1 à 4: ")

    if choix_utilisateur == "1":     #menu Ajouter un livre
        titre_a_ajouter = input("\nEntrez le titre du livre a ajouter: ")
        auteur_a_ajouter = input("\nEntrez le nom de l'auteur du livre a ajouter: ")        
        ajouter_livre(titre_a_ajouter, auteur_a_ajouter)    #appel de la fonction avec les variables qui seront entrees par l'utilisateur lors des 2 inputs
        print(f"\nLivre: {titre_a_ajouter} par {auteur_a_ajouter} ")    #pour tests, verification que les variables sont bien attribuees

    elif choix_utilisateur == "2": #menu Afficher les livres
        afficher_livres()

    elif choix_utilisateur == "3":   #menu Recherche un livre (par titre)
        titre_a_rechercher = input("\nEntrez le titre du livre a rechercher: ")
        rechercher_livre(titre_a_rechercher)
        print(f"\nRecherche de: {titre_a_rechercher}")
        

    elif choix_utilisateur == "4":     #menu Quitter
        break

    else:
        print("\nCe choix est invalide")

print("Au revoir!")