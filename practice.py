# Print Items in a list

def roll_call_dwarves(dwarf_names):
    for index,name in enumerate(dwarf_names,start=1):   
        print(f"{index}. {name}")       

roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"]) 


# Capitalize first letter and add !
def summon_captain_planet(planteer_calls): 
    plant_calls = []
    for item in planteer_calls:
        plant_calls.append(item.capitalize() + "!")
    print(f"{plant_calls}") 
    
summon_captain_planet(["earth", "wind", "fire", "water", "heart"])


def happy_new_year(i):
    while i > 0:
        print(i)
        i-= 1

    print("happy new year")

happy_new_year(10)  

# Square Integers in a list
def square_integers(list):
    squared_list = []

    for item in list:
        squared_list.append(item*2)

    print(f"{squared_list}")  
    return squared_list

square_integers([1, 2, 3, 4, 5]) 


# Write a function fizzbuzz() that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".
def fizzbuzz():
    i = 0
    while i<=100:
        if i%3 == 0:
            print("Fizz") 
        elif i%5 == 0:
            print("Buzz")
        elif i%3 and i%5 == 0:
            print("FizzBuzz") 
        else:
            print(f"{i}")
        i += 1

fizzbuzz()