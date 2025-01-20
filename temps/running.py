from regles.configuration import calculer_prochaine_generation
from regles.configuration import mettre_a_jour_interface
from tkinter import *

# Variables globales
running = False  # État de l'automatisation (jeu en pause ou en cours)
vitesse = 1  # Intervalle de temps entre chaque génération (en ms)

# Fonction pour générer une nouvelle génération
def nouvelle_generation(taille_grille, cellules, etat_cellules):
    prochaine_generation = calculer_prochaine_generation(etat_cellules, taille_grille)
    mettre_a_jour_interface(cellules, prochaine_generation)
    # Mettre à jour `etat_cellules` avec le nouvel état
    for i in range(taille_grille):
        for j in range(taille_grille):
            etat_cellules[i][j] = prochaine_generation[i][j]
    return

def arret_marche():
    """Active ou désactive l'avancement automatique."""
    global running
    running = not running
    return

def avancer_automatiquement(fenetre: Tk, taille_grille, cellules, etat_cellules):
    """Fait avancer le jeu automatiquement si running est actif."""
    global running
    if running:
        from temps.running import nouvelle_generation  # Import local pour éviter les dépendances circulaires
        nouvelle_generation(taille_grille, cellules, etat_cellules)
        # Appelle cette fonction après un délai (si toujours actif)
        fenetre.after(vitesse, avancer_automatiquement, fenetre, taille_grille, cellules, etat_cellules)
    return

def bouton_arret_marche(fenetre, taille_grille, cellules, etat_cellules):
    """Gère l'état d'automatisation."""
    arret_marche()  # Inverse l'état de `running`
    avancer_automatiquement(fenetre, taille_grille, cellules, etat_cellules)
    return

def vitesse_X1(event=None):
    global vitesse
    vitesse = 500
    return vitesse

def vitesse_X2(event=None):
    global vitesse
    vitesse = 1
    return vitesse
