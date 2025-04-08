import tkinter as tk
import random

################## Variables globales #################
nb_essai = 0  # Compteur d'essais
index_rond = 0
couleurs = ["green", "blue", "pink", "yellow", "orange", "purple"]
essai = []  # Liste des couleurs pour chaque ligne d'essai
code_secret = []  # Code secret à deviner

# Fonction pour générer un code secret aléatoire
def couleur_code_secret():
    global code_secret
    code_secret = random.sample(couleurs, 4)  # Code secret avec 4 couleurs aléatoires
    print("Les couleurs à deviner dans cet ordre sont:", code_secret)

couleur_code_secret()

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.update()
fenetre.state("zoomed")

# Récupération des dimensions de la fenêtre
largeur_fenetre = fenetre.winfo_width()
hauteur_fenetre = fenetre.winfo_height()

# Création du canvas principal
canvas = tk.Canvas(fenetre, width=4/8*largeur_fenetre, height=hauteur_fenetre, highlightthickness=5, highlightbackground="pink")
canvas.update()
canvas.pack()

# Création du canvas droit pour les boutons de sélection des couleurs
canvas_droit = tk.Canvas(fenetre, width=1/8*largeur_fenetre, height=hauteur_fenetre)
canvas_droit.place(x=largeur_fenetre - (1.5/8 * largeur_fenetre))

# Création du plateau de jeu (grille avec 10 lignes et 4 colonnes pour les couleurs)
ronds = [[], [], [], [], [], [], [], [], [], []]

# Coordonnées pour les ronds
cercle_y1 = 1/12 * hauteur_fenetre + 5
cercle_y2 = 2/12 * hauteur_fenetre - 5
for i in range(10):
    cercle_x1 = 1/5 * largeur_fenetre + 50
    cercle_x2 = 2/5 * largeur_fenetre - 50
    for j in range(4):
        rond = canvas.create_oval(cercle_x1, cercle_y1, cercle_x2, cercle_y2, width=3, fill="grey")
        ronds[i].append(rond)
        cercle_x1 += 1/5 * largeur_fenetre
        cercle_x2 += 1/5 * largeur_fenetre
    cercle_y1 += 1/12 * hauteur_fenetre
    cercle_y2 += 1/12 * hauteur_fenetre

# Fonction pour vérifier les couleurs après chaque essai
def verifie_couleur():
    global nb_essai, essai, code_secret
    liste_placement = [0, 0, 0]  # [bonnes places, mauvaises places, couleurs non présentes]

    if len(essai) != 4:
        print("Veuillez remplir toute la ligne avant de valider.")
        return  # Vérifie si la ligne est complète

    # Comparaison des couleurs
    for i in range(4):
        if essai[i] == code_secret[i]:
            canvas.itemconfig(ronds[nb_essai][i], fill="black")  # Bonnes couleurs et bonnes positions
        elif essai[i] in code_secret:
            canvas.itemconfig(ronds[nb_essai][i], fill="white")  # Couleurs présentes mais mal placées
        else:
            canvas.itemconfig(ronds[nb_essai][i], fill="grey")  # Couleur absente

    nb_essai += 1
    essai.clear()  # Réinitialise l'essai pour la ligne suivante

# Fonction pour changer la couleur d'un rond dans l'essai
def colorer_rond(couleur):
    global index_rond, essai, nb_essai
    if couleur == "grey" and essai:
        essai.pop()
        index_rond -= 1
        canvas.itemconfig(ronds[nb_essai][index_rond], fill="grey")  # Remet le rond en gris
    elif index_rond < 4:
        essai.append(couleur)
        canvas.itemconfig(ronds[nb_essai][index_rond], fill=couleur)  # Change la couleur du rond
        index_rond += 1

# Création des boutons de couleurs
for couleur in couleurs:
    bouton = tk.Button(canvas_droit, text=couleur, bg=couleur, command=lambda c=couleur: colorer_rond(c), font=("Arial", 30))
    bouton.pack(pady=10)

# Création des boutons de validation et d'annulation
bouton_valider = tk.Button(canvas_droit, text="Valider", command=verifie_couleur, font=("Arial", 30), relief="solid")
bouton_valider.pack(pady=10)
bouton_annuler = tk.Button(canvas_droit, text="Annuler", command=lambda: colorer_rond("grey"), font=("Arial", 30), relief="solid")
bouton_annuler.pack(pady=10)

# Lancement de la fenêtre principale
fenetre.mainloop()
