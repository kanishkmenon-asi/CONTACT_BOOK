import json

# 1. FUNCTIONS FIRST - before everything
def add_contacts(contacts):
    name = str(input("NAME:"))
    phone = str(input("Phone number:"))
    star = str(input("Star this contact? y/n: "))
    
    if star == 'y':
        is_starred = True
    else:
        is_starred = False
    
    contacts[name] = {"phone": phone, "starred": is_starred}
    
    with open("contact_book.txt","w") as file:
        json.dump(contacts,file)
    return contacts

def view_contacts(contacts):
    if len(contacts) == 0:
        print("CONTACT BOOK IS EMPTY")
    else:
        for name, info in contacts.items():
            phone = info["phone"]
            starred = info["starred"]
            if starred == True:
                print(f"⭐ {name} : {phone}")
            else:
                print(f"{name} : {phone}")
    return contacts

def search_contacts(contacts):
    ask_name = str(input("Name:"))
    if ask_name in contacts:
        phone = contacts[ask_name]["phone"]
        starred = contacts[ask_name]["starred"]
        if starred == True:
            print(f"⭐ {ask_name} : {phone}")
        else:
            print(f"{ask_name} : {phone}")
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
        print(f"{del_name} does not exist in the contacts.")
    return contacts

def edit_contacts(contacts):
    user_edit = str(input("Name of contact to edit:"))
    if user_edit in contacts:
        new_phone = str(input("New phone number:"))
        contacts[user_edit]["phone"] = new_phone
        with open("contact_book.txt","w") as file:
            json.dump(contacts,file)
        print(f"{user_edit}'s contact has been updated.")
    else:
        print(f"{user_edit} does not exist in the contacts.")

# 2. LOAD FILE
try:
    with open("contact_book.txt","r") as file:
        contacts = json.load(file)
except:
    contacts = {}

# 3. MENU LOOP
while True:
    print("------------")
    print("CONTACT BOOK")
    print("------------")
    print("1.ADD NEW CONTACT")
    print("2.VIEW CONTACTS")
    print("3.SEARCH CONTACT")
    print("4.EDIT CONTACT")
    print("5.DELETE CONTACT")
    print("6.EXIT")
    user_input = int(input("\nChoose an option (1-5): "))

    if user_input == 1:
        contacts = add_contacts(contacts)
    elif user_input == 2:
        contacts = view_contacts(contacts)
    elif user_input == 3:
        contacts = search_contacts(contacts)
    elif user_input == 4:
        contacts = edit_contacts(contacts)
    elif user_input == 5:
        contacts = delete_contacts(contacts)
    elif user_input == 6:
        exit()
