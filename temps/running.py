from regles.configuration import calculer_prochaine_generation
from regles.configuration import mettre_a_jour_interface
from tkinter import *

# Fonction pour générer une nouvelle génération
def nouvelle_generation(taille_grille, cellules, etat_cellules):
    prochaine_generation = calculer_prochaine_generation(etat_cellules, taille_grille)
    mettre_a_jour_interface(cellules, prochaine_generation)
    # Mettre à jour `etat_cellules` avec le nouvel état
    for i in range(taille_grille):
        for j in range(taille_grille):
            etat_cellules[i][j] = prochaine_generation[i][j]
    return
