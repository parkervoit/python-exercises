#1. 
print("Question 1")
x = input("input 2, please")
def is_two(x):
    if x == "2" or x == 2:
        return True
    else :
        return False  
print(is_two(x))
 
#2
print("Question 2")
value = input("input a string:")
def is_vowel(value):
    if value in ('a','e','i','o','u', 'A','E','I','O','U'):
        return True
    else:
        return False
print(is_vowel(value))

#3
print("Question 3")
value = input("input a string:")
def is_consonant(value):
    if is_vowel == False:
        return True
    else:
        return False
print(is_consonant(value))
#4. 
print("Question 4")
wrd = input("gimme a word:")
def cap_word(wrd):
    if is_consonant(wrd[0]) == True:
        return wrd.capitalize()
    else:
        return wrd
print(cap_word(wrd))
#5. 
tipamt = float(input("input your tip percentage: ")) / 100 
bill= float(input("what's your total bill:"))
def calculate_tip(tipamt):
    total = (tipamt * bill) + bill
    return total 
print(calculate_tip(tipamt))
#6. 
op = float(input("what's the OG price?:"))
dp = float(input("whats the discount percent amt?:")) / 100
def apply_discount(op, dp):
    np = op - (op * dp)
    return np
print(apply_discount(op, dp))
#7 
strng = input("Input a list of numbers with commas")
def handle_commas(strng):
    new = strng.replace(",", '')
    return new
print(handle_commas(strng))
#8 
grade = int(input("What's your grade?:"))
def get_letter_grade(grade):
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
string = str(input("give me a sentence:"))
def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    for vowel in vowels: 
        string = string.replace(vowel,'')
    return string
print(remove_vowels(string))
#10 
print("Question 10")
string = str(input("Gimme a string:"))
nobueno = set("!@#$%^&*()+=-[]{}\/|?.<>,`~'")
def normalize_name(string):
    string = string.lower()
    string = string.strip()
    for x in string:
        if x == ' ':
            string = string.replace(x,'_')
        elif x in nobueno:
            string = string.replace(x,'')      
    return string 
print(normalize_name(string))
#11.
lisnum = (input("give me a list of numbers: ")).split()
for x in range(0, len(lisnum)):
              lisnum[x] = int(lisnum[x])
def cumulative_sum(lisnum):
    total = [lisnum[0]]
    for x in lisnum[1:]:
        previous_total = total[-1]
        total.append(previous_total + x)
    return total
print(cumulative_sum(lisnum))
print(type(lisnum))
print(lisnum)