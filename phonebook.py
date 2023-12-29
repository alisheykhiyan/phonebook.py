# Phonebook.py
print("---------------Welcome to phonebook---------------")
command = int(input("To add a contact enter number 1 and to exit, print number 0 : "))
if command == 0:
    print("Thanks for running the program !")
    exit()
elif command == 1:
    name = input("Enter the contacts name : ")
    num = int(input("Enter the contacts numer : "))
else:
    print("ERROR: Invalid input")

while True:
    command = int(input("To see the contacts name and number press 1, to add a new contact press 2,"
                        "and press 0 to quit the program :"))
    if command == 0:
        print("Thanks for running the program !")
        break
    elif command == 1:
        print(f"Name: {name} ", f"Number: {num}")
    elif command == 2:
        name = input("Enter the contacts name : ")
        num = int(input("Enter the contacts numer : "))
    else:
        print("ERROR: Invalid input")
