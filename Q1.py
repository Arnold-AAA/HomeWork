"""using the reference provided here, https://en.wikipedia.org/wiki/List_of_municipalities_of_Estonia_by_area
* represent the Municipality and Population of all 10 municipalities with the best collection available in python
* implement the option of allowing the user change the population any municipality of their choice based on value entered
i.e if i want to change the population of "Märjamaa" then I just need to enter "MA" and the new population I want to change
( Hint: Märjamaa = MA, Illuka = IL, Vändra = VA )"""
name=input("Please enter your name: ")
municipalities = {"MA" : 7433,
                  "IL" : 1034,
                  "AN" : 6276,
                  "SA" : 2334,
                  "KE"  : 5181,
                  "VI" :5625,
                  "KU"  : 4626,
                  "JO"  : 5340,
                  "VA" : 2568,
                  "KO"  : 1331,
                  "RA"  : 4355}
print(f"{name} Welcome to out municipalities data base {municipalities}")
update = input("Do you want update municipalities population? yes/no ")
if update == "yes":
    what_munic = input("What municipalities do you want update? ").upper()
    new_population = input("Please enter new population: ")
    municipalities[what_munic] =  new_population
    print(municipalities)
else:
    print("Ok thank you!")