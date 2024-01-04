#Recherche de livres
import pandas as pd
from tabulate import tabulate
from recherche_simple import recherche_simple
from recherche_avancée import recherche_avancee



def menu_recherche(collection):
    print("\n1 : Pour effectuer une recherche simple")
    print("2 : Pour effectuer une recherche avancée (avec des filtres)") 
    print("3 : Retour\n")
    choix_0 = input("Quelle type de recherche voulez-vous faire ?\n")
    while not (choix_0 =="1" or choix_0 =="2" or choix_0 == "3") : 
        choix_0 = input("Je n'ai pas compris, veuillez ressaisir votre choix.\n")
    
    if choix_0 =="1":
        #recherche simple
        return(recherche_simple(collection))
    
    elif choix_0 =="2":
        # recherche avancée
        return(recherche_avancee(collection))
                