from monde.monde import monde
from regles.configuration import calculer_prochaine_generation
from temps.running import nouvelle_generation
from tkinter import *

fenetre, taille_grille, etat_cellules, cellules = monde()





# Associer l'événement de zoom à la fenêtre
# fenetre.bind("<MouseWheel>", zoom)

# Bouton pour passer à la génération suivante
prochaine_generation = calculer_prochaine_generation(etat_cellules, taille_grille)
bouton_generer = Button(fenetre, text="Nouvelle génération", command=lambda: nouvelle_generation(taille_grille, cellules, etat_cellules))
bouton_generer.grid(row=taille_grille, column=0, columnspan=taille_grille)

# fenetre.bind("<space>", jouer_auto(taille_grille, cellules, etat_cellules))

# Associer la barre espace à une pause
# fenetre.bind("<space>", pause)

# Lancement de la boucle principale
fenetre.mainloop()
