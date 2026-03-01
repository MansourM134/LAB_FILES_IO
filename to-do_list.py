'''
Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no.
If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , 
then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"
'''

while True:
    user_choice = input("do you want to add a new To-Do item? answer by y for yes and n for no: ")

    if user_choice == "y":
        new_item = input("enter the new To-do item: ")
        file = open("to_do.txt", "a", encoding="UTF-8")
        file.write(f"{new_item} \n")
        file.close()
    elif user_choice == "n":
        user_last_choice = input("do you want to list your To-Do items ? answer y for yes and n for no: ")
        if user_last_choice == "y":
            file = open("to_do.txt", "r", encoding="UTF-8")
            list = file.readlines()
            for item in list:
                print(item)
                file.close()
        elif user_last_choice == "n":
            continue
    elif user_choice == "exit":
        print("thank you for using the To-Do program, come back again soon")
        break

