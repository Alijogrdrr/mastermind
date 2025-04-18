 def enregistrer_la_partie():
        pseudo_joueur=champs_pseudo.get()
        mdp_joueur=champs_mdp.get()
        profil_joueur=[pseudo_joueur,mdp_joueur]
        with open('profils.txt','a',encoding='utf-8') as fichier:
        
        fichier.write('\n'+profil_joueur)
        fichier.close()
        print(joueur)
        