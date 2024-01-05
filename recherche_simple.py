# recherche simple
import pandas as pd

def recherche_auteur( collection):
    reiteration_recherche = True
    while reiteration_recherche :
        auteur = input("\nPouvez-vous m'indiquer l'auteur dont vous souhaitez connaitre ses ouvrages ?")
        results = collection.find({"authors" :  {"$in": [auteur]}})
        L = list(results)
        
        if len(L) == 0:
            print("\nL'auteur que vous avez indiqué n'a écrit aucun ouvrage dont nous disposons dans la bibliothèque.\n")
            print("1 : Pour ressaisir un nom d'auteur")
            print("2 : Pour retourner au menu\n")
            choix_0 = input("Que voulez vous faire ?")
            while not (choix_0 =="1" or choix_0 =="2") : 
                choix_0 = input("Je n'ai pas compris, veuillez ressaisir votre choix.")
                
            if choix_0 =="2":
                reiteration_recherche = False
        
            
        else : 
            reiteration_recherche = False
    
    data = pd.DataFrame(L)
        
    return(data)
    
def recherche_title(collection):
    reiteration_recherche = True
    
    while reiteration_recherche :
        title = input("Pouvez-vous m'indiquer le titre du livre que vous recherchez ?\n")
        results = collection.find({"title" : title}) 
        L = list(results)
        if len(L)  == 0:
            print("\nIl n'y a aucun livre qui correspond au nom que vous avez rempli.\n")
            print("1 : Pour ressaisir un titre de livre")
            print("2 : Pour retourner au menu\n")
            choix_0 = input("Que voulez vous faire ?\n")
            while not (choix_0 =="1" or choix_0 =="2") : 
                choix_0 = input("\nJe n'ai pas compris, veuillez ressaisir votre choix.\n")
                
            if choix_0 =="2":
                reiteration_recherche = False
        else : 
            reiteration_recherche = False
    
    data = pd.DataFrame(L)
    
    return(data)
    
        

def recherche_annee(collection):
    reiteration_recherche = True
    
    while reiteration_recherche :
        
        annee = input("\nPouvez-vous m'indiquer l'année qui vous intéresse ?\n")
        if len(annee)<5 and annee.isnumeric() and int(annee)<2025  :
            
            results = collection.find({"year" : int(annee)}) 
            L = list(results)
            if len(L)  == 0:
                print(f"\nIl n'y a aucun livre qui est paru en {annee} dans la bilbiothèque.\n")
                print("1 : Pour ressaisir une année de parution")
                print("2 : Pour retourner au menu\n")
                choix_0 = input("Que voulez vous faire ?\n")
                while not (choix_0 =="1" or choix_0 =="2") : 
                    choix_0 = input("\nJe n'ai pas compris, veuillez ressaisir votre choix.\n")
                    
                if choix_0 =="2":
                    reiteration_recherche = False
            else :
                reiteration_recherche = False
        else :
            print("Vous n'avez pas saisi une année.")
    
    data = pd.DataFrame(L)
    
    return(data)


def recherche_simple(collection):
        print('------------------ Recherche simple -------------------\n')
        print("1 Pour rechercher les ouvrages d'un auteur")
        print("2 Pour rechercher un livre à partir de son titre") 
        print("3 Pour rechercher les livres suivant leur année de parution")
        choix_1 = input("\nQuelle type de recherche voulez-vous faire ?\n")
        while not (choix_1 =="1" or choix_1 =="2" or choix_1 =="3") : 
            choix_1 = input("Je n'ai pas compris, veuillez ressaisir votre choix.\n")
        
        
        
        if choix_1 =="1":
            sortie = recherche_auteur(collection)
            return(sortie)
            
        elif choix_1 == "2":
            sortie = recherche_title(collection)
            return(sortie)
        
        elif choix_1 == "3":
            sortie = recherche_annee(collection)
            return(sortie)