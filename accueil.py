
    





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