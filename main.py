#main
from menu_utilisateur import menu_utilisateur
from pymongo import MongoClient
import pprint
from menu_recherche import menu_recherche
from ajout import ajout_livre
from suppression import menu_suppression
from tabulate import tabulate
import pandas as pd


while True:
    client = MongoClient("localhost", 27017)  
    db = client['test']
    collection = db["books"]
    pd.set_option('display.max_rows', None) 
    pd.set_option('display.width', None)
    print("\n")
    menu_utilisateur()
    
    choix = input("\nQue voulez-vous faire ?\n")
    
    if choix =="1": #cas de la recherche
        print("\n")
        print("---------------- recherche d'oeuvre ----------------")
        recherche = menu_recherche(collection)
        if not(recherche.empty) :
            print("Voici les résultats de la recherche : \n")
            print(recherche[["_id", "title", "year", "authors", "type" ]])
            
    elif choix == "2": # cas de l'ajout
        print("\n")
        print("---------------- ajout d'oeuvre --------------------\n")
        ajout_livre(collection)
        
    elif choix == "3": # cas de la suppression
        print("\n")
        print("------------- suppression d'oeuvre -----------------\n")
        menu_suppression(collection)
        
    elif choix == "4": # pour fermer l'application
        break
    else:
        print("Je n'ai pas compris, veuillez ressaisir votre choix.")
    
    