import os
import sys
import math

# defines operations and important items for things
species = {}
option1 = "check"
option2 = "add"
option3 = "finalize"


# allows for the creation of new animals and the amount that exist
class Animals():
    def __init__(self, amount, name):
        self.num = int(amount)
        self.name = str(name)


# creates a animal object
def createanimal(usernam, usernum):
   usernam = Animals(usernum, usernam)
   species[usernam] = usernum

   return usernam, species


# Allows for adding, checking, and finding of H
def listoptions(op):
    h = 0
    total = 0

    # adds animals to the dictionary of species
    if str(option1) == str(op):
            print(species)

    # checks and prints the list of current elements in the dictionary
    elif str(option2) == str(op):
        while True:
            q = str(input("Do you wish to add an animal? Y/N "))

            if q == 'y':
                n = str(input("What is the name of the animal you wish to add: "))
                num = int(input("How many do you wish to add: "))

                createanimal(str(n), num)

                print("You have created a %s and there are %d of them" % (n, num))

            elif q == 'n':
                break

            else:
                print("I didn't quite get that. Please try again! \n")

    # finalizes and calculates for H
    elif str(option3) == str(op):
        for animal in species:
            total += int(species[animal])
            pi = species[animal]/total
            lnpi = math.log(pi)
            h = -(pi * lnpi)
            print("H= %.3d" % float(h))

            break

    return species, createanimal, h


print("""Hello and welcome to this Simulation. This simulation is designed to represent Biological Diversity within
an environment. All you have to do is provide a few species to this environment and then you have yourself an ecosystem!""")

begin = str(input("Would you like to begin? y/n"))

if begin == 'y':
    while True:
        options = str(input("""\nWould you like to:
Add
Check
Finalize \n"""))

        listoptions(options)