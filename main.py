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
    
    #5) Ajouter un element a l'index numero 3
    print("\n5) Ajouter un element a l'index numero 3")
    # On ne peut pas modifier une tuple directement, il faut creer une nouvelle tuple
    Tup = Tup[:3] + (96,) + Tup[3:]
    print(Tup)

#6) Affichage de la nouvelle tuple
    print("\n6) Affichage de la nouvelle tuple")
    print(Tup)
    print("\n\n")
  
    # Question 3
    print("Q3")
    # Creation d'un set de 10 elements de type chaine de caractères
    Set_ch = {"Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre"}

    #1 Affichage du set
    print("\n1) Affichage du set")
    print(Set_ch)
    
    #2 Ajouter un element
    print("\n2) Ajout d'un element dans le set")
    Set_ch.add("Novembre")
    print(Set_ch)

    #3 Suppression d'un element
    print("\n3) Suppression d'un element dans le set")
    Set_ch.remove("Juin")
    print(Set_ch)
    
    #4 Suppression du set
    print("\n4) Suppression du set")
    del Set_ch
    print("\n\n")
    
     # Question 4
    print("Q4")
    # Dictionnaire de 10 elements de type chaîne de caractères
    Dic_ch = {"1": "un", "2": "deux", "3": "trois", "4": "quatre", "5": "cinq", "6": "six", "7": "sept", "8": "huit", "9": "neuf", "10": "dix"}

    #1 Afficher le dictionnaire
    print("\n1) Affichage du dictionnaire")
    print(Dic_ch)
    
    #2 Afficher seulement les cles
    print("\n2) Affichage des cles seulement")
    print(Dic_ch.keys())
    
    #3 Afficher seulement les valeurs
    print("\n3) Affichage des valeurs seulement")
    print(Dic_ch.values())
    
    #4 Afficher les cles et les valeurs sous le format : Cle : Valeur
    print("\n4) Affichage des cles et des valeurs sous le format: Cle : Valeur")
    for cle, valeur in Dic_ch.items():
        print(f"{cle} : {valeur}")

    #5 Suppression de l'element a la cle numero 2
    print("\n5) Suppression de l'element a la cle numero 2")
    Dic_ch.pop("2")
    print(Dic_ch)
    
    #6 Affichage de l'element de la cle numero  5
    print("\n6) Affichage de l'element de la cle numero 5")
    print(Dic_ch["5"])

    #7 Ajouter un nouvel element
    print("\n7) Ajout d'un nouvel element")
    Dic_ch["11"] = "onze"
    print(Dic_ch)
    
