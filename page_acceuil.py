import tkinter as tk
import fenetre_jeu_solo
import fenetre_jeu_duo



####TACHES A FAIRE############
#gerer l'aspect visuel
#boutton reles du jeu
#bouton retour pour le jeu
#fonction verifier duo et solo
#fonction aide et sauvegarde








##################################################################################################
# PARTIE 1 : GESTION DE LA PAGE D'ACCUEIL
##################################################################################################

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



bouton_joueur_solo=tk.Button(cadre,text="Jouer en solo",command=lambda: fenetre_jeu_solo.ouvrir_jeu_solo(fenetre),font=("Arial",20),bg=couleur_boutons,fg=couleur_fond)
bouton_joueur_solo.pack(side="left",padx=100)

bouton_joueur_duo = tk.Button(cadre, text="Jouer en duo", command=lambda: fenetre_jeu_duo.ouvrir_jeu_duo(fenetre), font=("Arial", 20), bg=couleur_boutons, fg=couleur_fond)
bouton_joueur_duo.pack(side="left", padx=50)

bouton_fermeture = tk.Button(fenetre, text="Fermer", command=fermer_fenetre, font=("Arial", 20), bg="red", fg="white")
bouton_fermeture.pack()






