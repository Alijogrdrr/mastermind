import tkinter as tk
import random




##################variables global#################
nb_essai=9 #cette variable est modifier a chaque essai (servira peut etre plus tard)
index_rond = 0
couleurs = ["green", "blue", "pink", "yellow", "orange", "purple"]
essai=[]#liste de 4 elements avec les couleurs des ronds de la ligne que l'on est entre de remplir
code_secret=[] #comptient 4 couleurs parmis "couleurs" generrer aléatoirement et sera le code a deviner
liste_ronds=[] #liste contenant les ronds
liste_petit_ronds=[] #liste contenant les petits ronds

##############################################################################################
# PARTIE 1 : CREATION DE LA FENETRE + CANVAS
##############################################################################################

fenetre = tk.Tk()
fenetre.update()
fenetre.state("zoomed")#permet d'ouvrire la page directement en grand ecran
# Récupére la largeur et hauteur de la fenetre (nous serivra pour le redimentionnement)
largeur_fenetre = int(fenetre.winfo_width())
hauteur_fenetre = int(fenetre.winfo_height())

print(largeur_fenetre,hauteur_fenetre)


#generation du code secret 

def couleur_code_secret():
    """
    Cette fonction sert a generer un code culeur qui sera le code couleur que l'utilistaeur devrait trouver
    """
    global couleurs
    global code_secret
    code_secret = [random.choice(couleurs) for _ in range(4)]  # Génère 4 couleurs aléatoires
    print("Les coulurs a deviner dans cet ordre sont:", code_secret)

couleur_code_secret()


#creation du canvas central
canvas=tk.Canvas(fenetre,width=4/8*largeur_fenetre,height=hauteur_fenetre,highlightthickness=5,highlightbackground="pink")
canvas.update()
canvas.pack()

#Récupere la largeur et la heuteur du canvas central
largeur_canvas=int(canvas.cget('width'))
hauteur_canvas=int(canvas.cget('height'))
print(largeur_canvas,hauteur_canvas)



# je vais creer le canevas droit
canvas_droit = tk.Canvas(fenetre, width=1/8*largeur_fenetre, height=hauteur_fenetre)
canvas_droit.place(x=largeur_fenetre-(1.5/8*largeur_fenetre),)




##############################################################################################
# PARTIE 2 : CREATION DE LA GRILLE DU JEU + RONDS
##############################################################################################


#creation du grand rectangle global du plateau de jeu (prennant 4/5 du canvas centre decallé a droite)
rectangle=canvas.create_rectangle(1/5*largeur_canvas,1/12*hauteur_canvas ,largeur_canvas,11/12*hauteur_canvas ,width=4, outline="black",fill="grey")

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
        rond=canvas.create_oval(cercle_x1,cercle_y1,cercle_x2,cercle_y2,width=3,fill="grey")
        ronds[i].append(rond)
        cercle_x1+=1/5*largeur_canvas
        cercle_x2+=1/5*largeur_canvas
    cercle_y1+=1/12*hauteur_canvas
    cercle_y2+=1/12*hauteur_canvas
for elem in ronds:#sert a renverser la liste
    liste_ronds.insert(0,elem)

#je cree une liste pour stocker les ronds
petits_ronds = [[],[],[],[],[],[],[],[],[],[]] #contient 4 elem dans chaque sous liste

#coordonnées pour les petit cercles de verification

petit_cercle_y1=1/12*hauteur_canvas+3                             #une ligne du canvas 
petit_cercle_y2=1/12*hauteur_canvas+1/2*(1/12*hauteur_canvas)-3   #une ligne du canvas + une demi-ligne


#position des cercles de verification pour chaque ligne
# Position des cercles de vérification pour chaque ligne
for i in range(10):
    petit_cercle_x1 = 25
    petit_cercle_x2 = 1/2 * (1/5 * largeur_canvas) - 25

    # Boucle pour les 4 petits ronds (2 en haut, 2 en bas)
    for j in range(4):
        rond_verification = canvas.create_oval(
            petit_cercle_x1, petit_cercle_y1, petit_cercle_x2, petit_cercle_y2, width=1, fill="pink"
        )
        petits_ronds[i].append(rond_verification)

        # Avancer les coordonnées pour les ronds suivants
        petit_cercle_x1 += 1/2 * (1/5 * largeur_canvas)
        petit_cercle_x2 += 1/2 * (1/5 * largeur_canvas)

        # Après 2 ronds, descendre pour les 2 ronds du bas
        if j == 1:
            petit_cercle_x1 = 25
            petit_cercle_x2 = 1/2 * (1/5 * largeur_canvas) - 25
            petit_cercle_y1 += 1/2 * (1/12 * hauteur_canvas)
            petit_cercle_y2 += 1/2 * (1/12 * hauteur_canvas)

    # Remettre les Y pour la prochaine ligne
    petit_cercle_y1 += 1/2 * (1/12 * hauteur_canvas)
    petit_cercle_y2 += 1/2 * (1/12 * hauteur_canvas)

