def phone_book():
    print("\nHI HOW MAY I HELP YOU?")
    contact = {}
    while True:
        print("\nTHESE ARE THE CHOICES OF YOUR PHONE BOOK")
        print("\n1. add contact")
        print("2. delete contact")
        print("3. view contact")
        print("4. exit")

        choice = input("\nplease enter your choice:  ")
        if choice == '1':
            name = input("enter name :  ")
            phone = int(input("enter mobile no :  "))
            email = input("enter the email :  ")
            contact[name] = {"phone": phone, "email": email}
        elif choice == '2':
            to_delete = input("enter the name to delete")
            if to_delete in contact:
                del contact[to_delete]
            else:
                print("sorry contact not found! ")
                print("please enter valid contact name to delete :) ")
        elif choice == '3':
            if contact == {}:
                print("\nsorry no contact is found :( ")   
            else:
                for key,values in contact.items():
                    print(f"\nhere is the list of contacts")
                    print(f"\nname : {key}")
                    print(f'phone : {values["phone"]} email : {values["email"]}')
        elif choice == '4':
            print("\nthank you :) ")
            print(" ")
            break
        else:
            print("\nentered choice is invalid")

phone_book()