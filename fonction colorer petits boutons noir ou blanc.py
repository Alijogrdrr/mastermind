
def colorer_petits_ronds(code_secret,couleur):
    if couleur in code_secret:
        for elem in code_secret:
            if elem == couleur:
                rond_verification = canvas.config(fill = "black")
            else:
                rond_verification = canvas.config(fill = "white")
    else:
        rond_verification = canvas.config(fill = "grey")

        







if verifie_couleur == True:
    colorer_petits_ronds()