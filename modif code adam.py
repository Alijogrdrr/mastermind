import tkinter as tk

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("mastermind")

fenetre.state("zoomed")  # Ouvre la fenêtre en plein écran

# Configuration des colonnes
fenetre.grid_columnconfigure(0, weight=1, minsize=100)
fenetre.grid_columnconfigure(1, weight=8, minsize=300)
fenetre.grid_columnconfigure(2, weight=1, minsize=100)

# Configuration de la ligne
fenetre.grid_rowconfigure(0, weight=1, minsize=200)

# Création des carrés collés les uns aux autres
canvas_gauche = tk.Canvas(fenetre, background="black")
canvas_gauche.grid(row=0, column=0, rowspan=2, sticky="nsew")

canvas_central = tk.Canvas(fenetre, background="purple")
canvas_central.grid(row=0, column=1, rowspan=2, sticky="nsew")

canvas_droit = tk.Canvas(fenetre, background="black")
canvas_droit.grid(row=0, column=2, rowspan=2, sticky="nsew")

# Décalage horizontal pour centrer les rectangles et cercles
decalage_horizontal = 100

# Création des rectangles dans le canvas central
for i in range(0, 11):
    canvas_central.create_rectangle(470 + decalage_horizontal, 42 + i * 60, 110 + decalage_horizontal, 8 + i * 60, outline="black")

# Création des cercles dans le canvas central
for i in range(0, 11):
    for j in range(0, 4):
        canvas_central.create_oval(122 + 100 * j + decalage_horizontal, 39 + i * 60, 152 + 100 * j + decalage_horizontal, 11 + i * 60)

# Création des petits cercles blancs à gauche des lignes dans le canvas central
button_diameter = 20  # Diamètre des petits boutons
button_offset_x = 20  # Espacement horizontal entre les cercles
button_offset_y = 60  # Espacement vertical entre les lignes de cercles

def couleur_petits_boutons():
    fill = None
    for i in range (couleur_code_secret):
        if couleur_code_secret[i] == couleur_choisie[i]:
            fill = "black"
        elif couleur_code_secret[i] in couleurs_choisies:
            fill = "white"
        else:
            fill = None

import random
def couleur_code_secret():
    canvas_central.oval(row = 1, fill = random.choice(couleurs))
    couleurs = ["green", "blue", "pink", "yellow", "orange", "grey", "white"]
    return couleurs

# Positionner les cercles blancs pour les aligner avec les cercles du canvas central
for i in range(0, 11):
    for j in range(0, 4):
        # Calculer la position verticale des cercles blancs pour les aligner avec les cercles du canevas central
        y_position = 39 + i * 60 + (button_diameter // 2) - 33  # Aligné avec le centre des cercles dans les rectangles
        x_position = 50 + j * (button_diameter + button_offset_x)  # Décalage horizontal
        canvas_central.create_oval(x_position, y_position, x_position + button_diameter, y_position + button_diameter, fill= couleur_petits_boutons())




# Affichage de la fenêtre
fenetre.mainloop()