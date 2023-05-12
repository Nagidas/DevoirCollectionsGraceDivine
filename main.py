if __name__ == '__main__':
    # Question I
    print("Q1.")
    # Liste de 10 elements de type chaîne de caractères
    List = ["papa", "maman", "fils", "fille", "oncle", "tante", "neveu", "niece", "parent", "enfant"]
    
    # 1- Affichage des elements de la liste
    print("1) Affichage des elements de la liste")
    print(List)
    print("\n")
    
    # 2- Changement du contenu de l'element numero 5
    print("2) Changement du contenu de l'element numero 5")
    List[4] = "soeur"
    print(List)
    
    #3- Creation d' une nouvelle liste
    NList = []
    # remplissage avec les elements de la liste precedente contenant la lettre "a"
    for element in List:
        if "a" in element:
            NList.append(element)
    print("\n3) les elements de la liste contenant la letter a:")
    print(NList)
