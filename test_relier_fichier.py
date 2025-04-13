import tkinter as tk

def ouvrir_jeu_solo(fenetre):
    for widget in fenetre.winfo_children():
        widget.destroy()  # Détruit les widgets existants

    # Configuration des colonnes et lignes de la fenêtre
    fenetre.grid_columnconfigure(0, weight=1, minsize=100)
    fenetre.grid_columnconfigure(1, weight=8, minsize=300)
    fenetre.grid_columnconfigure(2, weight=1, minsize=100)
    fenetre.grid_rowconfigure(0, weight=1, minsize=200)

    # Création des Canvas
    canvas_gauche = tk.Canvas(fenetre, background="#C18543")
    canvas_gauche.grid(row=0, column=0, rowspan=2, sticky="nsew")

    canvas_central = tk.Canvas(fenetre, background="#8D5416")
    canvas_central.grid(row=0, column=1, rowspan=2, sticky="nsew")

    canvas_droit = tk.Canvas(fenetre, background="#C18543")
    canvas_droit.grid(row=0, column=2, rowspan=2, sticky="nsew")

    # Dimensions du canvas central
    canvas_largeur = 400  # Largeur totale
    canvas_hauteur = 700  # Hauteur totale
    canvas_central.config(width=canvas_largeur, height=canvas_hauteur)

    # Calcul des tailles de la grille
    ligne_hauteur = canvas_hauteur / 11
    colonne_largeur = canvas_largeur / 10

    # Paramètres des cercles
    cercle_diametre = colonne_largeur * 1.5  # Diamètre des cercles ajusté
    espace_cercles = colonne_largeur * 0.2

    # Centrage vertical
    decalage_vertical = (canvas_hauteur - ((cercle_diametre + 20) * 10) - 90) / 2

    for i in range(10):
        # Calcul de la hauteur du rectangle en fonction des cercles
        rect_y1 = decalage_vertical + i * (cercle_diametre + 40)
        rect_y2 = rect_y1 + cercle_diametre + 20  # Ajusté selon la taille des cercles

        # Largeur du rectangle en fonction des cercles
        rect_x1 = colonne_largeur * 1.5
        rect_x2 = colonne_largeur * 8.5

        # Dessin du rectangle
        canvas_central.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, outline="black")

        # Calcul pour centrer les cercles horizontalement
        espace_total = (rect_x2 - rect_x1) - (4 * cercle_diametre)
        espace_entre_cercles = espace_total / 5

        for j in range(4):
            circle_x1 = rect_x1 + espace_entre_cercles * (j + 1) + cercle_diametre * j
            circle_x2 = circle_x1 + cercle_diametre
            circle_y1 = rect_y1 + 10  # Laisse un peu d'espace en haut
            circle_y2 = circle_y1 + cercle_diametre

            # Dessine chaque cercle
            canvas_central.create_oval(circle_x1, circle_y1, circle_x2, circle_y2, outline="black")

    # Création d'un canevas droit
    canvas = tk.Canvas(canvas_droit, width=450, height=200, bg="white")
    canvas.pack()

    couleurs = ["green", "blue", "pink", "yellow", "orange", "grey", "white"]
    ronds = []

    for i in range(4):
        rond = canvas.create_oval(50 + i * 100, 75, 100 + i * 100, 125, fill="white")
        ronds.append(rond)

    index_rond = 0


    # Création d'un cadre pour les boutons
    cadre1 = tk.Frame(canvas_droit)
    cadre1.pack()


    def colorer_rond(couleur):
        global index_rond
        if index_rond < len(ronds):
            canvas.itemconfig(ronds[index_rond], fill=couleur)
            index_rond += 1


    # Ajout de boutons correspondant aux couleurs
    for couleur in couleurs:
        bouton = tk.Button(cadre1, text=couleur, bg=couleur, command=lambda c=couleur: colorer_rond(c))
        bouton.pack(side="left")










