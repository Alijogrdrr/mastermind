import tkinter as tk
import random
from tkinter import ttk




####TACHES A FAIRE############
#gerer l'aspect visuel
#boutton reles du jeu
#bouton retour pour le jeu
#fonction aide et sauvegarde
#flouter les bouttons de verification quand je joueur 1 est entrain de remplir
#boutton retour pour la verification du mode duo
#boutton retour pour le choix des couleur de code secret en mode duo









#####################################################################################################################
################### LA PAGE D'ACCUEIL
#####################################################################################################################

#Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.update()
fenetre.state("zoomed")  # Ouvre en plein écran
fenetre.title("Mastermind")
couleur_fond = "#C9DFE5"
couleur_boutons = "white"
couleur_ecriture="#283747"
fenetre.configure(bg=couleur_fond)

#Création du titre de la page
titre = tk.Label(fenetre, text="Mastermind", font=("Segoe print", 70), fg=couleur_ecriture, bg=couleur_fond)
titre.pack(pady=50)

#Ajout d'une bordure lumineuse
titre.config(highlightbackground=couleur_ecriture, highlightthickness=5)

#Création des boutons dans un cadre
cadre = tk.Frame(fenetre, bg=couleur_fond)
cadre.pack(expand=True)


def fermer_fenetre():
    """
    Cette foncton permet de fermer la fenetre d'acceuil
    """
    fenetre.destroy()



bouton_joueur_solo=tk.Button(cadre,text="Jouer en solo",command=lambda: ouvrir_jeu_solo(fenetre,"mode_solo"),font=("Fixedsys",30),bg=couleur_boutons,fg=couleur_ecriture,width=17, height=3, relief="groove", bd=10)
bouton_joueur_solo.pack(side="left",padx=50,pady=50)

bouton_joueur_duo = tk.Button(cadre, text="Jouer en duo", command=lambda: ouvrir_fenetre_choix_couleur(fenetre), font=("Fixedsys", 30), bg=couleur_boutons, fg=couleur_ecriture,width=17, height=3, relief="groove", bd=10)
bouton_joueur_duo.pack(side="left", padx=50,pady=50)

bouton_regles_jeu = tk.Button(cadre, text="Règles du jeu", font=("Fixedsys", 30), bg=couleur_boutons, fg=couleur_ecriture,width=17, height=3, relief="groove", bd=10)
bouton_regles_jeu.pack(side="left", padx=50,pady=50)

bouton_fermeture = tk.Button(fenetre, text="Fermer", command=fermer_fenetre, font=("Fixedsys", 20), bg=couleur_boutons, fg=couleur_ecriture,width=10, height=2, relief="ridge", bd=6)
bouton_fermeture.pack()








####################################################################################################################################
#############    FENETRE JEU SOLO
###################################################################################################################################
    
