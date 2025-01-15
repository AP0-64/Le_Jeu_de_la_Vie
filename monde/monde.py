from monde.cellule import creation_tableau_cellules
from tkinter import *

def monde():
    # Taille de la grille
    taille_grille = 50

    # Création de la fenêtre
    fenetre = Tk()
    fenetre.title("Le jeu de la vie")

    # Création des cellules
    etat_cellules, cellules = creation_tableau_cellules(taille_grille, fenetre)

    return fenetre, taille_grille, etat_cellules, cellules
