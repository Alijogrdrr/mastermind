import tkinter as tk
from tkinter import ttk

####################################################
# PARTIE 1 : GESTION DE LA PAGE D'ACCUEIL
####################################################

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.state("zoomed")  # Ouvre en plein écran
fenetre.title("Mastermind")
couleur_fond = "#9B59B6"
couleur_boutons = "white"
fenetre.configure(bg=couleur_fond)

# Création du titre de la page

titre = tk.Label(fenetre, text="Mastermind", font=("Impact", 50), fg="black", bg="#9B59B6")
titre.pack(pady=50)

# Ajout d'une bordure lumineuse
titre.config(highlightbackground="black", highlightthickness=5)

# Création des boutons dans un cadre
cadre = tk.Frame(fenetre, bg=couleur_fond)
cadre.pack(expand=True)

def fermer_fenetre():
    # Ferme la fenêtre principale
    fenetre.destroy()

####################################################
# PARTIE 2 : GESTION DE L'INSCRIPTION
####################################################

def ouvrir_fenetre_inscription():

    #Ouvre la fenêtre d'inscription,Cette fonction est associé au bouton_incription 
    for widget in fenetre.winfo_children():
        widget.destroy()
#changement du fond
    couleur_fond = "pink"
    fenetre.configure(bg=couleur_fond)

#creation du titre
    titre = tk.Label(fenetre, text="Page d'inscription", bg=couleur_fond, fg="black", font=("Poppins", 50))
    titre.pack()

#creation du champs d'entree
    champs_pseudo = tk.Entry(fenetre)
    champs_pseudo.pack()
    champs_mdp = tk.Entry(fenetre, show="*")  # Cachera le mot de passe
    champs_mdp.pack()

#creation du champs d'entree
    def enregistrer():
        pseudo = champs_pseudo.get()
        mdp = champs_mdp.get()
        if pseudo and mdp:
            with open('profils.txt', 'a', encoding='utf-8') as fichier:
                fichier.write(f'\n{pseudo};{mdp}')
            retour_accueil()

    bouton_valider = tk.Button(fenetre, text="Valider", font=("Arial", 15), bg="#141769", fg="white", command=enregistrer)
    bouton_valider.pack()

    bouton_retour = tk.Button(fenetre, text="Retour", font=("Arial", 15), bg="red", fg="white", command=retour_accueil)
    bouton_retour.pack(pady=10)

####################################################
# PARTIE 3 : GESTION DE LA CONNEXION
####################################################

def ouvrir_fenetre_connexion():

    #Cette fonction est associé au bouton_connexion et permet l'ouverture de la page de connexion quand l'utilisateur clic sur ce bouton
    for widget in fenetre.winfo_children():
        widget.destroy()
#changement du fond
    couleur_fond = "pink"
    fenetre.configure(bg=couleur_fond)

    #creation du titre
    titre = tk.Label(fenetre, text="Page de connexion", bg=couleur_fond, fg="black", font=("Arial", 50))
    titre.pack()

    champs_pseudo = tk.Entry(fenetre)
    champs_pseudo.pack()
    champs_mdp = tk.Entry(fenetre, show="*")
    champs_mdp.pack()

    #bouton valider
    def verifier():
        pseudo = champs_pseudo.get()
        mdp = champs_mdp.get()
        with open('profils.txt', 'r', encoding='utf-8') as fichier:
            utilisateurs = fichier.read().splitlines()
            if f"{pseudo};{mdp}" in utilisateurs:
                retour_accueil()
            else:
                erreur = tk.Label(fenetre, text="Compte invalide. Réessayez ou inscrivez-vous.", bg=couleur_fond, fg="red", font=("Arial", 16))
                erreur.pack()

    bouton_valider = tk.Button(fenetre, text="Valider", font=("Arial", 15), bg="#141769", fg="white", command=verifier)
    bouton_valider.pack()

    bouton_retour = tk.Button(fenetre, text="Retour", font=("Arial", 15), bg="red", fg="white", command=retour_accueil)
    bouton_retour.pack(pady=10)

####################################################
# PARTIE 4 : MODE DUO - CHOIX DU CODE SECRET
####################################################

def ouvrir_fenetre_Duo():
    #Ouvre la fenêtre du mode Duo pour choisir un code couleur secret
    fenetre_Duo = tk.Toplevel(fenetre)
    fenetre_Duo.title("Mode Deux Joueurs")
    fenetre_Duo.geometry("800x600")
    fenetre_Duo.configure(bg="pink")

    titre = tk.Label(fenetre_Duo, text="Mode Deux Joueurs", bg="pink", fg="black", font=("Arial", 30))
    titre.pack(pady=20)

    couleurs_disponibles = ["Rouge", "Bleu", "Vert", "Jaune", "Orange", "Violet"]
    code_secret = []

    def lancer_jeu():
        # Fonction appelée lorsque le jeu commence
        print("Le jeu commence avec le code :", code_secret)
        fenetre_Duo.destroy()

    def ajouter_couleur():
        # Ajoute une couleur au code secret
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

    bouton_ajouter = tk.Button(fenetre_Duo, text="Ajouter", command=ajouter_couleur, font=("Arial", 16), bg="white")
    bouton_ajouter.pack(pady=10)

    # Bouton pour lancer le jeu (désactivé au départ)
    bouton_lancer = tk.Button(fenetre_Duo, text="Lancer le jeu", font=("Arial", 16), bg="white", fg="black", state="disabled", command=lancer_jeu)
    bouton_lancer.pack(pady=20)

    liste_couleurs = tk.Label(fenetre_Duo, text="Code secret : ", bg="pink", font=("Arial", 16))
    liste_couleurs.pack(pady=10)

####################################################
# AJOUT DES BOUTONS PRINCIPAUX
####################################################

def retour_accueil():
    # Revenir à l'écran d'accueil
    for widget in fenetre.winfo_children():
        widget.destroy()
    
    titre_page.pack(side="top")
    cadre.pack(expand=True)
    bouton_fermeture.pack()

bouton_inscription = tk.Button(cadre, text="Inscription", command=ouvrir_fenetre_inscription, font=("Arial", 20), bg=couleur_boutons, fg=couleur_fond)
bouton_inscription.pack(side="left", padx=50)

bouton_connexion = tk.Button(cadre, text="Connexion", command=ouvrir_fenetre_connexion, font=("Arial", 20), bg=couleur_boutons, fg=couleur_fond)
bouton_connexion.pack(side="left", padx=50)

bouton_joueur_duo = tk.Button(cadre, text="Jouer en duo", command=ouvrir_fenetre_Duo, font=("Arial", 20), bg=couleur_boutons, fg=couleur_fond)
bouton_joueur_duo.pack(side="left", padx=50)

bouton_fermeture = tk.Button(fenetre, text="Fermer", command=fermer_fenetre, font=("Arial", 20), bg="red", fg="white")
bouton_fermeture.pack()

fenetre.mainloop()