def ouvrir_jeu_solo(fenetre,mode_de_jeu):
    """
    Cette fonction sert a l'ouverture et a l'execution de la page du jeu solo
    """


    ##################variables global#####################
    nb_essai=9 #cette variable est modifier a chaque essai 
    index_rond = 0
    couleurs = ["green", "blue", "pink", "yellow", "orange", "purple"]
    essai=[]#liste de 4 elements avec les couleur des rond de la ligne que l'on est entre de remplir
    ronds = [[],[],[],[],[],[],[],[],[],[]]#liste intermériaire pour stocker les ronds
    liste_ronds=[] #liste contenant les ronds
    petits_ronds = [[],[],[],[],[],[],[],[],[],[]] #liste intermédiaire pour stocker les rondscontient (4 elem dans chaque sous liste)
    erreur_label = None  # Label d'erreur
    verification_en_cours = False  # Si le joueur 2 vérifie les couleurs
    couleurs_verif = ["#229954","#ffa600", "#A93226",]
    

    def couleur_code_genere():
            """
            Cette fonction sert a generer un code couleur qui sera le code couleur que l'utilistaeur devrait trouver
            """
            code_genere=[]
            for _ in range(4):
                code_genere.append(random.choice(couleurs))
            print("Les couleurs a deviner dans cet ordre sont:", code_genere)
            return code_genere



    if mode_de_jeu=="mode_solo":
        code_secret=couleur_code_genere()
        
        print("je rentre dans fenetre jeu solo")
    else:#sinon le code secret est directement dans la variable mode de jeu
        code_secret=mode_de_jeu
        print("je rentre dans fenetre jeu duo")




    #############################################
    # PARTIE 1 : CREATION DE LA FENETRE + CANVAS
    #############################################

    for widget in fenetre.winfo_children():
        widget.destroy()  # Détruit les widgets existants
    fenetre.configure(bg='white')
    
    # Récupére la largeur et hauteur de la fenetre (nous serivra pour le redimentionnement)
    largeur_fenetre = int(fenetre.winfo_width())
    hauteur_fenetre = int(fenetre.winfo_height())



    #creation du canvas central
    canvas=tk.Canvas(fenetre,width=4/8*largeur_fenetre,height=hauteur_fenetre,highlightthickness=5,highlightbackground=couleur_ecriture,bg="white")
    canvas.update()
    canvas.pack()
    #Récupere la largeur et la heuteur du canvas central
    largeur_canvas=int(canvas.cget('width'))
    hauteur_canvas=int(canvas.cget('height'))
    print(largeur_canvas,hauteur_canvas)



    # je vais creer le canevas droit et gauche
    canvas_droit = tk.Canvas(fenetre, width=1/8*largeur_fenetre, height=hauteur_fenetre,bg="white")
    canvas_droit.place(x=largeur_fenetre-(1.5/8*largeur_fenetre))
    canvas_gauche=tk.Canvas(fenetre, width=1/8*largeur_fenetre, height=hauteur_fenetre,bg="white")
    canvas_gauche.place(x=0)



    ################################################################
    # PARTIE 2 : CREATION DE LA GRILLE DU JEU DANS LE CANVAS CENTRAL
    ################################################################


    #creation du grand rectangle global du plateau de jeu (prennant 4/5 du canvas centre decallé a droite)
    rectangle=canvas.create_rectangle(1/5*largeur_canvas,1/12*hauteur_canvas ,largeur_canvas,11/12*hauteur_canvas ,width=4, outline=couleur_ecriture,fill=couleur_fond)

    #coordonnées pour les 9 lignes a tracer a l'interieur du recangle
    ligne_x1=0 #je les fait aller jusqu'au bout du canvas pour avoir la partie pour mettre les resultats de la ligne
    ligne_y=2/12*hauteur_canvas
    ligne_x2=largeur_canvas


    #dessin des lignes pour separer le grand rectangle 
    for lignes in range(11):
        canvas.create_line(ligne_x1, ligne_y, ligne_x2, ligne_y, width=4, fill=couleur_ecriture)
        ligne_y+=1/12*hauteur_canvas



    ##################################################
    # PARTIE 3 : CREATION DES RONDS DU CANVAS CENTRAL
    ##################################################


    #coordonnées pour les cercles
    cercle_y1=1/12*hauteur_canvas+5
    cercle_y2=2/12*hauteur_canvas-5

    #dessin des 4 cercles des 10 lignes
    for i in range(10):
        cercle_x1=1/5*largeur_canvas +50 #le 50 sert a faire des rond et non des oval, car les cases sont rectagulaire et non carré
        cercle_x2=2/5*largeur_canvas-50
        for j in range (4):
            rond=canvas.create_oval(cercle_x1,cercle_y1,cercle_x2,cercle_y2,width=3,fill=couleur_fond,outline=couleur_ecriture)
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
            rond_verification=canvas.create_oval(petit_cercle_x1,petit_cercle_y1,petit_cercle_x2,petit_cercle_y2,width=1,fill="white",outline=couleur_ecriture)
            petits_ronds[i].append(rond_verification)
            petit_cercle_x1+=1/2*(1/5*largeur_canvas)
            petit_cercle_x2+=1/2*(1/5*largeur_canvas)
        #on remet les X au bord du canvas et on descend les Y
        petit_cercle_x1=25                       
        petit_cercle_x2=1/2*(1/5*largeur_canvas)-25
        petit_cercle_y1+=1/2*(1/12*hauteur_canvas)
        petit_cercle_y2+=1/2*(1/12*hauteur_canvas)
        for j in range (2):#boucle pour les 2 ronds du bas du rectangle
            rond_verification=canvas.create_oval(petit_cercle_x1,petit_cercle_y1,petit_cercle_x2,petit_cercle_y2,width=1,fill="white",outline=couleur_ecriture)
            petits_ronds[i].append(rond_verification)
            petit_cercle_x1+=1/2*(1/5*largeur_canvas)
            petit_cercle_x2+=1/2*(1/5*largeur_canvas)
        petit_cercle_y1+=1/2*(1/12*hauteur_canvas)
        petit_cercle_y2+=1/2*(1/12*hauteur_canvas)
  


    #########################################################
    # PARTIE 4 : GESTION DU CHANGEMENT DE COULEUR DES RONDS
    #########################################################




    def colorer_rond(couleur,nb_essai):
        """
        Cette fonction prend en parametre la couleur du bouton qui a ete cliquer et
        change le couleur des rond correspondant
        """
        nonlocal index_rond
        nonlocal essai
        if 0<=nb_essai<=9:
            if couleur==couleur_fond and essai!=[]:
                essai.pop()
                index_rond-=1
                canvas.itemconfig(ronds[nb_essai][index_rond], fill=couleur_fond) #changement de la couleur du rond
                
            elif index_rond < len(ronds[nb_essai]):
                essai.append(couleur)
                canvas.itemconfig(ronds[nb_essai][index_rond], fill=couleur) #changement de la couleur du rond
                index_rond += 1





    ##############################################################
    # PARTIE 5 : GESTION DE LA VERIFICATION DES COULEUR RENTREES
    ##############################################################
    
    
    # Frame pour afficher les erreurs
    frame_erreur = tk.Frame(canvas_gauche,bg= "white")
    frame_erreur.pack(side="bottom", pady=10)


    def verifie_couleur_solo_test():
        nonlocal essai
        nonlocal index_rond
        nonlocal nb_essai
        essai=[]
        index_rond=0
        nb_essai-=1

    def verifie_couleur_duo_test():
        nonlocal essai
        nonlocal index_rond
        nonlocal nb_essai
        essai=[]
        index_rond=0
        nb_essai-=1



    #######################  VERIFICATION POUR LE JEU SOLO

    def verifie_couleur_solo():
        """
        Cette fonction permet de verifier apres l'appui du bouton valider, si les couleurs existent/sont à la bonne place/sont présentes
        et modifie la couleur des petits ronds.
        """
        nonlocal nb_essai
        nonlocal code_secret
        nonlocal essai
        nonlocal index_rond
        nonlocal petits_ronds
        # Si la ligne est pas complétée
        if len(essai) != 4:
            if erreur_label:
                erreur_label.destroy()
            erreur_label = tk.Label(frame_erreur, text="Remplissez 4 couleurs\navant de valider.", fg="red", font=("Arial", 15))
            erreur_label.pack()
            return  # On arrête tout si cest pas complet

        # Copie temporaire code secret pour suivre couleurs déjà vérifiées, éviter les doublons
        code_secret_temp = code_secret[:]
        petits_ronds_temp = []

        # couleurs bien placées
        for i in range(4):
            if essai[i] == code_secret_temp[i]:
                petits_ronds_temp.append("#229954")
                code_secret_temp[i] = None  # Marque cette couleur comme utilisée
            else:
                petits_ronds_temp.append(None)  # en gros ça ajoute dans la liste petits_ronds_temp un "None" pour dire que 
                #la couleu est pas mise en noir, mais qu'lle sera soit en gris soit en blanc, pour pas laisser de vide quoi

        # couleurs présentes mais mal placées
        for i in range(4):
            if petits_ronds_temp[i] is None:  # du cp si c'est pas noir (donc None)
                if essai[i] in code_secret_temp:  # Si la couleur est dans le code secret mais pas à la bonne place
                    petits_ronds_temp[i] = "#ffa600"
                    code_secret_temp[code_secret_temp.index(essai[i])] = None  # Marque la couleur comme utilisée, évite que le couleur
                    #soir comptée plusieures fois comle présente ms mal placée pdt la vérification
                else:  # Sinon la couleur est absente
                    petits_ronds_temp[i] = "#A93226"

        # Mélange les couleurs des petits ronds
        random.shuffle(petits_ronds_temp)

        # Applique les couleurs mélangées aux petits ronds
        for i in range(4):
            canvas.itemconfig(petits_ronds[nb_essai][i], fill=petits_ronds_temp[i])

        nb_essai -= 1
        essai = []
        index_rond = 0

    #######################  VERIFICATION POUR LE JEU DUO 

    def choisir_couleur_verif(couleur):
        nonlocal petits_ronds
        if verification_en_cours:
            for i in range(4):
                couleur_actuelle = canvas.itemcget(petits_ronds[nb_essai][i], "fill")
                if couleur_actuelle == "white":
                    canvas.itemconfig(petits_ronds[nb_essai][i], fill=couleur)
                    break

    
    def valider_essai_joueur1():
        """
        Fonction pour que le joueur 1 valide son essai
        """
        nonlocal verification_en_cours, erreur_label
        if len(essai) != 4:
            if erreur_label:
                erreur_label.destroy()
            erreur_label = tk.Label(frame_erreur, text="Remplissez 4 couleurs\navant de valider.", fg="red", font=("Arial", 15))
            erreur_label.pack()
            return
        verification_en_cours = True
        print("Joueur 1 a validé son essai :", essai)
        print("Joueur 2, choisis les couleurs de vérification.")

    
    def valider_verification_joueur2():
        """
        Fonction pour que le joueur 2 valide les couleurs
        """
        nonlocal nb_essai, index_rond, essai, verification_en_cours, erreur_label
        couleurs_utilisees = [canvas.itemcget(r, "fill") for r in petits_ronds[nb_essai]]
        if not all(c in couleurs_verif for c in couleurs_utilisees):
            if erreur_label:
                erreur_label.destroy()
            erreur_label = tk.Label(frame_erreur, text="Tous les petits ronds doivent\nêtre colorés par le joueur 2.", fg="red", font=("Arial", 15))
            erreur_label.pack()
            return
        print("Joueur 2 a validé :", couleurs_utilisees)
        nb_essai -= 1
        index_rond = 0
        essai = []
        verification_en_cours = False




    ####################################################
    # PARTIE 6 : AJOUT DES BOUTONS DANS LE CANVAS DROIT
    ####################################################


    # Ajout de boutons correspondant aux couleurs
    for couleur in couleurs:
        bouton = tk.Button(canvas_droit, text=couleur, bg=couleur, command=lambda c=couleur: colorer_rond(c, nb_essai),font=("Consolas",27),relief="groove",bd=5,fg="white", width=7, height=1)  
        bouton.pack(pady=10)
    
    if mode_de_jeu=="mode_solo":
        bouton_valider = tk.Button(canvas_droit, text="Valider", command=verifie_couleur_solo,font=("Consoloas",27),relief="groove",bd=5, width=7, height=1)  
    else:
        bouton_valider = tk.Button(canvas_droit, text="Valider", command=valider_essai_joueur1,font=("Consoloas",27),relief="groove",bd=5, width=7, height=1) 
        
        bouton = tk.Button(canvas_gauche, text="Est à la bonne\nplace", bg="#229954", command=lambda c="#229954": choisir_couleur_verif(c), font=("Consoloas", 20),relief="groove",bd=5)
        bouton.pack(pady=10)
        bouton = tk.Button(canvas_gauche, text="Est mal placé", bg="#ffa600", command=lambda c="#ffa600": choisir_couleur_verif(c), font=("Consoloas", 20),relief="groove",bd=5)
        bouton.pack(pady=10)
        bouton = tk.Button(canvas_gauche, text="N'existe pas", bg="#A93226", command=lambda c="#A93226": choisir_couleur_verif(c), font=("Consoloas", 20),relief="groove",bd=5)
        bouton.pack(pady=10)
        tk.Button(canvas_gauche, text="Valider \n la verification", command=valider_verification_joueur2, font=("Consoloas", 20), relief="groove",bd=5).pack(pady=20)
 
    bouton_valider.pack(pady=10)
    bouton_annuler = tk.Button(canvas_droit, text="Annuler", command=lambda c=couleur_fond: colorer_rond(c,nb_essai),font=("Consoloas",27),relief="groove",bd=5, width=7, height=1)  
    bouton_annuler.pack(pady=10)



    









