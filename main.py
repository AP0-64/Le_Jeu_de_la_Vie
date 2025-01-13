from monde.monde import monde
from temps.running import avancer_automatiquement, arret_marche
from tkinter import *



# Variable Tkinter
fenetre, taille_grille, etat_cellules, cellules = monde()

def bouton_arret_marche():
    """Gère l'état d'automatisation et actualise le texte du bouton."""
    etat = arret_marche()  # Inverse l'état de `running`
    bouton_auto.config(text="Pause" if etat else "Démarrer")
    avancer_automatiquement(fenetre, taille_grille, cellules, etat_cellules)

bouton_auto = Button(fenetre, text="Démarrer", command=bouton_arret_marche)
bouton_auto.grid(row=taille_grille, column=0, columnspan=taille_grille)

# Associer l'événement de zoom à la fenêtre
# fenetre.bind("<MouseWheel>", zoom)

# fenetre.bind("<space>", jouer_auto(taille_grille, cellules, etat_cellules))

# Associer la barre espace à une pause
# fenetre.bind("<space>", pause)

# Lancement de la boucle principale
fenetre.mainloop()
