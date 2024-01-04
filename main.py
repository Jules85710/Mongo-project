#main
from menu_utilisateur import menu_utilisateur
from pymongo import MongoClient
import pprint
from menu_recherche import menu_recherche
from ajout import ajout_livre
from suppression import menu_suppression
from tabulate import tabulate

while True:
    client = MongoClient("localhost", 27017)  
    db = client['test']
    collection = db["books"]
    print("\n")
    menu_utilisateur()
    
    choix = input("\nQue voulez-vous faire ?\n")
    
    if choix =="1":
        print("\n")
        print("---------------- recherche de livre ----------------\n")
        recherche = menu_recherche(collection)
        if recherche.empty :
            print("Il n'y a aucun ouvrage qui correspond à votre recherche.\n")
        else : 
            print("Voici les résultats de la recherche : \n")
            print(recherche[["_id", "title", "year", "authors", "type" ]])
    elif choix == "2":
        print("\n")
        print("---------------- ajout de livre --------------------\n")
        ajout_livre(collection)
        
    elif choix == "3":
        print("\n")
        print("------------- suppression de livre -----------------\n")
        menu_suppression(collection)
    elif choix == "4":
        break
    else:
        print("Je n'ai pas compris, veuillez ressaisir votre choix.")
    
    