####################################################################################################################################
#############    FENETRE CHOIX COULEUR DUO
####################################################################################################################################
  


def ouvrir_fenetre_choix_couleur(fenetre):
    """
    Cette fonction ouvre la fenêtre du mode Duo pour choisir un code couleur secret
    """
    print("je rentre dans le choix du code secret")
    fenetre_Duo = tk.Toplevel(fenetre)
    fenetre_Duo.title("Mode Deux Joueurs")
    fenetre_Duo.geometry("900x600")
    fenetre_Duo.configure(bg=couleur_fond)

    titre = tk.Label(fenetre_Duo, text="Mode Deux Joueurs", bg=couleur_fond, fg=couleur_boutons, font=("Segoe print", 53))
    titre.pack(pady=20)

    couleurs_disponibles = ["Rouge", "Bleu", "Vert", "Jaune", "Orange", "Violet"]
    code_secret = []

    def lancer_jeu(code_secret):
        """
        Fonction appelée lorsque le jeu commence
        """
        print("Le jeu commence avec le code :", code_secret)
        fenetre_Duo.destroy()
        ouvrir_jeu_solo(fenetre,code_secret)

    def ajouter_couleur(code_secret):
        """
        Ajoute une couleur au code secret
        """
        if len(code_secret) < 4:
            couleur_choisie = combo.get()
            if couleur_choisie:
                code_secret.append(couleur_choisie)
                liste_couleurs.config(text="Code secret : " + " - ".join(code_secret))

            if len(code_secret) == 4:
                bouton_ajouter.config(state="disabled")
                bouton_lancer.config(state="normal")  # Active le bouton de lancement
            

    label = tk.Label(fenetre_Duo, text="Le joueur doit choisir 4 couleurs\nqui formeront le code secret:", bg=couleur_fond,fg=couleur_ecriture, font=("Fixedsys", 30))
    label.pack(pady=10)

    combo = ttk.Combobox(fenetre_Duo, values=couleurs_disponibles, state="readonly")
    combo.pack(pady=5)

    bouton_ajouter = tk.Button(fenetre_Duo, text="Ajouter", command=lambda: ajouter_couleur(code_secret), font=("Fixedsys", 20), bg=couleur_boutons,fg=couleur_ecriture,relief="groove",bd=5)
    bouton_ajouter.pack(pady=10)

    # Bouton pour lancer le jeu (désactivé au départ)
    bouton_lancer = tk.Button(fenetre_Duo, text="Lancer le jeu", font=("Fixedsys", 20), bg=couleur_boutons, state="disabled", command=lambda: lancer_jeu(code_secret),fg=couleur_ecriture,relief="groove",bd=5)
    bouton_lancer.pack(pady=20)

    liste_couleurs = tk.Label(fenetre_Duo, text="Code secret : ", bg=couleur_fond, font=("Fixedsys", 23),fg=couleur_ecriture)
    liste_couleurs.pack(pady=10)


    




fenetre.mainloop()