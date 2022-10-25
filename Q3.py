""" Allow a user provide the list of countries they would like to visit.
 order the list in alphabetical order and return the list to the user.
 then allow user inform of one destination they would like to visit.
 Once that is provided remove it from the list and wish the user safe flights"""

name = input("Please enter you name:") #Person name
countries = [] #our list of countries
while True:
    wtfly = input(f"""{name} Please enter a countries you would like to visit.
To finish this process enter 'q':""")
    if wtfly == "q":
        break
    countries.append(wtfly)#adding countries to the list
print(countries) # list before sort
countries.sort() # sort the list in  alphabetical order
print(countries) # sorted list
choose=str(input(f"{name} make your choice now?"
             "Enter this country here please:"))
print(f"Have a safe flight{name} to {choose}")
countries.remove(choose)
print(f"Other countries {name} wouldn't like to visit {countries}")
