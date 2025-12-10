import random

def choisir_mot():
    mots = ["python", "programmation", "github", "collaboration"]
    return mots[random.randint(0, len(mots) - 1)]