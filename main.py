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
    
    #4 Ajout d'un element a la fin de la liste
    print("\n4) Ajout d'un element a la fin de la liste")
    List.append("frere")
    print(List)

   #5 Ajout d'un element a l'index numero 2
    print("\n5) Ajout d'un element a l'index numero 2")
    List.insert(2, "jumeaux")
    print(List)
 
    #6 Suppression de l'element numero 3
    print("\n6) Suppression de l'element numero 3")
    List.remove("fils")
    print(List)
    
    #7. Suppression l'element a l'index numero 2
    print("\n7) Suppression de l'element a l'index numero 2")
    del List[2]
    print(List)

    #8 Ordonner la liste
    print("\n8) Ordonnancement de la liste")
    List.sort()
    print(List)
    
    #9 Afficher la liste au sens inverse
    print("\n9) Affichage dans le sens inverse")
    List.reverse()
    print(List)

    #10 Vider la liste
    print("\n10) Vidange de la liste")
    List.clear()
    print(List)
    
    #11 Suppression de la liste
    del List
    print("\n\n")

    # Question 2
    print("Q2")
    # Tuple de 10 elements de type entier
    Tup = (23,52,14,78,69,5,14,6,44,9)
    
    # Affichage des elements de la tuple Tup
    print("\nAffichage des elements de la tuple")
    print(Tup)
    
    #1) Affichage du nombre de fois que valeur 3 apparait dans la tuple Tup
    print("\n1) Affichage du nombre de fois que valeur 3 apparait dans la tuple")
    print(Tup.count(3))

    #2) Affichage du contenu de l'element numero 5
    print("\n2) Affichage du contenu de l'element numero 5")
    print(Tup[4])
    
    #3) Ordonnancement de la tuple
    print("\n3) Ordonnancement de la tuple")
    Tup = tuple(sorted(Tup))
    print(Tup)
    
    #4) Ajout d' un element a la fin de la tuple
    print("\n4) Ajout d' un element a la fin de la tuple")
    # On ne peut pas modifier une tuple directement, il faut d'abord convertir la tuple en liste
    liste = list(Tup)
    # Ajouter un element a la fin de la liste
    liste.append(20)
    # Reconvertir la liste en tuple
    Tup = tuple(liste)
    # Affichage du nouveau tuple 
    print(Tup)
    
