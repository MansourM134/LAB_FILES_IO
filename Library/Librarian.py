import json

def add_book(library:dict, title:str, isbn:str, author:str):

    if title not in library:
        library[title] = {}
     
    if isbn in library[title]:
        print("the book already exists in the library")
        return False
   
    library[title][isbn] = {
        "author" : author,
        "available" : True
    }

    with open("library.json", "w" ) as file:
        json.dump(library, file, indent = 4)

    

    return True
        
    

def remove_book(library:dict, title:str, isbn:str):

    if title in library and isbn in library[title]:
        del library[title][isbn]
        if not library[title]:
            del library[title]

            with open("library.json", "w" ) as file:
                json.dump(library, file, indent = 4)

        return True
    else:
        print("there is no book with this isbn")


def check_out_book(library:dict, title:str, isbn:str):
    if title in library and isbn in library[title]:
        if library[title][isbn]["available"] == True:
            library[title][isbn]["available"] = False

            with open("library.json", "w" ) as file:
                json.dump(library, file, indent = 4)

            return True
    else:
        print("this book is not available")
        return False
        

def return_book(library:dict, title:str, isbn:str):


    if title in library and isbn in library[title]:
        if library[title][isbn]["available"] == False:
            library[title][isbn]["available"] = True

            with open("library.json", "w" ) as file:
                json.dump(library, file, indent = 4)

            return True
    else:
        print("this book is not in the library")
        return False


def display_books(json_file:str = "library.json"):

    with open(json_file, "r") as file:
        library = json.load(file)
        
    for title in library:
        for isbn in library[title]:
            print(f"Title:{title}  ISBN: {isbn}  Author: {library[title][isbn]['author']}  Available: {library[title][isbn]['available']}")



