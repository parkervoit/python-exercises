# Python String, List, Dictionary Warmup Exercises

#Write the code that operates on a single string containing the make and model of a vehicle.
#The first part of the string before the space is the make
#The last part of the string after the space is the model
#We can assume that the strings will only have one space.
#Assume the input string is completely lower-cased.#

## Exercise #1
#rite the code to take a string and produce a dictionary out of that string such that the output looks like the following:
#Some thoughts:
#- You'll need a way to get the first part of the string and a way to get the second part of the string
#- Feel free to make new variables/data types in between the string and the output dictionary


truck = "toyota tacoma"
strtruck= truck.split()
truck = {"make": strtruck[0], "model": strtruck[1]}
print(truck)

## Exercise #2
#Write the code that takes a dictionary containing make/model for a vehicle and capitalizes the first character of the make and the model:
    ## Uses truck dictionary made in exercise 1
truck["make"].capitalize()
truck["model"].capitalize()
print(truck)

## Exercise #3
#Create a list of 3 dictionaries where each dictionary represents a vehicle, as above
#Write the code that operates on that list of dictionaries in order to uppercase the entire make and model values.

trucks = [{
    "make": "Toyota",
    "model": "Tacoma"
},
{
    "make": "Honda",
    "model": "Fit"
},
{
    "make": "Ford",
    "model": "Focus"
}]

for x in trucks:
    x['make'] = x['make'].upper()
    x['model'] = x['model'].upper()
    print(x)