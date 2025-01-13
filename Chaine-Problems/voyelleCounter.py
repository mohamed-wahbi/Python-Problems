def voyellesCounter () :
    print("Tu as une phrase et tu veux compter les voyelles existants ?")
    choix = input("si ui entre 1 si non 2 : ")
    if choix == "1" :
        text = input("entrer votre text : ")
        voyelleCounter = 0
        for lettre in text :
            if lettre in ["a","e","i","o","u","y"]:
                voyelleCounter = voyelleCounter + 1
        print(f"le nombre des voyelle existants dans votre phrase = {voyelleCounter} , MERCI *_*")
    else :
        print("vous etes les bien venue .")

voyellesCounter()