###############################################################################################
# PARTIE 4 : GESTION DU CHANGEMENT DE COULEUR DES RONDS
###############################################################################################



def colorer_rond(couleur):
    """
    Cette fonction prend en parametre la couleur du bouton qui a ete cliquer et
    change le couleur des ronds correspondant
    """
    global index_rond
    global nb_essai
    global essai
    if couleur=="grey":
        if essai!=[]:
            essai.pop()
            index_rond-=1
            canvas.itemconfig(ronds[nb_essai][index_rond], fill="grey") #changement de la couleur du rond
        else:
            index_rond-=1
    elif index_rond < len(ronds[nb_essai]):
        essai.append(couleur)
        canvas.itemconfig(ronds[nb_essai][index_rond], fill=couleur) #changement de la couleur du rond
        index_rond += 1





###############################################################################################
# PARTIE 4 : GESTION DE LA VERIFICATION DES COULEUR RENTREES
###############################################################################################
def verifie_couleur():
    global nb_essai
    global index_rond
    global essai
    essai=[]
    index_rond=0
    nb_essai-=1

def verifie_couleur2():
    """
    Cette fonction permet de verifier apres l'appuis du bouton valider, si les coueleur existe/sont a la bonne place/ou sont presente
    et modifie la couleur 
    """
    global nb_essai
    global code_secret
    global essai


    #si la ligne n'est pas complétée
    if len(essai) != 4:
        erreur=tk.Label(fenetre,text="Attention vous ne pouvez pas valider\nsans avoir remplie toute la ligne",fg="red",font=("Impact",15))
        erreur.pack(side="right")
        return #on arrête tout si c'est pas complet
    
    liste_placement=[0,0,0]#liste_placement[0]= les couleurs bien placees,   liste_placement[1]= les couleurs presentes mais mal placee,   liste_placement[2]= les couleurs pas presentes
    #si la ligne est complétée
    for i in range(4):
            if essai[i]==code_secret[i]:#verifie si cette couleur est a la bonne place
                canvas.itemconfig(petits_ronds[nb_essai][i], fill="black") #changement de la couleur du rond
                liste_placement[0] += 1

            elif essai[i]!=code_secret[i] and essai[i] in code_secret:#regarde si cette couleur est dans la liste mais pas a la bonne place
                canvas.itemconfig(petits_ronds[nb_essai][i], fill="white") #changement de la couleur du rond
                liste_placement[1] += 1

            else:#sinon cette couleur est pas presente
                canvas.itemconfig(petits_ronds[nb_essai][i], fill="grey") #changement de la couleur du rond
                liste_placement[2] += 1

    #il faut pas que les petits ronds de vérification soient dans le même ordre que les ronds qu'on a rempli pour trouver le code secret, sinon c'est trop facile on devine quelle couleur 
    #est pas à la bonne place et tout, trop facile, donc on mélange la liste
    import random
    random.shuffle(liste_placement)


    nb_essai -= 1
    essai=[]
    index_rond=0
    print("Resultat de la vérification:",liste_placement)



##############################################################################################
# PARTIE 3 : AJOUT DES BOUTONS DANS LE CANVAS DROIT
##############################################################################################


# Ajout de boutons correspondant aux couleurs
for couleur in couleurs:
    bouton = tk.Button(canvas_droit, text=couleur, bg=couleur, command=lambda c=couleur: colorer_rond(c),font=("Arial",30))   #???
    bouton.pack(pady=10)
bouton_valider = tk.Button(canvas_droit, text="Valider", command=verifie_couleur2,font=("Arial",30),relief="solid")  
bouton_valider.pack(pady=10)
bouton_annuler = tk.Button(canvas_droit, text="Annuler", command=lambda c="grey": colorer_rond(c),font=("Arial",30),relief="solid")  
bouton_annuler.pack(pady=10)
   

#Affichage de la fenêtre
fenetre.mainloop()