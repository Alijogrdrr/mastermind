import tkinter as tk
import random

################## Variables globales #################
nb_essai = 9
index_rond = 0
couleurs = ["green", "blue", "pink", "yellow", "orange", "purple"]
couleurs_verif = ["black", "white", "grey"]
essai = []
code_secret = [] 
liste_ronds = []
liste_petit_ronds = []
erreur_label = None  # Label d'erreur

verification_en_cours = False  # Si le joueur 2 vérifie les couleurs
ligne_courante = 0


##############################################################################################
# PARTIE 1 : CREATION DE LA FENETRE + CANVAS
##############################################################################################

fenetre = tk.Tk()
fenetre.update()
fenetre.state("zoomed")
largeur_fenetre = int(fenetre.winfo_width())
hauteur_fenetre = int(fenetre.winfo_height())

print(largeur_fenetre,hauteur_fenetre)

# Frame pour afficher les erreurs
frame_erreur = tk.Frame(fenetre)
frame_erreur.pack(side="bottom", pady=10)

# Génération du code secret
def couleur_code_secret():
    global code_secret
    code_secret = [random.choice(couleurs) for _ in range(4)]
    print("Les couleurs à deviner sont :", code_secret)

couleur_code_secret()

# Canevas pour afficher les éléments du jeu
canvas = tk.Canvas(fenetre, width=4/8*largeur_fenetre, height=hauteur_fenetre, highlightthickness=5, highlightbackground="pink")
canvas.pack()
largeur_canvas = int(canvas.cget('width'))
hauteur_canvas = int(canvas.cget('height'))

# Canevas pour les boutons à droite
canvas_droit = tk.Canvas(fenetre, width=1/8*largeur_fenetre, height=hauteur_fenetre)
canvas_droit.place(x=largeur_fenetre - (1.5/8 * largeur_fenetre))


##############################################################################################
# PARTIE 2 : CREATION DE LA GRILLE DU JEU + RONDS
##############################################################################################

rectangle = canvas.create_rectangle(1/5*largeur_canvas, 1/12*hauteur_canvas, largeur_canvas, 11/12*hauteur_canvas, width=4, outline="black", fill="grey")

#coordonnées pour les 9 lignes a tracer a l'interieur du recangle
ligne_x1=0 #je les fait aller jusqu'au bout du canvas pour avoir la partie pour mettre les resultats de la ligne
ligne_y=2/12*hauteur_canvas
ligne_x2=largeur_canvas


#dessin des lignes pour separer le grand rectangle 
for lignes in range(11):
    canvas.create_line(ligne_x1, ligne_y, ligne_x2, ligne_y, width=4, fill="black")
    ligne_y+=1/12*hauteur_canvas

# Création des ronds pour les essais du joueur 1
ronds = [[] for _ in range(10)]
cercle_y1 = 1/12*hauteur_canvas + 5
cercle_y2 = 2/12*hauteur_canvas - 5

for i in range(10):
    cercle_x1 = 1/5*largeur_canvas + 50
    cercle_x2 = 2/5*largeur_canvas - 50
    for j in range(4):
        rond = canvas.create_oval(cercle_x1, cercle_y1, cercle_x2, cercle_y2, width=3, fill="grey")
        ronds[i].append(rond)
        cercle_x1 += 1/5*largeur_canvas
        cercle_x2 += 1/5*largeur_canvas
    cercle_y1 += 1/12*hauteur_canvas
    cercle_y2 += 1/12*hauteur_canvas
for elem in ronds:
    liste_ronds.insert(0, elem)

