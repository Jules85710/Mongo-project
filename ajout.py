# ajout des livres
from nanoid import generate

def ajout_livre(collection):
    input_name = input("Veuillez saisir le titre de ce livre\n")
    List_auteur =[]
    input_auteur = input("\nVeuillez indiquer le nom de l'auteur du livre\n")
    List_auteur.append(input_auteur)
    
    autre_auteur = True
    while autre_auteur :
        print("\nY-a-il un autre auteur qui a contribué à l'écriture de cette oeuvre? \n")
        input_auteur = input("saissisez le nom de cette autre auteur ou appuyer sur entrer s'il n'y en a pas d'autre.\n")
        if input_auteur == "":
            autre_auteur = False
        else :
            List_auteur.append(input_auteur)
            
    input_annee = input("\nVeuillez indiquer l'année de parution du livre \n")
    while not(len(input_annee)<5 and input_annee.isnumeric() and int(input_annee)<2025 ) :
        print("Vous n'avez pas saisi une année.")
        input_annee = input( "\nVeuillez ressaisir l'année de parution du livre.\n")
    print("\nVeuillez indiquer le type de votre ouvrage parmi les suivants : ")
    print("1 : pour un livre")
    print("2 : pour un article")
    print("3 : pour une thèse\n")
    input_type = input("Quel est le type de votre ouvrage ?\n")
    
    while not(input_type == "1" or input_type == "2" or input_type == "3"):
        input_type = input("Je n'ai pas compris votre réponse. \nVeuillez ressaisir votre choix.\n")
    
    if input_type == "1":
        type_ouvrage = 'Book'
    elif input_type == "2":
        type_ouvrage = 'Article'
    else :
        type_ouvrage = 'Phd'
    id = generate(size = 8)
    collection.insert_one({"_id" : id, "title": input_name, "authors" : List_auteur, "year" : int(input_annee), "type": type_ouvrage })
    
    if type_ouvrage == "Book":
        print(f"\nLe livre : '{input_name}' a bien été ajouté.")
    elif type_ouvrage == "Article":
        print(f"\nL'article : '{input_name}' a bien été ajouté.")
    else :
        print(f"\nLa thèse : '{input_name}' a bien été ajoutée.")