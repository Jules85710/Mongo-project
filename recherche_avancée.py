# recherche avancée
import pandas as pd

def recherche_avancee(collection):
    print('\n------------------recherche filtrée-------------------')
    print("\nNous allons remplir les filtres pour chaque variable une à une.")
    print("Si vous ne voulez pas filtrer suivant une variable il suffit de ne rien indiquer lorsqu'on vous questionnera sur cette variable.\n")
    print("\n---------------------titre----------------------------")
    mot_0 = input("\nVeuillez saisir le premier mot que doit contenir le titre des livres que vous cherchez : \n (Si vous ne voulez pas filtrer suivant le titre vous n'avez qu'à appuyer sur entrer.)\n")
    liste_mots=[]
    while not(mot_0)=="":
        liste_mots.append(mot_0)
        mot_0 = input("\nVeuillez saisir un mot de plus que doit contenir le titre des livres que vous cherchez : \n (Si vous ne voulez pas ajouter de mot à ce filtre vous n'avez qu'à appuyer sur entrer.)\n")
    
    print('\n---------------------années---------------------------')
    print("\nNous allons filtrer les oeuvres suivant une liste d'année. \n (Si vous ne voulez pas filtrer suivant les années vous n'avez qu'à appuyer sur entrer.) ")
    
    year_0 = input("\nVeuillez saisir une première année  \n")
    liste_year = []
    
    while not(year_0)=="":
        if year_0.isnumeric() and  int(year_0)<2025 :
            liste_year.append(year_0)
            year_0 = input("Veuillez saisir une année suplémentaire. (Si vous ne voulez pas ajouter d'année à la liste, vous n'avez qu'à appuyer sur entrer.)\n")
        else : 
            year_0 = input("Vous n'avez pas saisi une année. \n Veuillez la ressaisir ou appuyer sur entrer pour passer au filtre suivant.\n")
    
    liste_authors = []
    print('---------------------auteurs--------------------------\n')
    print("Nous allons filtrer les oeuvres suivant une liste d'autheurs. \nAinsi, tous les livres écrit dont l'un des auteurs figure dans la liste seront sélectionnés. \n")
    print("(Si vous ne voulez pas filtrer suivant les auteurs vous n'avez qu'à appuyer sur entrer.)\n")
    author_0 = input("Veuillez saisir un premier auteur  \n")
    while not(author_0)=="":
        liste_authors.append(author_0)
        author_0 = input("\nVeuillez saisir un auteur de plus à la liste : \n (Si vous ne voulez pas ajouter d'auteur à la liste vous n'avez qu'à appuyer sur entrer.)\n")
    print('---------------------type----------------------------')
    print("Nous allons filtrer suivant le type de l'ouvrage.\n")
    print("Entrer : Pour sélectionner tout type d'ouvrage")
    print("1 : Pour sélectionner uniquement les livres.")
    print("2 : Pour sélectionner uniquement les articles")
    print("3 : Pour sélectionner uniquement les thèses")
    type_input = input("\nQuel est votre choix ?\n")
    while not(type_input == "" or type_input =="1" or type_input =="2" or type_input == "3") :
        type_input = input("\nJe n'ai pas compris, veuillez ressaisir votre choix.\n")
    
    #creation du dictionnaire qui va stocker tous les choix des filtres 
    dico = {}
    if len(liste_mots) > 0:
        dico['title'] = liste_mots
    if len(liste_authors) > 0:
        dico['authors']= liste_authors
    if len(liste_year) > 0:
        dico['year'] = liste_year
    if type_input == "1":
        dico['type'] = "Book"
    elif type_input == "2":
        dico['type'] = "Article"
    elif type_input =="3":
        dico["type"] = "Phd"
    
    print(f"\nLe filtre choisi est donc {dico}\n")
    dico_requete = {}
    for keys in dico.keys():
        if keys == 'title':
            list_title = dico[keys]
            dico_requete['title'] = {"$and" : [{"title": {"$regex": mot, "$options": "i"}} for mot in list_title]}
        elif keys == "authors" :
            list_authors = dico[keys]
            dico_requete['authors'] = {"authors" : {"$elemMatch": {"$in": list_authors}}}
            
            
        elif keys == 'year':
            list_year = dico[keys]
            dico_requete['year'] = {'$or' : [{'year' : int(year)} for year in list_year]}
        if keys == 'type' :
            dico_requete['type'] = {'type' : dico[keys]}
            

    results = collection.find({"$and" : [requete for requete in dico_requete.values()]})
    data = pd.DataFrame(list(results))
    return(data)
            