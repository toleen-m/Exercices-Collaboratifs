import random
from affichage import affichage_pendu
from mots import choisir_mot
from jeu import jouer_tour


secret_word = choisir_mot()
erreur = 0
guess_word = "_" * len(secret_word)
guess_word_liste = list(guess_word)


affichage_pendu(erreur)
print(f"{guess_word} | erreurs : {erreur}")


while True:
    lettre = input("Entrez une lettre : ").lower()

    bonne_lettre = jouer_tour(secret_word, guess_word_liste, lettre)
    if bonne_lettre == True:
        affichage_pendu(erreur)
    elif bonne_lettre == False:
        print("\n\tMauvaise lettre !")
        erreur += 1
        affichage_pendu(erreur)
    guess_word = "".join(guess_word_liste)

    print(f"{guess_word} | erreurs : {erreur}")


    # si le mot secret n'a plus de _ le joureur a gagné
    if "_" not in guess_word:
        print("Mot trouvé !")
        break

    # si le nombre de vie est à 0, le joueur a perdu
    elif erreur >= 6:
        print("Perdu !")
        print(f"Le mot secret était : {secret_word} !")
        break

