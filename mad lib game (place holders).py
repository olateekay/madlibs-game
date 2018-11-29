"""
This program promts the user for words and prints a story with those words 
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!'Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %s ruled the world."
print ("Mad Libs is starting") #notify the use that the game is starting

name = input("Enter a name: ")
adjective_1 = input("Enter the first adjective: ")
adjective_2 = input("Enter the second adjective: ")
adjective_3 = input("Enter the third adjective: ")

verb = input("Enter a verb: ")
first_noun = input("Enter the first noun: ")
second_noun = input("Enter the second noun: ")

animal = input("Enter an animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
superhero = input("Enter a superhero: ")
country = input("Enter the name of a country: ")
dessert =  input("Enter your favourite dessert: ")
year = input("Enter your year of choice: ")

print (STORY % (name, adjective_1, adjective_2, animal, food, verb, first_noun, fruit, adjective_3, name, superhero, name, country, name, dessert, name, year, second_noun))









