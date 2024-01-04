# recherche simple
import pandas as pd

def recherche_auteur( collection):
    L=[]
    while len(L) == 0 :
        
        auteur = input("Pouvez-vous m'indiquer l'auteur dont vous souhaitez connaitre ses ouvrages ?")
        for elem in collection.find() : 
            authors = elem['authors']
            if auteur in authors:
                L.append(elem)
        if len(L) == 0:
            print("\n")
            print("L'auteur que vous avez indiqué n'a écrit aucun livre dont nous disposons dans la bibliothèque.")
            print("\n")
    
    data = pd.DataFrame(L)
    
    return(data)
    
def recherche_title(collection):
    L=[]
    while len(L) == 0 :
        
        
        title = input("Pouvez-vous m'indiquer le nom du livre que vous recherchez ?")
        for elem in collection.find({"title" : title}) : 
                L.append(elem)
        if len(L)  == 0:
            print("Il n'y a aucun livre qui correspond au nom que vous avez rempli.")
    
    data = pd.DataFrame(L)
    
    return(data)
    
        

def recherche_annee(collection):
    L=[]
    while len(L) == 0 :
        
        
        annee = input("Pouvez-vous m'indiquer l'année qui vous intéresse ?\n")
        if len(annee)<5 and annee.isnumeric() and int(annee)<2025  :
            
            for elem in collection.find({"year" : int(annee)}) : 
                    L.append(elem)
            if len(L)  == 0:
                print(f"Il n'y a aucun livre qui est paru en {annee} dans la bilbiothèque.")
        else :
            print("Vous n'avez pas saisi une année.")
    
    data = pd.DataFrame(L)
    
    return(data)


def recherche_simple(collection):
        print('---------------------------------------------------')
        print("1 Pour rechercher les ouvrages d'un auteur")
        print("2 Pour rechercher un livre à partir de son titre") 
        print("3 Pour rechercher les livres suivant leur année de parution")
        choix_1 = input("Quelle type de recherche voulez-vous faire ?")
        while not (choix_1 =="1" or choix_1 =="2" or choix_1 =="3") : 
            choix_1 = input("Je n'ai pas compris, veuillez ressaisir votre choix.")
        
        
        
        if choix_1 =="1":
            sortie = recherche_auteur(collection)
            return(sortie)
            
        elif choix_1 == "2":
            sortie = recherche_title(collection)
            return(sortie)
        
        elif choix_1 == "3":
            sortie = recherche_annee(collection)
            return(sortie)