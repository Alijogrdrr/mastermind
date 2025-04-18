import tkinter as tk
from tkinter import ttk
import fenetre_choix_couleurs



##################variables global#####################
nb_essai=9 #cette variable est modifier a chaque essai (servira peut etre plus tard)
index_rond = 0
couleurs = ["green", "blue", "pink", "yellow", "orange", "purple"]
essai=[]#liste de 4 elements avec les couleur des rond de la ligne que l'on est entre de remplir
ronds = [[],[],[],[],[],[],[],[],[],[]]#liste intermériaire pour stocker les ronds
liste_ronds=[] #liste contenant les ronds
petits_ronds = [[],[],[],[],[],[],[],[],[],[]] #liste intermédiaire pour stocker les rondscontient (4 elem dans chaque sous liste)
liste_petit_ronds=[] #liste contenant les petits ronds

def ouvrir_jeu_duo(fenetre):
    print("je rentre dans fenetre jeu duo")
    for widget in fenetre.winfo_children():
        widget.destroy()  # Détruit les widgets existants
    fenetre.configure(bg='white')
    code_secret=fenetre_choix_couleurs.ouvrir_fenetre_Duo(fenetre)
    print(code_secret)
    ##############################################################################################
    # PARTIE 1 : CREATION DE LA FENETRE + CANVAS
    ##############################################################################################

    # Récupére la largeur et hauteur de la fenetre (nous serivra pour le redimentionnement)
    largeur_fenetre = int(fenetre.winfo_width())
    hauteur_fenetre = int(fenetre.winfo_height())




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
    # PARTIE 2 : CREATION DE LA GRILLE DU JEU DANS LE CANVAS CENTRAL
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



    ##############################################################################################
    # PARTIE 3 : CREATION DES RONDS DU CANVAS CENTRAL
    ##############################################################################################


    #coordonnées pour les cercles
    cercle_y1=1/12*hauteur_canvas+5
    cercle_y2=2/12*hauteur_canvas-5

    #dessin des 4 cercles des 10 lignes
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





    #coordonnées pour les petit cercles de verification
    petit_cercle_y1=1/12*hauteur_canvas+3                             #une ligne du canvas 
    petit_cercle_y2=1/12*hauteur_canvas+1/2*(1/12*hauteur_canvas)-3   #une ligne du canvas + une demi-ligne


    #position des cercles de verification pour chaque ligne
    for i in range(10):
        petit_cercle_x1=25
        petit_cercle_x2=1/2*(1/5*largeur_canvas)-25
        for j in range (2):#boucle pour les 2 ronds du haut du rectangle
            rond_verification=canvas.create_oval(petit_cercle_x1,petit_cercle_y1,petit_cercle_x2,petit_cercle_y2,width=1,fill="white")
            petits_ronds[i].append(rond_verification)
            petit_cercle_x1+=1/2*(1/5*largeur_canvas)
            petit_cercle_x2+=1/2*(1/5*largeur_canvas)
        #on remet les X au bord du canvas et on descend les Y
        petit_cercle_x1=25                       
        petit_cercle_x2=1/2*(1/5*largeur_canvas)-25
        petit_cercle_y1+=1/2*(1/12*hauteur_canvas)
        petit_cercle_y2+=1/2*(1/12*hauteur_canvas)
        for j in range (2):#boucle pour les 2 ronds du bas du rectangle
            rond_verification=canvas.create_oval(petit_cercle_x1,petit_cercle_y1,petit_cercle_x2,petit_cercle_y2,width=1,fill="white")
            petit_cercle_x1+=1/2*(1/5*largeur_canvas)
            petit_cercle_x2+=1/2*(1/5*largeur_canvas)
        petit_cercle_y1+=1/2*(1/12*hauteur_canvas)
        petit_cercle_y2+=1/2*(1/12*hauteur_canvas)
    for elem in petits_ronds:#sert a renverser la liste
        liste_petit_ronds.insert(0,elem)



    ###############################################################################################
    # PARTIE 4 : GESTION DU CHANGEMENT DE COULEUR DES RONDS
    ###############################################################################################




    def colorer_rond(couleur):
        """
        Cette fonction prend en parametre la couleur du bouton qui a ete cliquer et
        change le couleur des rond correspondant
        """
        global index_rond
        global nb_essai
        global essai
        if 0<=nb_essai<=9:
            if couleur=="grey":
                if essai!=[]:
                    essai.pop()
                    index_rond-=1
                    canvas.itemconfig(ronds[nb_essai][index_rond], fill="grey") #changement de la couleur du rond
                
            elif index_rond < len(ronds[nb_essai]):
                essai.append(couleur)
                canvas.itemconfig(ronds[nb_essai][index_rond], fill=couleur) #changement de la couleur du rond
                index_rond += 1





    ###############################################################################################
    # PARTIE 5 : GESTION DE LA VERIFICATION DES COULEUR RENTREES PAR LE JOUEUR 2
    ###############################################################################################


    def verifie_couleur():
        global nb_essai
        global index_rond
        global essai
        essai =[]
        index_rond=0
        nb_essai-=1


    def verifie_couleur2():
        """
        Cette fonction permet de au deuxieme joueur,(apres l'appuis du bouton valider) , de rentrer le code couleur des petit rond en fonction des couleur
        """
        global code_secret
        ##########partie pour la fenetre de selection du score
        fenetre_score_duo = tk.Toplevel(fenetre)
        fenetre_score_duo.title("Mode Deux Joueurs")
        fenetre_score_duo.geometry("600x600")
        fenetre_score_duo.configure(bg="pink")

        titre = tk.Label(fenetre_score_duo, text="Entrer le code couleur du score", bg="pink", fg="black", font=("Arial", 30))
        titre.pack(pady=20)

        couleurs_disponibles = ["black", "white","red"]
        code_score = []

        def ajouter_couleur():
            """
            Cette fonction ouvre une nouvelle fenetre pour que le deuxieme joueur selection le code du score
            """
            while len(code_score) < 4:
                couleur_choisie = combo.get()
                if couleur_choisie:
                    code_score.append(couleur_choisie)
                    liste_couleurs.config(text="Code du score : " + " - ".join(code_score))

                if len(code_secret) == 4:
                    bouton_ajouter_score.config(state="disabled")
                    bouton_lancer_score.config(state="normal")  # Active le bouton de lancement

        label = tk.Label(fenetre_score_duo, text="Choisissez 4 couleurs :", bg="pink", font=("Arial", 16))
        label.pack(pady=10)

        combo = ttk.Combobox(fenetre_score_duo, values=couleurs_disponibles, state="readonly")
        combo.pack(pady=5)

        bouton_ajouter_score = tk.Button(fenetre_score_duo, text="Ajouter", command=ajouter_couleur, font=("Arial", 16), bg="white")
        bouton_ajouter_score.pack(pady=10)

        # Bouton pour lancer le jeu (désactivé au départ)
        bouton_lancer_score = tk.Button(fenetre_score_duo, text="Continuer le jeu", font=("Arial", 16), bg="white", fg="black", state="disabled", command=fenetre_score_duo.destroy())
        bouton_lancer_score.pack(pady=20)

        liste_couleurs = tk.Label(fenetre_score_duo, text="Code secret : ", bg="pink", font=("Arial", 16))
        liste_couleurs.pack(pady=10)



        ##########partie de la coloration des petits boutons

        global index_rond
        global nb_essai
        for couleurs in code_score:
                canvas.itemconfig(petits_ronds[nb_essai][index_rond], fill=couleurs) #changement de la couleur du rond
                index_rond += 1
        index_rond=0
        nb_essai-=1







    ##############################################################################################
    # PARTIE 6 : AJOUT DES BOUTONS DANS LE CANVAS DROIT
    ##############################################################################################


    # Ajout de boutons correspondant aux couleurs
    for couleur in couleurs:
        bouton = tk.Button(canvas_droit, text=couleur, bg=couleur, command=lambda c=couleur: colorer_rond(c),font=("Arial",30))   #???
        bouton.pack(pady=10)
    bouton_valider = tk.Button(canvas_droit, text="Valider", command=verifie_couleur,font=("Arial",30),relief="solid")  
    bouton_valider.pack(pady=10)
    bouton_annuler = tk.Button(canvas_droit, text="Annuler", command=lambda c="grey": colorer_rond(c),font=("Arial",30),relief="solid")  
    bouton_annuler.pack(pady=10)


    



