# Fonction principale pour la calculatrice
def calculatrice():
    print("Bienvenue dans la calculatrice de base")
    print("Opérations disponibles :")
    print("1. Addition (+)")
    print("2. Soustraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Demander à l'utilisateur de choisir une opération
    choix = input("Choisissez une opération (1/2/3/4) : ")
    
    if choix not in ['1', '2', '3', '4']:
        print("Erreur : Choix invalide. Veuillez réessayer.")
        return
    
    # Demander les deux nombres
    try:
        num1 = float(input("Entrez le premier nombre : "))
        num2 = float(input("Entrez le deuxième nombre : "))
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
        return
    
    # Effectuer l'opération choisie
    if choix == '1':
        resultat = num1 + num2
        print(f"Le résultat de {num1} + {num2} est : {resultat}")
    elif choix == '2':
        resultat = num1 - num2
        print(f"Le résultat de {num1} - {num2} est : {resultat}")
    elif choix == '3':
        resultat = num1 * num2
        print(f"Le résultat de {num1} * {num2} est : {resultat}")
    elif choix == '4':
        if num2 == 0:
            print("Erreur : Division par zéro non autorisée.")
        else:
            resultat = num1 / num2
            print(f"Le résultat de {num1} / {num2} est : {resultat}")
    
# Appeler la fonction
calculatrice()

