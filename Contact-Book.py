contact = {}
def showcontact():
    print(contact.items())
    print("name \t Contest")
    for key in contact:
        print("{} \t {} ".format(key,contact.get(key)))


while True:
    choice = int(input("1. Add the Contact : \n"
                   "2. Edit the Contact : \n"
                   "3. Search the Contact : \n"
                   "4. Display the Contact : \n"
                   "5. Delete the Contact : \n"
                   "6. Closed the Contact : \n"
                   "Please Enter the Number between 1 to 6 : "))

    if choice == 1:
        name = input(" Enter The Name : ")
        number = input("Enter The NUmber : ")
        contact[name]= number

    elif choice == 2:
        edit = input("Edit The Contact : ")
        if edit in contact:
            name = input("Change Your Name : ")
            phone = input("Change Your Number : ")
            contact[edit] = name , phone
            print("The Contact Updated Successfully")
            showcontact()
        else:
            print("The Name is not Found")
    elif choice == 3:
        search = input("Search The Contact : ")
        if search in contact:
            print(search , "Contact Number is ", contact[search])
        else:
            print("Don't Found the Contact ")

    elif choice == 4:
        if not contact:
            print("The Contact is empty")
        else:
            showcontact()

    elif choice == 5:
        delete = input("Which Contact Do you want delete : ")
        if delete in contact:
            deletecon = input("Do you want to delete Contact [y/n] : ")
            if deletecon == "y" or deletecon == "Y":
                contact.pop(delete)
                print("The Contact Delete Successfully")
                showcontact()
        else:
            print("The Contact is not found")



    else:
        break