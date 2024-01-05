# suppression
from menu_recherche import menu_recherche
import pandas as pd
from bson import ObjectId 


def menu_suppression(collection):
    indicateur_suppression = False
    print("1 : Pour supprimer un livre à l'aide de son identifiant unique")
    print("2 : Pour supprimer un livre en faisant une recherche dans la bibliothèque\n") 
    choix_1 = input("Quelle type de suppresion voulez-vous faire ?\n")
    
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
                print("Il n'y a aucun ouvrage qui correspond à votre recherche.\n")
                print("1 : Pour refaire une recherche")
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
    if indicateur_suppression : 
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
                f"\nLa thèse : '{ligne["title"]}' a bien été supprimé."
                
        elif choix_2 =='2':
            menu_suppression(collection)
                
            
        

