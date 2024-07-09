# Contact Management System

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        new_contact = Contact(name, phone_number, email, address)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts found!")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    def search_contact(self, query):
        found_contacts = [contact for contact in self.contacts if query in contact.name or query in contact.phone_number]
        if not found_contacts:
            print("No contacts found!")
        else:
            print("Search Results:")
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    def update_contact(self, name, phone_number, email, address):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = phone_number
                contact.email = email
                contact.address = address
                print(f"Contact '{name}' updated successfully!")
                return
        print("Contact not found!")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully!")
                return
        print("Contact not found!")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone_number, email, address)
        elif choice == "2":
            contact_manager.view_contact_list()
        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            contact_manager.search_contact(query)
        elif choice == "4":
            name = input("Enter name of contact to update: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact_manager.update_contact(name, phone_number, email, address)
        elif choice == "5":
            name = input("Enter name of contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()