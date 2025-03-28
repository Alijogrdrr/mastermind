def couleur_code_secret_2():
    global couleur
    """
    Permet à l'utilisateur de choisir un code couleur qu'il devra deviner plus tard.
    """
    code_secret = []

    print("Couleurs disponibles :", ", ".join(couleurs))
    while True:
        couleur = input("Choisissez une couleur (ou tapez 'fin' pour terminer) : ").lower()
        if couleur == "fin":
            break
        elif couleur in couleurs:
            code_secret.append(couleur)
        else:
            print("Couleur invalide, veuillez choisir parmi :", ", ".join(couleurs))
    
    print("Les couleurs à deviner dans cet ordre sont :", code_secret)
    return code_secret

# Exécution de la fonction
code_secret = couleur_code_secret_2()
