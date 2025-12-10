# Structure initiale
bibliotheque = []

def ajouter_livre(titre, auteur):
    pass

def afficher_livres():
    pass

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
    if int(choix_utilisateur) == 1:
        titre_a_ajouter = input("\nEntrez le titre du livre a ajouter: ")
        auteur_a_ajouter = input("\nEntrez le nom de l'auteur du livre a ajouter: ")        
        ajouter_livre(titre_a_ajouter, auteur_a_ajouter)
        print(f"\nLivre: {titre_a_ajouter} par {auteur_a_ajouter} ")
    elif int(choix_utilisateur) == 2:
        afficher_livres()
    elif int(choix_utilisateur) == 3:
        titre_a_rechercher = input("\nEntrez le titre du livre a rechercher: ")
        rechercher_livre(titre_a_rechercher)
        print(f"\nRecherche de: {titre_a_rechercher}")
        pass
    if int(choix_utilisateur) == 4:
        break

print("Au revoir!")