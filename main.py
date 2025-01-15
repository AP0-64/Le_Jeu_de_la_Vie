from monde.monde import monde
from temps.running import bouton_arret_marche, vitesse_X1, vitesse_X2
from tkinter import *

# Variable Tkinter
fenetre, taille_grille, etat_cellules, cellules = monde()

# Associer la barre espace à une pause
fenetre.bind("<space>", lambda event: bouton_arret_marche(fenetre, taille_grille, cellules, etat_cellules))

# Bouton 1, 2, 3 associer aux changements de vitesse
fenetre.bind("<KeyPress-1>", vitesse_X1)
fenetre.bind("<KeyPress-2>", vitesse_X2)

# Associer l'événement de zoom à la fenêtre
# fenetre.bind("<MouseWheel>", zoom)

# Lancement de la boucle principale
fenetre.mainloop()
