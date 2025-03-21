import tkinter as tk

fenetre_echec = tk.Tk()
fenetre_echec.title("oops... perdu ...")
fenetre_echec.geometry("400x300")
fenetre_echec.config(bg="grey")

fenetre_echec.state("zoomed")

# Fonction "Recommencer"
def recommencer():
    """Renvoie sur la première fenêtre pour recommencer la partie"""
    print("Recommencer la partie")  # Ajoute une action (sinon ne fait rien)
    # Ici, tu pourrais ajouter du code pour relancer la partie

# Fonction "Arrêter de jouer"
def stopjeu():
    print("Arrêt du jeu")
    fenetre_echec.quit()

# Création du label d'échec
labelechec = tk.Label(fenetre_echec, text="Tu as perdu...", font=("Helvetica", 30), bg="grey")
labelechec.pack(pady=50)  # Pour laisser un peu d'espace autour du texte

# Bouton "Recommencer"
buttonrecommencer = tk.Button(fenetre_echec, text="Cliques ici pour recommencer", font=("Helvetica", 30), command=recommencer)
buttonrecommencer.pack(side="left", padx=50)

# Bouton "Arrêter de jouer"
buttonstop = tk.Button(fenetre_echec, text="Arrêter de jouer", font=("Helvetica", 30), command=stopjeu)
buttonstop.pack(side="right", padx=50)

fenetre_echec.mainloop()
