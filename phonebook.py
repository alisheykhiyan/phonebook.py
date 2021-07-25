# phonebook.py
print ("Type number '1' to add a contact to the list,type number '2' to see the contacts and the numbers ,try number '3' if you want to do the both reading and appending or press 'Enter' key to exit.")
choosen_command = input (":")
while choosen_command != "Enter":
   if choosen_command == '1':
       contactname = input ("Enter the contacts name:")
       contactnum = int(input("Enter the contacts number:"))
       p = open ('phonebook.txt','w')
       # ("pp") equals to phonebooks_parts .
       pp = (contactname,":",contactnum) 
       p.write(pp)
       p.close()
   if choosen_command == '2' :
       p = open ('phonebook.txt','r') 
       print(p.read())
       p.close()
   if choosen_command == '3' :
       decision = input ("Do you mind reading or appending fisrt? (r/a)")
       if decision == 'r' :
           p = open ('phonebook.txt','w+')
           print (p.read())
           contactname = input ("Enter the contacts name:")
           contactnum = int(input("Enter the contacts number:"))
           p.write(contactname,"=",contactnum)
           p.close() 
       if decision == 'a' :
           p = open ('phonebook.txt','w+')
           contactname = input ("Enter the contacts name:")
           contactnum = int(input("Enter the contacts number:"))
           p.write(contactname,"=",contactnum) 
           print (p.read())
           p.close()

           
    
