#39999999999 code fore man
#49999999999 code for women
#10999999999 code for child
customer_name = str(input("Enter Your name: ").capitalize())
if customer_name.isalpha() == True and len(customer_name) >= 4:
    print(f"Hello, {customer_name}!")
else:
    print("Please enter only latter's and your name should have at least 4 latter's")
    exit()
age = int(input("Please enter your age:"))
if age <= 17:
    print (f"Sorry {customer_name} you are too young for our library")
else:
    age >=18
    print(f"Welcome to our library {customer_name}!")
    idcode = input(f"{customer_name},please enter your 11 numbers ID code. Please use only numbers:")
    if (len(idcode)) == 11 and idcode.isnumeric() == True:
        gender = idcode[0]
        if gender == ("3"):
            print("Welcome to the library my man!")
        elif gender == ("4") == ("woman"):
            print("Welcome to the library lady!")
        else:
            gender == ("1")
            print("Go home kid!")
        if gender == "3" or gender == "4":
            print(f"{customer_name}, since you are new in our library. You can get only one book")
            book1=("Hamlet")
            book1price=10
            book2=("Dive into python")
            book2price=25
            book3=("Invisible man")
            book3price=30
            print("""
    1)Hamlet
    2)Dive into python
    3)Invisible man
    """)
            book_choosen = str(input("Enter book name please:")).capitalize()
            if book_choosen[:2] == "Ha" and book_choosen.isalpha():
                print(f"| {customer_name} | {gender} 3=man 4=woman | {book1} | {book1price} euro |")
            elif book_choosen[:3] == "Div" and book_choosen.isalpha():
                print(f"| {customer_name} | {gender} 3=man 4=woman | {book2} | {book1price} euro |")
            elif book_choosen[:4] == "Invi" and book_choosen.isalpha():
                print(f"| {customer_name} | {gender} 3=man 4=woman | {book3} | {book1price} euro |")
            else:
                book_choosen.isnumeric()
                print("Sorry we dont have this book")
    else:
        (len(idcode)) >= 11 and (len(idcode)) <= 11 and idcode.isalpha() == True
        print("Wrond ID number")