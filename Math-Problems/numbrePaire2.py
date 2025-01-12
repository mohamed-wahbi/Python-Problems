def numbrePaireInInterval () :
    try : 
        intervalStartValue = int (input("saisire le debue de l'intervale = "))
        intervalEndValue = int (input("saisire la fin de l'intervale = "))
    except ValueError:
        print('tu a entre un caractere autre que numbre !')
        return
    
    while intervalStartValue < intervalEndValue + 1  :
        
        if intervalStartValue % 2 == 0 :
            print (f"le nombre tester {intervalStartValue} est paire .")
        else :
            print (f"le nombre tester {intervalStartValue} est impaire !")

        intervalStartValue = intervalStartValue + 1 
        

numbrePaireInInterval()