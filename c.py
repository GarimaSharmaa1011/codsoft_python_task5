# Contact Book Program

# A dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found!")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['Phone']}")

# Function to search for a contact
def search_contact():
    query = input("Enter name or phone number to search: ")
    found = False

    for name, details in contacts.items():
        if query.lower() in name.lower() or query == details["Phone"]:
            print(f"\nContact Found: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            found = True
            break
    if not found:
        print("Contact not found!")

# Function to update contact details
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("\nWhat do you want to update?")
        print("1. Phone Number")
        print("2. Email")
        print("3. Address")
        choice = input("Enter your choice: ")

        if choice == "1":
            new_phone = input("Enter new phone number: ")
            contacts[name]["Phone"] = new_phone
        elif choice == "2":
            new_email = input("Enter new email: ")
            contacts[name]["Email"] = new_email
        elif choice == "3":
            new_address = input("Enter new address: ")
            contacts[name]["Address"] = new_address
        else:
            print("Invalid choice!")
            return
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

# Main program loop
def main():
    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid choice. Please try again!")

# Run the program
if __name__ == "__main__":
    main()
