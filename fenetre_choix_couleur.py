import tkinter as tk
from tkinter import ttk



####################################################
# PARTIE : MODE DUO - CHOIX DU CODE SECRET
####################################################

def ouvrir_fenetre_Duo(fenetre):
    """
    Cette fonction ouvre la fenêtre du mode Duo pour choisir un code couleur secret
    """
    print("je rentre dans le choix du code secret")
    fenetre_Duo = tk.Toplevel(fenetre)
    fenetre_Duo.title("Mode Deux Joueurs")
    fenetre_Duo.geometry("800x600")
    fenetre_Duo.configure(bg="pink")

    titre = tk.Label(fenetre_Duo, text="Mode Deux Joueurs", bg="pink", fg="black", font=("Arial", 30))
    titre.pack(pady=20)

    couleurs_disponibles = ["Rouge", "Bleu", "Vert", "Jaune", "Orange", "Violet"]
    code_secret = []

    def lancer_jeu(code_secret):
        """
        Fonction appelée lorsque le jeu commence
        """
        print("Le jeu commence avec le code :", code_secret)
        fenetre_Duo.destroy()
        return code_secret

    def ajouter_couleur(code_secret):
        """
        Ajoute une couleur au code secret
        """
        if len(code_secret) < 4:
            couleur_choisie = combo.get()
            if couleur_choisie:
                code_secret.append(couleur_choisie)
                liste_couleurs.config(text="Code secret : " + " - ".join(code_secret))

            if len(code_secret) == 4:
                bouton_ajouter.config(state="disabled")
                bouton_lancer.config(state="normal")  # Active le bouton de lancement
            

    label = tk.Label(fenetre_Duo, text="Choisissez 4 couleurs :", bg="pink", font=("Arial", 16))
    label.pack(pady=10)

    combo = ttk.Combobox(fenetre_Duo, values=couleurs_disponibles, state="readonly")
    combo.pack(pady=5)

    bouton_ajouter = tk.Button(fenetre_Duo, text="Ajouter", command=lambda: ajouter_couleur(code_secret), font=("Arial", 16), bg="white")
    bouton_ajouter.pack(pady=10)

    # Bouton pour lancer le jeu (désactivé au départ)
    bouton_lancer = tk.Button(fenetre_Duo, text="Lancer le jeu", font=("Arial", 16), bg="white", fg="black", state="disabled", command=lambda: lancer_jeu(code_secret))
    bouton_lancer.pack(pady=20)

    liste_couleurs = tk.Label(fenetre_Duo, text="Code secret : ", bg="pink", font=("Arial", 16))
    liste_couleurs.pack(pady=10)

    return code_secret