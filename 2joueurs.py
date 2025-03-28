def couleur_code_secret_2():
    """
    Cette fonction sert a faire choisir un code couleur qui sera le code couleur que l'utilistaeur devrait trouver
    """
    global couleurs
    global code_secret
    code_secret.append(random.choice(couleurs))
    print("Les couleurs a deviner dans cet ordre sont:", code_secret)

couleur_code_secret_2()