import tkinter as tk






####################################################
# PARTIE 1 : GESTION DE LA PAGE INSCRIPTION
####################################################





def ouvrir_fenetre_inscription():
    """
    Cette fonction est associé au bouton_incription 
    et permet l'ouverture de la page d'inscription quand l'utilisateur clic sur ce bouton
    """
    couleur_fond="pink"
    #permet de detruir les widgets de la page precedente
    for widget in fenetre.winfo_children():#A REGARDER
        widget.destroy()

    #creation du titre
    titre=tk.Label(fenetre,text="Page d'inscription",bg=couleur_fond,fg="black",font=("Arial",90))
    titre.pack(side="top") 
    #changement du fond
    fenetre.configure(bg=couleur_fond)

    #creation du champs d'entree
    champs_pseudo=tk.Entry(fenetre)
    champs_pseudo.pack()
    champs_mdp=tk.Entry(fenetre)
    champs_mdp.pack()

    #bouton valider
    def enregistre():
        pseudo_joueur=champs_pseudo.get()
        mdp_joueur=champs_mdp.get()
        profil_joueur=[pseudo_joueur,mdp_joueur]
        """
        Cette fonction recupere le pseudo et le mot de passe du joueur (2str),
        pour ensuite les ajouter dans la base de donnée
        """
        joueur=profil_joueur
        with open('profils.txt','r',encoding='utf-8') as fichier:
            utilisateurs=fichier.read().split()
            profil_joueur=";".join(profil_joueur)
            with open('profils.txt','a',encoding='utf-8') as fichier:
                fichier.write('\n'+profil_joueur)
                fichier.close()
                print(joueur)
        for widget in fenetre.winfo_children():#A REGARDER
            widget.destroy()
        titre=tk.Label(fenetre,text="Page d'inscription",bg=couleur_fond,fg="black",font=("Arial",90))
        titre.pack(side="top")
        titre2=tk.Label(fenetre,text="Félicitation ! Vous êtes bien inscrit",bg=couleur_fond,fg="black",font=("Arial",50))
        titre2.pack()  
        bouton_jouer=tk.Button(fenetre,text="Lancer le jeu !",font=("Arial",15),bg="#141769",fg="white")
        bouton_jouer.pack()


    bouton_valider=tk.Button(fenetre,text="Valider",font=("Arial",15),bg="#141769",fg="white",command=enregistre)
    bouton_valider.pack()

    







####################################################
# PARTIE 2 : GESTION DE LA PAGE CONNEXION
####################################################






def ouvrir_fenetre_connexion():
    """
    Cette fonction est associé au bouton_connexion 
    et permet l'ouverture de la page de connexion quand l'utilisateur clic sur ce bouton
    """
    couleur_fond="pink"
    #permet de detruir les widgets de la page precedente
    for widget in fenetre.winfo_children():#A REGARDER
        widget.destroy()

    #creation du titre
    titre=tk.Label(fenetre,text="Page de connexion",bg=couleur_fond,fg="black",font=("Arial",90))
    titre.pack(side="top") 
    #changement du fond
    fenetre.configure(bg=couleur_fond)

    #creation du champs d'entree
    champs_pseudo=tk.Entry(fenetre)
    champs_pseudo.pack()
    champs_mdp=tk.Entry(fenetre)
    champs_mdp.pack()

    #bouton valider
    def verification():
        """
        Cette fonction recupere le pseudo et le mot de passe du joueur (2str),
        pour ensuite verifier qu'il est bien dans la base de données
        """
        pseudo_joueur=champs_pseudo.get()
        mdp_joueur=champs_mdp.get()
        with open('profils.txt','r',encoding='utf-8') as fichier:
            utilisateurs=fichier.read().split()
            for elem in utilisateurs:
                if str(pseudo_joueur+";"+mdp_joueur) == elem:
                    print('le profil est dans la base de données')
                    for widget in fenetre.winfo_children():#A REGARDER
                        widget.destroy()
                    titre=tk.Label(fenetre,text="Page de connexion",bg=couleur_fond,fg="black",font=("Arial",90))
                    titre.pack(side="top")
                    titre2=tk.Label(fenetre,text="Félicitation ! Vous êtes bien connecté",bg=couleur_fond,fg="black",font=("Arial",50))
                    titre2.pack()  
                    bouton_jouer=tk.Button(fenetre,text="Lancer le jeu !",font=("Arial",15),bg="#141769",fg="white")
                    bouton_jouer.pack()
                    return True
            titre3=tk.Label(fenetre,text="Votre compte n'existe pas\nRéessayer ou inscrivez-vous",bg=couleur_fond,fg="black",font=("Arial",50))
            titre3.pack()


    bouton_valider=tk.Button(fenetre,text="Valider",font=("Arial",15),bg="#141769",fg="white",command=verification)
    bouton_valider.pack()

    











####################################################
# PARTIE 3 : GESTION DE LA PAGE D'ACCEUIL
####################################################



def fermer_fenetre():
    """
    Cette fonction est associé au bouton_fermeture 
    et permet la fermeture de la page quand l'utilisateur clic sur ce bouton
    """
    fenetre.destroy()#permet de fermer la fenetre
    return fenetre
    
    

####################################################
# PARTIE 4 : GESTION FOND JEU
####################################################


def ouvrir_jeu_solo():

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

   
    # Affichage de la fenêtre
    fenetre.mainloop()



def ouvrir_fenetre_jeu_duo():
    print("hey")
    return bouton_joueur_duo





####################################################
# PARTIE 6 : Page principale
####################################################


fenetre = tk.Tk()
fenetre.state("zoomed")#permet d'ouvrire la page directement en grand ecran
fenetre.title("Page d'acceuil")
couleur_fond="#F3B065"
couleur_boutons="white"
fenetre.configure(bg=couleur_fond)


#céation titre de la page
titre_page=tk.Label(fenetre,text="Bienvenue sur le\nMastermind !",bg=couleur_fond,fg="white",font=("Impact",90))
titre_page.pack(side="top") #sa place dans la fenetre



#creation des boutons
cadre=tk.Frame(fenetre,bg=couleur_fond)#cadre où sont les 2 boutons (inscription et connexion)
cadre.pack(expand=True)

bouton_inscription=tk.Button(cadre,text="Inscription",command=ouvrir_fenetre_inscription,font=("Arial",20),bg=couleur_boutons,fg=couleur_fond)
bouton_inscription.pack(side="left",padx=100)

bouton_connexion=tk.Button(cadre,text="Connexion",command=ouvrir_fenetre_connexion,font=("Arial",20),bg=couleur_boutons,fg=couleur_fond)
bouton_connexion.pack(side="left",padx=100)

bouton_joueur_solo=tk.Button(cadre,text="jouer en solo",command=ouvrir_jeu_solo,font=("Arial",20),bg=couleur_boutons,fg=couleur_fond)
bouton_joueur_solo.pack(side="left",padx=100)

bouton_joueur_duo=tk.Button(cadre,text="jouer en duo",command=ouvrir_fenetre_jeu_duo,font=("Arial",20),bg=couleur_boutons,fg=couleur_fond)
bouton_joueur_duo.pack(side="left",padx=100)

bouton_fermeture=tk.Button(fenetre,text="Fermer la fenetre",command=fermer_fenetre,font=("Arial",20),bg=couleur_boutons,fg=couleur_fond)
bouton_fermeture.pack()



####TACHES A FAIRE
#boutton retour sur les page inscription et connexion
#boutton qui renvoie a la page d'inscription quand la connexion n'a pas reussi (si c'est possible)
#gerer l'aspect visuel
#boutton reles du jeu






fenetre.mainloop()