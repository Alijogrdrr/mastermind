
import tkinter as tk

# Fonction appelée qd on clique sur "Recommencer"
def recommencer():
    """renvoie sur la première fenêtre pour recommencer la partie"""
    fenetrevictoire.mainloop()


# Fonction appelée qd on clique sur "Arrêter de jouer"
def stopjeu():
        print("Arrêt du jeu")
        fenetrevictoire.quit()

fenetrevictoire = tk.Tk()
fenetrevictoire.title("C'est gagné !")
fenetrevictoire.geometry("400x300")
fenetrevictoire.config(bg="pink")

labelvictoire = tk.Label(fenetrevictoire, text="Bravo tu as gagné !", font = ("Tmes New Roman", "60"), bg="pink" )
labelvictoire.pack(pady=50)      #pour laisser un peu d'espace autour du texte

buttonrecommencer = tk.Button(fenetrevictoire, text= "Cliques ici pour recommencer", font = ("Impact","30"), command = recommencer)
buttonrecommencer.pack(side="left", padx=50)     #pr laisser de l'espace autour du bouton

buttonstop = tk.Button(fenetrevictoire, text="Arrêter de jouer", font=("Impact", "30"), command=stopjeu)
buttonstop.pack(side="right", padx=50)        


fenetrevictoire.mainloop() #lancement boucle principale