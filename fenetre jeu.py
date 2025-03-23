import tkinter as tk


    

####################################################
# PARTIE 4 : GESTION FOND JEU
####################################################

fenetre = tk.Tk()
fenetre.update()
fenetre.state("zoomed")#permet d'ouvrire la page directement en grand ecran
# Récupére la largeur et hauteur de la fenetre (nous serivra pour le redimentionnement)
largeur_fenetre = int(fenetre.winfo_width())
hauteur_fenetre = int(fenetre.winfo_height())

print(largeur_fenetre,hauteur_fenetre)


# Dimensions du canvas central
canvas=tk.Canvas(fenetre,width=4/8*largeur_fenetre,height=hauteur_fenetre,highlightthickness=5,highlightbackground="pink")
canvas.update()
canvas.pack()

#Récupere la largeur et la heuteur du canvas central
largeur_canvas=int(canvas.cget('width'))
hauteur_canvas=int(canvas.cget('height'))
print(largeur_canvas,hauteur_canvas)


#creation du grand rectangle global du plateau de jeu (prennant 4/5 du canvas centre decallé a droite)
rectangle=canvas.create_rectangle(1/5*largeur_canvas,1/12*hauteur_canvas ,largeur_canvas,11/12*hauteur_canvas ,width=4, outline="black",fill="gray")

#coordonnées pour les 9 lignes a tracer a l'interieur du recangle
ligne_x1=0 #je les fait aller jusqu'au bout du canvas pour avoir la partie pour mettre les resultats de la ligne
ligne_y=2/12*hauteur_canvas
ligne_x2=largeur_canvas


#dessin des lignes pour separer le grand rectangle 
for lignes in range(11):
    canvas.create_line(ligne_x1, ligne_y, ligne_x2, ligne_y, width=4, fill="black")
    ligne_y+=1/12*hauteur_canvas

 #je cree une liste pour stocker les ronds
ronds = [[],[],[],[],[],[],[],[],[],[]]


#coordonnées pour les cercles
cercle_y1=1/12*hauteur_canvas+5
cercle_y2=2/12*hauteur_canvas-5

#dessin des 4 cercles d'une ligne
for i in range(10):
    cercle_x1=1/5*largeur_canvas +50 #le 50 sert a faire des rond et non des oval, car les cases sont rectagulaire et non carré
    cercle_x2=2/5*largeur_canvas-50
    for j in range (4):
        rond=canvas.create_oval(cercle_x1,cercle_y1,cercle_x2,cercle_y2,width=3,fill="gray")
        ronds[i].append(rond)
        cercle_x1+=1/5*largeur_canvas
        cercle_x2+=1/5*largeur_canvas
    cercle_y1+=1/12*hauteur_canvas
    cercle_y2+=1/12*hauteur_canvas

    
print(ronds)
####################################################
# PARTIE 4 : GESTION FOND choisir couleur
####################################################

#variables
nb_essai=0
index_rond = 0
couleurs = ["green", "blue", "pink", "yellow", "orange", "grey", "white"]


def verifie_couleur():
    global nb_essai
    nb_essai+=1
    print(nb_essai)
    

# je vais creer un canevas
canvas_droit = tk.Canvas(fenetre, width=1/8*largeur_fenetre, height=hauteur_fenetre)
canvas_droit.place(x=largeur_fenetre-(1.5/8*largeur_fenetre),)


def colorer_rond(couleur):
    global index_rond
    global nb_essai
    if index_rond < len(ronds[nb_essai]):
        canvas.itemconfig(ronds[nb_essai][index_rond], fill=couleur)
        index_rond += 1


# Ajout de boutons correspondant aux couleurs
for couleur in couleurs:
    bouton = tk.Button(canvas_droit, text=couleur, bg=couleur, command=lambda c=couleur: colorer_rond(c),font=("Arial",30))   #???
    bouton.pack(pady=10)
bouton = tk.Button(canvas_droit, text="Valider", command=verifie_couleur,font=("Arial",30),relief="solid")  
bouton.pack(pady=10)
   
   
# Affichage de la fenêtre
fenetre.mainloop()





