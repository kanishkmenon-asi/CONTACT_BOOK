import json
try :
    with open("contact_book.txt","r") as file:
        contacts = json.load(file)
except:
    contacts = {}

while True:
    print("------------")
    print("CONTACT BOOK")
    print("------------")
    print("1.ADD NEW CONTACT")
    print("2.VIEW CONTACTS")
    print("3.SEARCH CONTACT")
    print("4.DELETE CONTACT")
    print("5.EXIT")
    user_input = int(input("\nChoose an option (1-5): "))

    if user_input == 1:
        name = str(input("NAME:"))
        phone = str(input("\nPhone number:"))
        contacts[name] = phone
        with open("contact_book.txt","w") as file:
            json.dump(contacts,file)
    elif user_input == 2:
        for name, phone in contacts.items():
            print(f"{name} : {phone}")
    elif user_input == 3:
        ask_name = str(input("Name:"))
        if ask_name in contacts :
            print(f"{ask_name} : {contacts[ask_name]}")
        else:
            print("CONTACT NOT FOUND")
    elif user_input == 4:
        del_name = str(input("Name to delete:"))
        if del_name in contacts:
            del contacts[del_name]
            with open("contact_book.txt","w") as file:
                json.dump(contacts,file)
                print(f"{del_name} has been deleted")
        else:
            print(f"{del_name}does not exist in the contacts.")
exit()