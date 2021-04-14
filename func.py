def is_two(x):
    if x == "2" or x == 2:
        return True
    else :
        return False  

def is_vowel(value):
    if value in ('a','e','i','o','u', 'A','E','I','O','U'):
        return True
    else:
        return False

def is_consonant(value):
    if is_vowel == False:
        return True
    else:
        return False

def cap_word(wrd):
    if is_consonant(wrd[0]) == True:
        #if true, word is capitalized
        return wrd.capitalize()
    else:
        return wrd

def calculate_tip(tipamt, bill):
    total = (tipamt * bill) + bill
    return total 

def apply_discount(op, dp):
    np = op - (op * dp)
    return np

def handle_commas(strng):
    new = strng.replace(",", '')
    return new

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

def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    for vowel in vowels: 
        string = string.replace(vowel,'')
    return string

def normalize_name(string):
    nobueno = set("!@#$%^&*()+=-[]{}\/|?.<>,`~'")
    string = string.lower()
    string = string.strip()
    for x in string:
        if x == ' ':
            string = string.replace(x,'_')
        elif x in nobueno:
            string = string.replace(x,'')      
    return string 

def cumulative_sum(lisnum):
    lisnum = lisnum.split()
    total = [lisnum[0]]
    for x in lisnum[1:]:
        previous_total = total[-1]
        total.append(previous_total + x)
    return total

def twelveto24(time):
    if time[-2:] == "AM" and time[:2] == "12":
        return "00" + time[2:-2] 
    elif time[-2:] == "AM": 
        return time[:-2]
    else:
        return str(int(time[:2]) + 12) + time[2:4] 

def monstrfloat(string):
    nobueno = {'$': '', ',': '', ''}
    for key, value in nobueno.items():
        string = string.replace(key, value)
    return float(string)

