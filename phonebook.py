# phonebook.py

print ("--------- welcom to phonebook ---------")


# Hinting to user the directions to use the program :


print ("Enter number 1 to add a number or 2 to quit the program:")


# Reciving the users preferation :
while True :
    run_decision = int(input("Enter the number 1 or 2 to continue :"))


    # What happens if user preffered (1):
    if run_decision == 1:
        contact_name = input("Please enter the contacts name :")
        contact_number = int(input("Then please enter number belongs"
                                   " to this contact :"))


    # What happens if user preffered (2):


    elif run_decision == 2:
        break


    # What happens if user enters inappropriat input:
    else:
        print("Sorry,inappropriat number or letter entered .")
        
    


