def palandrom (chaine) :
    chaine = chaine.replace(" ","").lower()
    return chaine == chaine[::-1]
clientText = input("saire un text et verifier si il est palandrome : ")
print (palandrom(clientText))
