# ajout des livres
from nanoid import generate

def ajout_livre(collection):
    input_name = input("Veuillez saisir le titre de ce livre\n")
    input_auteur = input("\nVeuillez indiquer le nom de l'auteur du livre\n")
    input_annee = input("\nVeuillez indiquer l'année de parution du livre \n")
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
    collection.insert_one({"_id" : id, "title": input_name, "authors" : [input_auteur], "year" : int(input_annee), "type": type_ouvrage })