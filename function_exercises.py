#1. 
print("Question 1")
#prompts user for an input
x = input("input 2, please")
def is_two(x):
#boolean operators to check if value entered is a 2 as a string or int datatype
    if x == "2" or x == 2:
        return True
    else :
        return False  
#returns result for user 
print(is_two(x))
 
#2
print("Question 2")
# asks for a user input
value = input("input a letter:")

def is_vowel(value):
    #checks if input is found in list of vowels
    if value in ('a','e','i','o','u', 'A','E','I','O','U'):
        return True
    else:
        return False
# returns true/false statement whether the input string is a vowel
print(is_vowel(value))

#3
print("Question 3")
# asks for a user input
value = input("input a letter:")
def is_consonant(value):
    #checks if input is a vowel using the previous is_vowel function. If it is false, then it means we have a consonant and returns true
    if is_vowel == False:
        return True
    else:
        return False
#prints true/false statement confirming if the letter is a consonant
print(is_consonant(value))

#4. 
print("Question 4")
#prompts user for an input
wrd = input("gimme a word:")
def cap_word(wrd):
    # calls is_constant function to see if the first word is a consonant
    if is_consonant(wrd[0]) == True:
        #if true, word is capitalized
        return wrd.capitalize()
    else:
        return wrd
print(cap_word(wrd))

#5. 
# divided tipamt by 100 so that the value is stored as a decimal 
tipamt = float(input("input your tip percentage: ")) / 100 
#prompt user for bill total
bill= float(input("what's your total bill:"))
def calculate_tip(tipamt, bill):
    # finds tip amount, adds it to the total, and outputs the bill with tip included
    total = (tipamt * bill) + bill
    return total 
print(calculate_tip(tipamt))

#6. 
# prompt user for original price
op = float(input("what's the OG price?:"))
# prompt for discount amount, divide by 100 for decimal 
dp = float(input("whats the discount percent amt?:")) / 100
def apply_discount(op, dp):
    # takes original price, calculates discount, and returns a new price
    np = op - (op * dp)
    return np
print(apply_discount(op, dp))

#7 
#prompt user for a list of numbers
strng = input("Input a list of numbers with commas")
def handle_commas(strng):
    # .replace function to replace every comma with no space
    new = strng.replace(",", '')
    return new
print(handle_commas(strng))

#8 
#prompts user for number grade, stores as an integer
grade = int(input("What's your number grade?:"))
def get_letter_grade(grade):
    #if/else loop to bin response, creates temp variable lg to store the letter equivalent grade
    if 100 >= grade >= 88:
        lg = 'A'
    elif 87 >= grade >= 80:
        lg = 'B'
    elif 79 >= grade >= 67:
        lg = 'C'
    elif 66 >= grade >= 60:
        lg = 'D'
    else:
        lg = 'F'
    return lg 
print(get_letter_grade(grade))

#9
print("question 9")
#prompts user for input, converts to a string
string = str(input("give me a sentence:"))
def remove_vowels(string):
    # creates a temporary variable to store known vowels
    vowels = 'aeiouAEIOU'
    # for loop that checks every element in the input string against the stored vowels variable
    for vowel in vowels: 
        # if located in vowels, it removes the element
        string = string.replace(vowel,'')
    return string
print(remove_vowels(string))

#10 
print("Question 10")
# prompts user for a string, converts it to a string
string = str(input("Gimme a string:"))
#creates a set of banned characters
nobueno = set("!@#$%^&*()+=-[]{}\/|?.<>,`~'")
def normalize_name(string):
    # converts all letters to lowercase
    string = string.lower()
    # removes trailing and leading whitespace
    string = string.strip()
    for x in string:
        # for loop checks every character in the string, replaces spaces with underscores and replaces any characters that match the nobueno set
        if x == ' ':
            string = string.replace(x,'_')
        elif x in nobueno:
            string = string.replace(x,'')      
    return string 
print(normalize_name(string))

#11.
# takes user input and converts them into a list
lisnum = (input("give me a list of numbers: ")).split()
# converts list elements from str type to integer
for x in range(0, len(lisnum)):
              lisnum[x] = int(lisnum[x])
def cumulative_sum(lisnum):
    # creates a working sum variable called total. Initial value is set to the first element of the input
    total = [lisnum[0]]
    # for loop that goes through the second all the way to the last element
    for x in lisnum[1:]:
        # takes the last element of the working sum variable
        previous_total = total[-1]
        # appends working sum variable to be a sum of the most recent element and the one before
        total.append(previous_total + x)
    return total
# returns a list of values that are self summing
print(cumulative_sum(lisnum))
print(type(lisnum))
print(lisnum)