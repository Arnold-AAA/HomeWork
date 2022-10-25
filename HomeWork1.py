name = str(input("Plese enter your name: "))
print ("Hello",name)
age = int(input("How old are you? "))
if age <=17:
    print("Sorry", name, "you are too young for our library")
else:
    print("Welcome to our library",name,".You can get any books you want,but not more than 3 at same time")
    borrowed_books = str(input("Did you borrow some books before? (yes/no?)"))
    if borrowed_books == ("yes"):
        borrowed=int(input("How many?"))
        if borrowed >=3:
            print("Sorry",name,"you cant get more books")
        else:
            borrowed >=2
            print("You can get more books")
            want_borrow=int(input("How many books do you want to borrow? "))
            if want_borrow+borrowed >=4:
                print("Sorry",name,"you cant get more than 3 books")
            else:
                want_borrow+borrowed <=2
                print("Yes you can borrow this books, but not more than 3 total")
                print("One book cost 10 Euro. You have to pay",want_borrow*10,"Euro")
    else:
        borrowed_books == ("no")
        want_get=int(input("How many books do you want to borrow now? "))
        if want_get >=4:
            print("You cant borrow so many books. You can get three books total")
        else:
            want_get <=3
            print("You can get this books")
            print("One book cost 10 Euro. You need to pay", want_get * 10, "Euro")
wtb=str(input("Do you want maybe buy some books? (yes/no)"))
if wtb == ("yes"):
    print("We have three books now")
    print("1)Story of Love. Cost 10 Euro")
    print("2)History of Estonia. Cost 25 Euro")
    print("3)The war in Ukraine. Cost 30 Euro")
    balance = 30
    book1=10
    book2=25
    book3=30
    print("Now you have 30 Euro, on your library balance")
    what_book=int(input("What book do you want to buy? Please enter a number (1/2/3)?"))
    if what_book == (1):
        print("You have to pay",book1,"Euro")
        print("Your balance now",balance - 10,"Euro")
    elif what_book == (2):
        print("You have to pay", book2, "Euro")
        print("Your balance now", balance - 25, "Euro")
    else:
        what_book == (3)
        print("You have to pay", book3, "Euro")
        print("Your balance now", balance - 30, "Euro")
else:
    wtb == ("no")
print("Have a nice day",name)