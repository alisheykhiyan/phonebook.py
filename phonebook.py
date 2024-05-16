# Phonebook.py
print("---------------Welcome to phonebook---------------")


# Run command
command = input("To add a contact enter number 1 and to exit, enter number 0 : ")


if command == "0":
    print("Thanks for running the program !")
    exit()

elif command == "1":
    name = input("Enter the contacts name : ")
    num = input("Enter the contacts number : ")

else:
    print("ERROR: Invalid input")
    command = input("To add a contact enter number 1 and to exit, enter number 0 : ")


if command != "1":
    pass

else:
    while True:
        command = input("To view the contacts name and number enter '1', to add a new contact enter '2' ",
                        "and enter '0' to quit the program : ")

        if command == "0":
            print("Thanks for running the program !")
            break

        elif command == "1":
            print(f"Name: {name} ", f"Number: {num}")

        elif command == "2":
            name = input("Enter the contacts name : ")
            num = int(input("Enter the contacts numer : "))

        else:
            print("ERROR: Invalid input")
