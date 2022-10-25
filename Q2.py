"""Q2, create a registration form for user to provide the following information and save it ( hint : use a dictionary)
name, age, email, nationality, password
checks
** if the name is not alphabet end the program ( or ask user to provide an alphabetical name)
** if the age is less than 18, end and inform the user they must be 18 above
** ask for the password twice and compare that the first provided password and second one are the same
*** if all these are done, then print out the user information but encrypt the password provided by the user.
e.g. your print statement should show something like ******** for the password and not show the password the user provided
you want to encrypt the password of a new user to your system
the user provides their user_name, and password.
Using your knowledge of collections, encrypt the password to always replace the"""

customer_data = {}
customer_name = str(input("Enter Your name: ").capitalize())
if customer_name.isalpha() == True and len(customer_name) >= 4:
    print(f"Hello, {customer_name}!")
else:
    print("Please enter only latter's and your name should have at least 4 latter's")
    exit()
age = int(input("Please enter your age:"))
if age < 18:
    print (f"Sorry {customer_name} you are too young. You should be above 18 ")
    exit()
else:
    age > 18
    print(f"Welcome  {customer_name}!")
    password1=input("Please enter your password:")
    password2=input("Please confirm your password:")
    len_pass = len(password2)
    encrypted_password = len_pass*"*"
    if password1 != password2:
        print("Password doesn't match.")
    else:
        print("Your data saved to our base")
customer_data.update({f"{customer_name}": 1, f"{age}": 2, f"{encrypted_password}": 3})
print(customer_data.keys())