# suppression
from menu_recherche import menu_recherche
import pandas as pd
from bson import ObjectId 


def menu_suppression(collection):
    indicateur_suppression = False
    print("1 : Pour supprimer un livre à l'aide de son identifiant unique")
    print("2 : Pour supprimer un livre en faisant une recherche dans la bibliothèque") 
    print("3 : Pour une suppression de plusieurs livres\n")
    choix_1 = input("Quelle type de suppresion voulez-vous faire ?\n")
    while not (choix_1 =="1" or choix_1 =="2" or choix_1 =="3") : 
        choix_1 = input("Je n'ai pas compris, veuillez ressaisir votre choix.\n")
        
    
    if choix_1 =="1":
        L=[]
        id = input("Veuillez indiquer l'identifiant unique de livre que vous voulez supprimer : ")
        document_trouve = collection.find({"_id" : id})
        L = list(document_trouve)

        while len(L)==0:
            id = input("L'identifiant que vous avez rentré ne correspond à aucun identifiant de livre. \nVeuillez saisir un autre identifiant : ")
            document_trouve = collection.find({"_id" : id})
            L= list(document_trouve)
            
        indicateur_suppression = True
        ligne = L[0]
        pd_dataframe = pd.DataFrame([ligne])[["_id", "title", "year", "authors", "type"]]
        
        
        
    elif choix_1 == "2":
        print("\n")
        print('-----------recherche du livre à supprimer-------------\n')
        
        reessai_recherche = True
        while reessai_recherche :
            sortie = menu_recherche(collection)
            if sortie.empty :
                print("1 : SI vous voulez refaire une recherche pour supprimer un ouvrage.")
                print("2 : Pour retourner au menu\n")
                choix_2 = input("Que voulez-vous faire ?\n")
                while not(choix_2 == "1" or choix_2 == "2"):
                    choix_2 = input("Votre saisi ne correspond a aucune des deux options. \n Veuillez ressaisir votre choix.\n")
                    
                if choix_2 == "2":
                    reessai_recherche = False
                    
                    
            else : 
                print("Voici les résultats de la recherche : \n")
                print(sortie[["_id", "title", "year", "authors", "type" ]])

            
                if sortie.shape[0] >1 :
                    numero_ligne = input("\nVeuillez saisir le numéro de ligne associée au livre que vous voulez supprimer \n")

                    while not(numero_ligne.isnumeric()) or int(numero_ligne) > sortie.shape[0] : 
                        numero_ligne = input("Votre saisie ne correspond à aucun numéro de ligne.\n Veuillez ressaisir un numéro de ligne ?\n")
                    
                else : 
                    numero_ligne = 0
                    
                ligne = sortie.loc[int(numero_ligne),:]
                pd_dataframe = ligne[["_id", "title", "year", "authors", "type"]]
                indicateur_suppression = True
                reessai_recherche = False
                
    if (choix_1 == "1"or choix_1 == "2") and indicateur_suppression : 
        print("\n Vous allez supprimer le livre suivant :\n ")
        print(pd_dataframe)    
        print("\n1 : Pour supprimer ce livre")
        print("2 : Pour retourner au menu de suppression de livre")
        print("3 : Pour retourner au menu de la bibliothèque\n")
        choix_2 = input("Quel est votre choix ?\n")
        
        while not(choix_2.isnumeric()) or int(choix_2)>3 :
            choix_2 = input("Votre réponse est incompatible avec les numéros d'option proposés.\n Veuillez ressaisir votre réponse.")
        
        if choix_2 == '1':
            collection.delete_one({"_id" : ligne['_id']})
            type = ligne["type"]
            if type == "Book":
                print(f"\nLe livre : '{ligne["title"]}' a bien été supprimé.")
            elif type == "Article":
                print(f"\nL' article : '{ligne["title"]}' a bien été supprimé.")
            else :
                f"\nLa thèse : '{ligne["title"]}' a bien été supprimée."
                
        elif choix_2 =='2':
            menu_suppression(collection)
            
    if choix_1 == "3":
        print('---------------- suppression multiple ---------------\n')
        print("1 : Pour supprimer tous les oeuvres écrite par un auteur")
        print("2 : Pour supprimer toutes les oeuvres datant d'une certaine année\n")
        
        choix_3 = input("Quel est votre choix ?\n")
        while not (choix_3 =="1" or choix_3 =="2") : 
            choix_3 = input("Je n'ai pas compris, veuillez ressaisir votre choix.\n")
        
        if choix_3 == "1":
            reiteration_auteur = True
            while reiteration_auteur :
                input_auteur = input("\nVeuillez saisir l'auteur dont vous voulez supprimer ses oeuvres de la bibliothèque :\n")
                
                recherche = collection.find({"authors": {"$in": [input_auteur]}})
                list_recherche = list(recherche)
                if len(list_recherche) == 0 :
                    print("Cet auteur n'a pas écrit d'oeuvres présent dans la bibliothèque.\n")
                    print("Voulez-vous en saisir un nouveau ?\n")
                    print("1 : Pour saisir un nouvel auteur")
                    print("2 : pour retourner au menu\n")
                    choix_5 = input("\nQuel est votre choix ?\n")
                    while not (choix_5 =="1" or choix_5 =="2") : 
                        choix_5 = input("Je n'ai pas compris, veuillez ressaisir votre choix.\n")
                    if choix_5 =="2":
                        reiteration_auteur = False
                
                else : 
                    reiteration_auteur = False
                    data = pd.DataFrame(list_recherche)
                    print("\n Vous allez supprimer les oeuvres suivantes de la bilbiothèque :\n")
                    print(data)
                    
                    print("\nEtes-vous sur de vouloir les supprimer ? \n")
                    print("1 : Pour supprimer ces oeuvres")
                    print("2 : Pour retourner au menu")
                    
                    choix_4 = input("\nQuel est votre choix ?\n")
                    while not (choix_4 =="1" or choix_4 =="2") : 
                        choix_4 = input("Je n'ai pas compris, veuillez ressaisir votre choix.\n")
                    
                    if choix_4 == "1":
                        collection.delete_many({"authors": {"$in": [input_auteur]}})
                        print(f"\nLes oeuvres écrites par {input_auteur} ont bien été supprimées.\n")
                    
                    
            
            
        if choix_3 == "2" :
            
            reiteration_annee = True
            while reiteration_annee :
                input_annee = input("\nVeuillez saisir l'année dont vous voulez supprimer les oeuvres :\n")
                while not(input_annee.isnumeric() and  int(input_annee)<2025):
                    input_annee = input("\nVous n'avez pas saisi une année. Veuillez ressaisir une année.\n")
                    
                recherche = collection.find({"year" : int(input_annee)})
                list_recherche = list(recherche)
                if len(list_recherche) == 0 :
                    print(f"Aucune oeuvre n'est parue durant l'année : {int(input_annee)}\n")
                    print("Voulez-vous en saisir une à nouveau ?\n")
                    print("1 : Pour saisir une nouvelle année")
                    print("2 : pour retourner au menu\n")
                    choix_7 = input("\nQuel est votre choix ?\n")
                    while not (choix_7 =="1" or choix_7 =="2") : 
                        choix_7 = input("Je n'ai pas compris, veuillez ressaisir votre choix.\n")
                    if choix_7 =="2":
                        reiteration_annee = False
                
                else : 
                    reiteration_annee = False
                    data = pd.DataFrame(list_recherche)
                    print("\n Vous allez supprimer les oeuvres suivantes de la bilbiothèque :\n")
                    print(data)
                    
                    print("\nEtes-vous sur de vouloir les supprimer ? \n")
                    print("1 : Pour supprimer ces oeuvres")
                    print("2 : Pour retourner au menu")
                    
                    choix_8 = input("\nQuel est votre choix ?\n")
                    while not (choix_8 =="1" or choix_8 =="2") : 
                        choix_8 = input("Je n'ai pas compris, veuillez ressaisir votre choix.\n")
                    
                    if choix_8 == "1":
                        collection.delete_many({"year" : int(input_annee)})
                        print(f"\nLes oeuvres parues en {int(input_annee)} ont bien été supprimées.\n")
                    
                    
                
            
        
                
            
        

