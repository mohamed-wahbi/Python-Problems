def nbrPaire() :
    try:
        nbr = int(input("saisire un numbre = "))
    except ValueError:
        print("valeur incorracte !")
        return
    for i in range(nbr):
        if (i+1) % 2 == 0 :
            print(f"{i+1} est un nombre paire .")
        else : 
            print(f"{i+1} est un nombre impaire !")
            
nbrPaire()