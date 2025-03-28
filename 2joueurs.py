import tkinter as tk
from tkinter import ttk

def ouvrir_fenetre_Duo():
    """
    Ouvre une fenêtre où le joueur peut choisir un code secret de 4 couleurs.
    """
    couleur_fond = "pink"

    # Création d'une nouvelle fenêtre
    fenetre_Duo = tk.Toplevel(root)
    fenetre_Duo.title("Mode Deux Joueurs")
    fenetre_Duo.geometry("800x600")
    fenetre_Duo.configure(bg=couleur_fond)

    # Création du titre
    titre = tk.Label(fenetre_Duo, text="Mode Deux Joueurs", bg=couleur_fond, fg="black", font=("Arial", 30))
    titre.pack(side="top", pady=20)

    # Liste des couleurs disponibles
    couleurs_disponibles = ["Rouge", "Bleu", "Vert", "Jaune", "Orange", "Violet"]
    code_secret = []

    def ajouter_couleur():
        """ Ajoute une couleur au code secret si la limite de 4 n'est pas atteinte. """
        if len(code_secret) < 4:
            couleur_choisie = combo.get()
            if couleur_choisie:
                code_secret.append(couleur_choisie)
                liste_couleurs.config(text="Code secret : " + " - ".join(code_secret))
            
            # Désactiver le bouton si 4 couleurs sont choisies
            if len(code_secret) == 4:
                bouton_ajouter.config(state="disabled")

    # Label et liste déroulante
    label = tk.Label(fenetre_Duo, text="Choisissez 4 couleurs :", bg=couleur_fond, font=("Arial", 16))
    label.pack(pady=10)

    combo = ttk.Combobox(fenetre_Duo, values=couleurs_disponibles, state="readonly")
    combo.pack(pady=5)

    bouton_ajouter = tk.Button(fenetre_Duo, text="Ajouter", command=ajouter_couleur, font=("Arial", 16), bg="white")
    bouton_ajouter.pack(pady=10)

    liste_couleurs = tk.Label(fenetre_Duo, text="Code secret : ", bg=couleur_fond, font=("Arial", 16))
    liste_couleurs.pack(pady=10)

# Fenêtre principale
root = tk.Tk()
root.title("Jeu")
root.geometry("800x600")

# Bouton Joueur Duo
bouton_joueur_duo = tk.Button(root, text="Jouer en duo", command=ouvrir_fenetre_Duo, font=("Arial", 20), bg="lightblue")
bouton_joueur_duo.pack(pady=50)

root.mainloop()
