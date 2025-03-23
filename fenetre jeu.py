import tkinter as tk




fenetre = tk.Tk()
fenetre.update()
fenetre.state("zoomed")#permet d'ouvrire la page directement en grand ecran
# Récupére la largeur et hauteur de la fenetre (nous serivra pour le redimentionnement)
largeur_fenetre = int(fenetre.winfo_width())
hauteur_fenetre = int(fenetre.winfo_height())

print(largeur_fenetre,hauteur_fenetre)


# Dimensions du canvas central
canvas=tk.Canvas(fenetre,width=4/8*largeur_fenetre,height=hauteur_fenetre,highlightbackground="pink")
canvas.update()
canvas.pack()

#Récupere la largeur et la heuteur du canvas central
largeur_canvas=int(canvas.cget('width'))
hauteur_canvas=int(canvas.cget('heignt'))
print(largeur_canvas,hauteur_canvas)


#creation du grand rectangle global du plateau de jeu (prennant 4/5 du canvas centre decallé a droite)
canvas.create_rectangle((2//8*largeur_fenetre)+(1//5*largeur_canvas),1//12*hauteur_canvas , (2//8*largeur_fenetre)+largeur_canvas,11//12*hauteur_canvas , outline="black",fill="gray")

# coordonnées pour les 9 lignes a tracer a l'interieur du recangle
ligne_x1=2//8*largeur_fenetre #je les fait aller jusqu'au bout du canvas pour avoir la partie pour mettre les resultats de la ligne
ligne_y=2//12*hauteur_canvas
ligne_x2=(2//8*largeur_fenetre)+largeur_canvas
#coordonnées pour les cercles
cercle_x1=(2//8*largeur_fenetre)+(1//5*largeur_canvas)
cercle_y1=1//12*hauteur_canvas
cercle_x2=(2//8*largeur_fenetre)+(1//5*largeur_canvas)
cercle_y2=2//12*hauteur_canvas

# dessin des lignes pour separer le grand rectangle 
for lignes in range(11):
    canvas.create_line(ligne_x1, ligne_y, ligne_x2, ligne_y, width=4, fill="red")
    ligne_y+=1/12*hauteur_canvas

# Dessine les 4 cercles d'une ligne
for i in range(10):
    for j in range (3):
        canvas.create_oval(cercle_x1,cercle_y1,cercle_x2,cercle_y2,width=3,outline="black")
        cercle_x1+=1//5*largeur_canvas
        cercle_x2+=1//5*largeur_canvas
    cercle_y1+=1//12*hauteur_canvas
    cercle_y2+=1//12*hauteur_canvas


   
# Affichage de la fenêtre
fenetre.mainloop()
