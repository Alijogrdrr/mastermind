import tkinter as tk
# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("mastermind")
fenetre.state("zoomed")  # Ouvre la fenêtre en plein écran, parce que sinon c'est pas la bonne taille a chaque fois
# Configuration des colonnes 

fenetre.grid_columnconfigure(0, weight=1, minsize=100)  # ici (nom de a colone 0 1 ou 2, weight c'est la taille 1=petit 5=grand, minsize= taille min )

fenetre.grid_columnconfigure(1, weight=8, minsize=300)  # grid_columnconfigure C'est une fonction de Tkinter qui permet de configurer les colonnes d'une grille (grid).
 
fenetre.grid_columnconfigure(2, weight=1, minsize=100)
 
# Configuration de la ligne
fenetre.grid_rowconfigure(0, weight=1, minsize=200) 

#ici on met 0 parce qu'il y a qu'une seule ligne, 1 parce qu'on a pas besoin qu'elle soit plus grande qu'une aure ligne
 
# Création des carrés collés les uns aux autres
canvas_gauche = tk.Canvas(fenetre, background="black")
canvas_gauche.grid(row=0, column=0, rowspan=2,sticky="nsew" )  
 

#row=0 : place le widget dans la première ligne.
#column=0 : place le widget dans la première colonne.
#rowspan=2 : fait occuper au widget deux lignes.
#sticky="nsew" : fait en sorte que le rectangle s'étende dans toutes les directions.
 
canvas_central = tk.Canvas(fenetre, background="purple")
canvas_central.grid(row=0, column=1,rowspan=2, sticky="nsew")
canvas_droit = tk.Canvas(fenetre, background="black")
canvas_droit.grid(row=0, column=2, rowspan=2, sticky="nsew") 
for i in range (0,11):
 

    canvas_central.create_rectangle(470,42+i*60,110,8+i*60,outline="black")
 

for i in range (0,11):
 

    for j in range(0,4):
 

        canvas_central.create_oval(122+100*j,39+i*60,152+100*j,11+i*60)
 


 

# Affichage de la fenêtre
 

fenetre.mainloop()