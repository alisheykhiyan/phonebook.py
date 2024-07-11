import os

contacts_file = 'contacts.txt'

def file_initializer(contact_name, contact_num):
    # Writes a contact's name and number to the contacts file.
    with open(contacts_file, 'a') as file:
        file.write(f'{contact_name}: {contact_num}\n')
    print('Contact added successfully!')


def add_contact():
    # Prompts the user to enter a contact name and number, then writes it to the file.
    contact_name = input('Enter the contact name: ')
    contact_num = input('Enter the contact number: ')
    file_initializer(contact_name, contact_num)



def main():
    # Main menu loop for the phone book program.
    while True:
        print('\nPhone Book Menu:')
        print('1. Add a contact')
        print('0. Exit')
        
        choice = input('Enter your choice: ')

        if choice == '1':
            add_contact()
        elif choice == '0':
            print('Exiting program...')
            break
        else:
            print('Invalid choice!')


def starter():
    # Asks the user if they want to run the phone book program.
    start_program = input('Do you want to run the phone book program? (yes/no): ').strip().lower()
    if start_program == 'yes':
        main()
    else:
        print('Thanks for your time.', '\nExiting the program...')
        exit()

if __name__ == '__main__':
    print("Current Working Directory:", os.getcwd())
    starter()
    
