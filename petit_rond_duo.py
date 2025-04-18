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