# Création des petits ronds pour la vérification
petits_ronds = [[] for _ in range(10)]
petit_cercle_y1 = 1/12*hauteur_canvas + 3
petit_cercle_y2 = petit_cercle_y1 + 1/2*(1/12*hauteur_canvas) - 6
for i in range(10):
    petit_cercle_x1 = 25
    petit_cercle_x2 = 1/2 * (1/5 * largeur_canvas) - 25
    for j in range(4):
        rond_verification = canvas.create_oval(petit_cercle_x1, petit_cercle_y1, petit_cercle_x2, petit_cercle_y2, width=1, fill="pink")
        petits_ronds[i].append(rond_verification)
        petit_cercle_x1 += 1/2 * (1/5 * largeur_canvas)
        petit_cercle_x2 += 1/2 * (1/5 * largeur_canvas)
        if j == 1:
            petit_cercle_x1 = 25
            petit_cercle_x2 = 1/2 * (1/5 * largeur_canvas) - 25
            petit_cercle_y1 += 1/2 * (1/12 * hauteur_canvas)
            petit_cercle_y2 += 1/2 * (1/12 * hauteur_canvas)
    petit_cercle_y1 += 1/2 * (1/12 * hauteur_canvas)
    petit_cercle_y2 += 1/2 * (1/12 * hauteur_canvas)
for elem in petits_ronds:
    liste_petit_ronds.insert(0, elem)

# Fonction pour colorier un rond
def colorer_rond(couleur):
    global index_rond, nb_essai, essai
    if couleur == "grey":
        if essai:
            essai.pop()
            index_rond -= 1
            canvas.itemconfig(liste_ronds[nb_essai][index_rond], fill="grey")
        else:
            index_rond-=1
    elif index_rond < 4:
        essai.append(couleur)
        canvas.itemconfig(liste_ronds[nb_essai][index_rond], fill=couleur)
        index_rond += 1

###############################################################################################
# PARTIE 4 : GESTION DE LA VERIFICATION DES COULEUR RENTREES
###############################################################################################
def choisir_couleur_verif(couleur):
    if verification_en_cours:
        for i in range(4):
            couleur_actuelle = canvas.itemcget(liste_petit_ronds[nb_essai][i], "fill")
            if couleur_actuelle == "pink":
                canvas.itemconfig(liste_petit_ronds[nb_essai][i], fill=couleur)
                break

# Fonction pour que le joueur 1 valide son essai
def valider_essai_joueur1():
    global verification_en_cours, erreur_label
    if len(essai) != 4:
        if erreur_label:
            erreur_label.destroy()
        erreur_label = tk.Label(frame_erreur, text="Remplissez 4 couleurs avant de valider.", fg="red", font=("Arial", 14))
        erreur_label.pack()
        return
    verification_en_cours = True
    print("Joueur 1 a validé son essai :", essai)
    print("Joueur 2, choisis les couleurs de vérification.")

# Fonction pour que le joueur 2 valide les couleurs
def valider_verification_joueur2():
    global nb_essai, index_rond, essai, verification_en_cours, erreur_label
    couleurs_utilisees = [canvas.itemcget(r, "fill") for r in liste_petit_ronds[nb_essai]]
    if not all(c in couleurs_verif for c in couleurs_utilisees):
        if erreur_label:
            erreur_label.destroy()
        erreur_label = tk.Label(frame_erreur, text="Tous les petits ronds doivent être colorés par le joueur 2.", fg="red", font=("Arial", 14))
        erreur_label.pack()
        return
    print("Joueur 2 a validé :", couleurs_utilisees)
    nb_essai -= 1
    index_rond = 0
    essai = []
    verification_en_cours = False

# Boutons pour le joueur 1
for couleur in couleurs:
    bouton = tk.Button(canvas_droit, text=couleur, bg=couleur, command=lambda c=couleur: colorer_rond(c), font=("Arial", 20), relief="solid")
    bouton.pack(pady=5)

tk.Button(canvas_droit, text="Annuler", command=lambda: colorer_rond("grey"), font=("Arial", 20), relief="solid").pack(pady=10)
tk.Button(canvas_droit, text="Valider (Joueur 1)", command=valider_essai_joueur1, font=("Arial", 20), relief="solid").pack(pady=10)

# Boutons pour le joueur 2
for couleur in couleurs_verif:
    bouton = tk.Button(canvas_droit, text=couleur, bg=couleur, command=lambda c=couleur: choisir_couleur_verif(c), font=("Arial", 20))
    bouton.pack(pady=5)

tk.Button(canvas_droit, text="Valider (Joueur 2)", command=valider_verification_joueur2, font=("Arial", 20), relief="solid").pack(pady=20)

fenetre.mainloop()
