# Global variables
contacts_name = None
contacts_num = None


def add_contact():
    global contacts_name, contacts_num

    contacts_name = input('Enter the contact name: ')
    contacts_num = input('Enter the contact number: ')
    print('Contact added successfully!')


def view_contact():
    global contacts_name, contacts_num

    if contacts_name is not None and contacts_num is not None:
        print(f'Contact Name: {contacts_name}')
        print(f'Contact Number: {contacts_num}')
    
    else:
        print('No contact found!')


def exit_program():
    print('Thanks for your time.', '\nExiting the program...')
    exit()


def main():
    while True:
        print('\nPhone Book Menu:')
        
        choice = input('\nEnter "1" to add a contact, "2" to view the contact and "0" to exit: ')

        if choice == '1':
            add_contact()
        
        elif choice == '2':
            view_contact()
        
        elif choice == '0':
            exit_program()
        
        else:
            print('Invalid choice!')


def starter():
    start_program = input('Do you want to run the phone book program? (yes/no): ').strip().lower()
    if start_program == 'yes':
        main()
    
    else:
        exit_program()


if __name__ == '__main__':
    starter()
    
