# Creating a List of 10 random strings in Python, & sorting them in ascending and descending order :

list=["i","hey","meow","hola","grass","Valley","Gracias","School","eee","yup"]

# The sorting will be done from the first letter of the word. If the first letters are same, the second ones will be sorted., and so on.
# Basis of sorting : 1. Alphabetical order , 2. Whether the letter is capital or small.


list.sort(reverse = False)
print(list)

# Lowest Value : Capital letter, first in Alphabetical order.
# Highest Value : Small letter, last in Alphabetical order.

list.sort(reverse = True)
print(list)