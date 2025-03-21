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


fenetre = tk.Tk()
fenetre.state("zoomed")#permet d'ouvrire la page directement en grand ecran
fenetre.title("Page d'acceuil")
couleur_fond="#141769"
couleur_boutons="white"
fenetre.configure(bg=couleur_fond)


#céation titre de la page
titre_page=tk.Label(fenetre,text="Bienvenue sur le\nMastermind !",bg=couleur_fond,fg="white",font=("Impact",60))
titre_page.pack(side="top") #sa place dans la fenetre



#creation des boutons

cadre=tk.Frame(fenetre,bg=couleur_fond)#cadre où sont les 2 boutons (inscription et connexion)
cadre.pack(expand=True)


def fermer_fenetre():
    """
    Cette fonction est associé au bouton_fermeture 
    et permet la fermeture de la page quand l'utilisateur clic sur ce bouton
    """
    fenetre.destroy()#permet de fermer la fenetre
    return fenetre
    
def ouvrir_jeu_solo():
    print("hey")
    return bouton_joueur_solo


def ouvrir_fenetre_jeu_duo():
    print("hey")
    return bouton_joueur_duo



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