import tkinter as tk
import fenetre_jeu_solo
import fenetre_choix_couleurs





####################################################
# PARTIE 1 : GESTION DE LA PAGE D'ACCUEIL
####################################################

#Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.update()
fenetre.state("zoomed")  # Ouvre en plein écran
fenetre.title("Mastermind")
couleur_fond = "pink"
couleur_boutons = "white"
fenetre.configure(bg=couleur_fond)

#Création du titre de la page
titre = tk.Label(fenetre, text="Mastermind", font=("Impact", 50), fg="black", bg="pink")
titre.pack(pady=50)

#Ajout d'une bordure lumineuse
titre.config(highlightbackground="black", highlightthickness=5)

#Création des boutons dans un cadre
cadre = tk.Frame(fenetre, bg=couleur_fond)
cadre.pack(expand=True)

def fermer_fenetre():
    """
    Cette foncton permet de fermer la fenetre d'acceuil
    """
    fenetre.destroy()




####################################################
# PARTIE 2 : GESTION DE L'INSCRIPTION
####################################################

def ouvrir_fenetre_inscription():

    #Ouvre la fenêtre d'inscription,Cette fonction est associé au bouton_incription 
    for widget in fenetre.winfo_children():
        widget.destroy()
#changement du fond
    couleur_fond = "pink"
    fenetre.configure(bg=couleur_fond)

#creation du titre
    titre = tk.Label(fenetre, text="Page d'inscription", bg=couleur_fond, fg="black", font=("Poppins", 50))
    titre.pack()

#creation du champs d'entree
    champs_pseudo = tk.Entry(fenetre)
    champs_pseudo.pack()
    champs_mdp = tk.Entry(fenetre, show="*")  # Cachera le mot de passe
    champs_mdp.pack()

#creation du champs d'entree
    def enregistrer():
        pseudo = champs_pseudo.get()
        mdp = champs_mdp.get()
        if pseudo and mdp:
            with open('profils.txt', 'a', encoding='utf-8') as fichier:
                fichier.write(f'\n{pseudo};{mdp}')
            retour_accueil()

    bouton_valider = tk.Button(fenetre, text="Valider", font=("Arial", 15), bg="black", fg="white", command=enregistrer)
    bouton_valider.pack()

    bouton_retour = tk.Button(fenetre, text="Retour", font=("Arial", 15), bg="red", fg="white", command=retour_accueil)
    bouton_retour.pack(pady=10)




####################################################
# PARTIE 3 : GESTION DE LA CONNEXION
####################################################

def ouvrir_fenetre_connexion():

    #Cette fonction est associé au bouton_connexion et permet l'ouverture de la page de connexion quand l'utilisateur clic sur ce bouton
    for widget in fenetre.winfo_children():
        widget.destroy()
#changement du fond
    couleur_fond = "pink"
    fenetre.configure(bg=couleur_fond)

    #creation du titre
    titre = tk.Label(fenetre, text="Page de connexion", bg=couleur_fond, fg="black", font=("Arial", 50))
    titre.pack()

    champs_pseudo = tk.Entry(fenetre)
    champs_pseudo.pack()
    champs_mdp = tk.Entry(fenetre, show="*")
    champs_mdp.pack()

    #bouton valider
    def verifier():
        pseudo = champs_pseudo.get()
        mdp = champs_mdp.get()
        with open('profils.txt', 'r', encoding='utf-8') as fichier:
            utilisateurs = fichier.read().splitlines()
            if f"{pseudo};{mdp}" in utilisateurs:
                retour_accueil()
            else:
                erreur = tk.Label(fenetre, text="Compte invalide. Réessayez ou inscrivez-vous.", bg=couleur_fond, fg="red", font=("Arial", 16))
                erreur.pack()

    bouton_valider = tk.Button(fenetre, text="Valider", font=("Arial", 15), bg="#141769", fg="white", command=verifier)
    bouton_valider.pack()

    bouton_retour = tk.Button(fenetre, text="Retour", font=("Arial", 15), bg="red", fg="white", command=retour_accueil)
    bouton_retour.pack(pady=10)



####################################################
# AJOUT DES BOUTONS PRINCIPAUX
####################################################

def retour_accueil():
    # Revenir à l'écran d'accueil
    for widget in fenetre.winfo_children():
        widget.destroy()
    
    #titre_page.pack(side="top")
    cadre.pack(expand=True)
    bouton_fermeture.pack()

bouton_inscription = tk.Button(cadre, text="Inscription", command=ouvrir_fenetre_inscription, font=("Arial", 20), bg=couleur_boutons, fg=couleur_fond)
bouton_inscription.pack(side="left", padx=50)

bouton_connexion = tk.Button(cadre, text="Connexion", command=ouvrir_fenetre_connexion, font=("Arial", 20), bg=couleur_boutons, fg=couleur_fond)
bouton_connexion.pack(side="left", padx=50)

bouton_joueur_solo=tk.Button(cadre,text="jouer en solo",command=lambda: fenetre_jeu_solo.ouvrir_jeu_solo(fenetre),font=("Arial",20),bg=couleur_boutons,fg=couleur_fond)
bouton_joueur_solo.pack(side="left",padx=100)

bouton_joueur_duo = tk.Button(cadre, text="Jouer en duo", command=lambda: fenetre_choix_couleurs.ouvrir_fenetre_Duo(fenetre), font=("Arial", 20), bg=couleur_boutons, fg=couleur_fond)
bouton_joueur_duo.pack(side="left", padx=50)

bouton_fermeture = tk.Button(fenetre, text="Fermer", command=fermer_fenetre, font=("Arial", 20), bg="red", fg="white")
bouton_fermeture.pack()





####TACHES A FAIRE############
#boutton retour sur les page inscription et connexion
#boutton qui renvoie a la page d'inscription quand la connexion n'a pas reussi (si c'est possible)
#gerer l'aspect visuel
#boutton reles du jeu
########################POUR LES PROBLEME DE FICHIER RELIE ENTRE EUX #########################
#import sys
#sys.path.append('chemin de vos fichiers')












fenetre.mainloop()