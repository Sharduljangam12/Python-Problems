import json

contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"{name} added.")

def show_all():
    if contacts:
        for name, phone in  contacts.items():
            print(f"{name}:{phone}")
    else:
        print("No contacts yet.")

def delete_contacts(name):
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted.")
    else:
        print("Contact not found.")

def lookup_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def save_contacts():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)
    print("Contacts saved")

def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        pass

load_contacts()
while True:
    print("\nWhat do you want to do?")
    print("1. Add contacts")
    print("2. Look up contact")
    print("3. Delete contanct")
    print("4. Show all")
    print("5. Quit")

    choice = input("Enter 1-5: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        add_contact(name,phone)
    elif choice == "2":
        name = input("Name to look up:")
        lookup_contact(name)
    elif choice == "3":
        name = input("Name to delete: ")
        delete_contacts(name)
    elif choice == "4":
        show_all()
    elif choice == "5":
        save_contacts()
        break 