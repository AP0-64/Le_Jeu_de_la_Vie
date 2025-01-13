from tkinter import *
from regles.configuration import changement_etat

# Création du monde (interface graphique et lien avec le tableau)
def creation_tableau_cellules(taille_grille, fenetre):
    # Tableau 2D pour stocker les états des cellules (0 = mort, 1 = vivant)
    etat_cellules = [[0 for _ in range(taille_grille)] for _ in range(taille_grille)]  # États logiques
    cellules = []  # Liste pour stocker les celulles

    for i in range(taille_grille):
        ligne_cellules = []
        for j in range(taille_grille):
            # Créer un bouton pour chaque cellule
            cellule = Button(fenetre, width=5, height=2, bg="black")
            cellule.grid(row=i, column=j)
            # Associer la position (i, j) au clic
            cellule.bind("<Button-1>", lambda event, x=i, y=j: changement_etat(etat_cellules, event, x, y))
            ligne_cellules.append(cellule)
        cellules.append(ligne_cellules)

    return etat_cellules, cellules
