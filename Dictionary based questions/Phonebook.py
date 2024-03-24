import sys

phonebook = {}

def contacts():

    def add_contact():
        global phonebook
        name = input("Enter name : ")
        number = int(input("Enter mobile number : "))
        phonebook[number] = name

    def remove_contact():
        global phonebook
        number = int(input("Enter mobile number to remove : "))
        print(f"Number removed : {number} ({phonebook[number]})")
        phonebook.pop(number)

    def search_contact():
        global phonebook
        name = input("Enter name to search : ")
        for i,j in phonebook.items():
            if name == j:
                print(j,"\t",i)
                
    def display_contact():
        global phonebook
        print("\tYour Phonebook : ", end="\n\n")
        print("Name \t Number")
        for i,j in phonebook.items():
            print(j,"\t",i)

    def exit():
        sys.exit()

    print("\n\t\tAvailable options : ")
    print("1. Add a contact \t\t 2. Remove a contact")
    print("3. Serch for a contact \t\t 4. Display all contacts \n5. Exit \n")

    choice = int(input("Enter your choice (1,2,3,4,5): "))

    if choice == 1:
        add_contact()
    elif choice == 2:
        remove_contact()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        display_contact()
    elif choice == 5:
        exit()
    else:
        print("Wrong input entered !!") 


user_in = input("To start phonebook program, enter 'Start' : ")
x = True
while x:
    if user_in == "Start":
        contacts()
    else:
        x = False
        exit
