# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = [x.upper() for x in fruits]
# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [x.capitalize() for x in fruits]
# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
vowels='aeiou'
def has_vowels(value):
    for s in value:
        if s in vowels:
            return True
    else:
            return False
def count_vowels(value):
    count = 0 
    for i in value:
        if(has_vowels(i)==True):
            count += 1
    return count
fruits_with_more_than_two_vowels = [x for x in fruits if count_vowels(x) > 2]
print(fruits_with_more_than_two_vowels)
# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
vowels='aeiou'
def has_vowels(value):
    for s in value:
        if s in vowels:
            return True
    else:
            return False
def count_vowels(value):
    count = 0 
    for i in value:
        if(has_vowels(i)==True):
            count += 1
    return count
fruits_with_only_two_vowels = [x for x in fruits if count_vowels(x) == 2]
print(fruits_with_only_two_vowels)
# Exercise 5 - make a list that contains each fruit with more than 5 characters
def count_char(char):
    return len(char)
more_than_5 = [x for x in fruits if count_char(x) > 5]
# Exercise 6 - make a list that contains each fruit with exactly 5 characters
def count_char(char):
    return len(char)
more_than_5 = [x for x in fruits if count_char(x) == 5]
# Exercise 7 - Make a list that contains fruits that have less than 5 characters
def count_char(char):
    return len(char)
more_than_5 = [x for x in fruits if count_char(x) < 5]
# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
characters_in_fruit = [len(x) for x in fruits]
# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = [x for x in fruits if 'a' in x]
# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [x for x in numbers if x % 2 == 0]
# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [x for x in numbers if x % 2 != 0]
# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [x for x in numbers if x > 0]
# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [x for x in numbers if x < 0]
# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
two_or_more = [x for x in numbers if len(abs(str(x))) >= 2]
# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [x ** 2 for x in numbers]
# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [x for x in numbers if x % 2 != 0 and x < 0]
# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = [x + 5 for x in numbers]
# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
primes = [x for x in numbers if all(x % y != 0 for y in range(2, x)) and  x > 0]