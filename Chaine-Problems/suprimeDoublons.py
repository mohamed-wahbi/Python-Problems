def supprimer_doublons():
    lettre = input("crée votre mot : ")
    chaineWithoutLettre = ""

    for alpha in lettre :
        if alpha not in chaineWithoutLettre :
            chaineWithoutLettre += alpha
    print(f"chaine sans double : {chaineWithoutLettre}")

supprimer_doublons()
