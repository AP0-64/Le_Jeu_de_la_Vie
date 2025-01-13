# Fonction qui alterne l'état de la cellule
def changement_etat(etat_cellules, evenement, ligne, colonne):
    etat_actuel = etat_cellules[ligne][colonne]
    nouvel_etat = 1 if etat_actuel == 0 else 0  # Alterne entre 0 et 1
    etat_cellules[ligne][colonne] = nouvel_etat  # Met à jour le tableau 2D

    # Mettre à jour la couleur du bouton
    nouvel_etat = "white" if nouvel_etat == 1 else "black"
    evenement.widget.config(bg=nouvel_etat)
    return

def compter_voisins_vivants(etat_cellules, ligne, colonne, taille_grille):
    voisins = [
        (1, -1), (1, 0), (1, 1),
        (0, -1),           (0, 1),
        (-1, -1), (-1, 0), (-1, 1)
    ]
    compteur = 0
    for dx, dy in voisins:
        x, y = ligne + dx, colonne + dy
        if 0 <= x < taille_grille and 0 <= y < taille_grille:
            compteur += etat_cellules[x][y]
    return compteur

def calculer_prochaine_generation(etat_cellules, taille_grille):
    prochaine_generation = [[0 for _ in range(taille_grille)] for _ in range(taille_grille)]
    for i in range(taille_grille):
        for j in range(taille_grille):
            voisins_vivants = compter_voisins_vivants(etat_cellules, i, j, taille_grille)
            if etat_cellules[i][j] == 1:  # Cellule vivante
                if voisins_vivants == 2 or voisins_vivants == 3:
                    prochaine_generation[i][j] = 1
            else:  # Cellule morte
                if voisins_vivants == 3:
                    prochaine_generation[i][j] = 1
    return prochaine_generation

def mettre_a_jour_interface(cellules, etat_cellules):
    for i, ligne in enumerate(cellules):
        for j, cellule in enumerate(ligne):
            nouvel_etat = "white" if etat_cellules[i][j] == 1 else "black"
            cellule.config(bg=nouvel_etat)
