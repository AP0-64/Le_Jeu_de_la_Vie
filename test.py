import tkinter as tk

# Initialisation des variables globales
running = True  # Indique si le jeu est en cours
temps = 0  # Simule l'avancée du temps

def boucle_jeu():
    """Boucle principale du jeu."""
    global temps
    if running:
        # Incrémenter le temps
        temps += 1
        label_temps.config(text=f"Temps : {temps}")

        # Ajouter ici la logique du jeu

    # Reprogrammer la fonction pour être appelée après 100 ms
    fenetre.after(100, boucle_jeu)

def toggle_pause():
    """Met le jeu en pause ou reprend."""
    global running
    running = not running
    bouton_pause.config(text="Reprendre" if not running else "Pause")

# Création de la fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Jeu avec boucle sans classe")

# Création d'un label pour afficher le temps
label_temps = tk.Label(fenetre, text=f"Temps : {temps}")
label_temps.pack()

# Création d'un bouton pour mettre en pause ou reprendre
bouton_pause = tk.Button(fenetre, text="Pause", command=toggle_pause)
bouton_pause.pack()

# Démarrer la boucle de jeu
boucle_jeu()

# Lancer la boucle principale de Tkinter
fenetre.mainloop()
