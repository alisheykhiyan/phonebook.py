print ('--------- welcom to phonebook ---------')
print ('Enter letter (a) to add a number or letter (q) to quit the program:')

num_comment = ' Then please enter number belongs to this contact : ' 
name_comment = 'Please enter the contacts name :'

while True :
    run_command = input('Enter the letter (a) or (q) to continue :')
    if run_command == "a":
        contact_name = input(name_comment) 
        contact_number = input(contact_num_comment)

    elif run_command == "q":
        break
        
    else:
       print('Sorry,inappropriat number or letter entered .')
