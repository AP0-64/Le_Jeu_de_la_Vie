

def zoom(evenement):
    global taille_cellule
    if evenement.delta > 0 and taille_cellule > 4:  # Molette vers le haut (zoom avant)
        taille_cellule += 2
    elif evenement.delta < 0:  # Molette vers le bas (zoom arrière) avec une taille minimale
        taille_cellule -= 2

    # Mettre à jour la taille des boutons
    for i in range(taille_grille):
        for j in range(taille_grille):
            boutons[i][j].config(width=taille_cellule, height=int(taille_cellule / 2))
    return
