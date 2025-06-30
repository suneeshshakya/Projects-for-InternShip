contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found!")
        return
    
    print("\nAll Contacts:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. Name: {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print()

def edit_contact():
    if not contacts:
        print("No contacts to edit!")
        return
    
    view_contacts()
    try:
        index = int(input("Enter contact number to edit: ")) - 1
        if 0 <= index < len(contacts):
            print("Enter new details:")
            contacts[index]['name'] = input("Name: ")
            contacts[index]['phone'] = input("Phone: ")
            contacts[index]['email'] = input("Email: ")
            print("Contact updated successfully!")
        else:
            print("Invalid contact number!")
    except:
        print("Invalid input!")

def delete_contact():
    if not contacts:
        print("No contacts to delete!")
        return
    
    view_contacts()
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted = contacts.pop(index)
            print(f"Contact {deleted['name']} deleted successfully!")
        else:
            print("Invalid contact number!")
    except:
        print("Invalid input!")

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        edit_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        break
    else:
        print("Invalid choice!")