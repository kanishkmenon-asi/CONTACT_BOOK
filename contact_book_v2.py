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

    def add_contacts(contacts):
        name = str(input("NAME:"))
        phone = str(input("\nPhone number:"))
        contacts[name] = phone
        with open("contact_book.txt","w") as file:
            json.dump(contacts,file)
        return contacts

    def view_contacts(contacts):
        for name, phone in contacts.items():
            print(f"{name} : {phone}")
        return contacts

    def search_contacts(contacts):
        ask_name = str(input("Name:"))
        if ask_name in contacts :
            print(f"{ask_name} : {contacts[ask_name]}")
        else:
            print("CONTACT NOT FOUND")
        return contacts

    def delete_contacts(contacts):
        del_name = str(input("Name to delete:"))
        if del_name in contacts:
            del contacts[del_name]
            with open("contact_book.txt","w") as file:
                json.dump(contacts,file)
            print(f"{del_name} has been deleted")
        else:
            print(f"{del_name}does not exist in the contacts.")
        return contacts

    if user_input == 1:
        contacts = add_contacts(contacts)
    elif user_input == 2:
        contacts = view_contacts(contacts)
    elif user_input == 3:
        contacts = search_contacts(contacts)
    elif user_input == 4:
        contacts = delete_contacts(contacts)
    elif user_input == 5:
        exit()