def affichage_pendu(erreur):
    #Quand on lance le script avec affichage_pendu(mettre la variable qui compte les erreur quand on entre la mauvaise lettre)
    #aucune erreur = position 0
    #possibiliter de 6 erreur total
    #Liste avec chaque dessins a des positions differentes, position 0 = 0 erreur, position 1 = 1 erreur
    
    if erreur < 0: # securiter pour chiffre trop petit
        erreur = 0
    if erreur > 6: # securiter pour chiffre trop grand
        erreur = 6
        
    dessin = ["""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""]
    print(dessin[erreur])