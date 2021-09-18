# phonebook.py
print ("------------------------------ welcom to phonebook ------------------------------")

# Hinting to user the directions to use the program:

print ("Enter number 1 to add a number or 2 to quit the program:")

while True :
    decision =int(input("Enter the number 1 or 2 to continue :"))

    # If user needs to add number(enters '1'):
    if decision == 1:
        name = input("Please enter the contacts name :")
        number = int(input("Then please enter number belongs to this contact :"))

    # If user needs to close program(enters '2'):
    elif decision == 2:
        break

    # If user enters inappropriat input:
    else:
        print("Sorry,inappropriat number or letter entered .")
        

