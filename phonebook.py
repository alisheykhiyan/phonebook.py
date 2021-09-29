# phonebook.py
print ("------------------------------ welcom to phonebook ------------------------------")

# Hinting to user the directions to use the program:

print ("Enter number 1 to add a number or 2 to quit the program:")

while True :
    run_command_number =int(input("Enter the number (1/2) :"))

    # If user needs to add number(enters '1'):
    if run_command_number == 1:
        contact_name = input("Please enter the contacts name :")
        contact_number = int(input("Then please enter number belongs to this contact :"))

    # If user needs to close program(enters '2'):
    elif run_command_number == 2:
        break

    # If user enters inappropriat input:
    else:
        print("Sorry,inappropriat number or letter entered .")
        
    


