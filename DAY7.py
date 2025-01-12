#!/usr/bin/env python3

# Simple Contact Management System using Dictionary
contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"{name} added successfully!")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Phone: {contacts[name]['Phone']}, Email: {contacts[name]['Email']}")
    else:
        print(f"{name} not found!")

def view_all_contacts():
    print("\nAll Contacts:")
    for name, info in contacts.items():
        print(f"{name}: Phone: {info['Phone']}, Email: {info['Email']}")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted!")
    else:
        print(f"{name} not found!")

# Main program loop
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View All Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        view_all_contacts()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("try again")

    else:
        print("Invalid choice. Please try again.")
