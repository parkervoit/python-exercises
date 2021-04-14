#1 
import func 

#1.a
func.is_vowel('a')

#1.b
from func import calculate_tip
print(calculate_tip(.2,100))

#1.c
from func import get_letter_grade as letter
letter(90) 
#2
import itertools as it
al = 'abc'
n = '123'
x = it.product(al, n)
num = 0
for i in list(x):
    num += 1
    # 9 combinations found

comb = 'abcd'
x = it.combinations(comb, 2)
num = 0
for i in list(x):
    num += 1
    print(num)
    #6 combinations of abcd

perm = 'abcd'
x = it.permutations(perm, 2)
num = 0
for i in list(x):
    num += 1
    print(num)

    # 12 permutations

#3 json exercises
# total users
def total_users(x):
    ids = [x["_id"] for x in dc]
    return(len(ids))
print(total_users(dc))
    #19

# total active users
def total_users(value):
    ids = [x["_id"] for x in dc if x['isActive'] == True]
    return(len(ids))
print(total_users(dc))
#9 active

#total inactive users
def total_users(value):
    ids = [x["_id"] for x in dc if x['isActive'] == False]
    return(len(ids))
print(total_users(dc))
    #10 inactive

# grand total balances for all users
def total_balance(value):
    bal = [x['balance'] for x in dc]
    bal2 = [x.replace(",", "") for x in bal]
    bal3 = [x.replace("$", "") for x in bal2]
    bal4 = [float(x) for x in bal3]
    return(sum(bal4))
print(total_balance(dc))
    # 52667.02

# average balance per user
def average_balance(value):
    return total_balance(dc) / total_users(dc)
print(average_balance(dc))

    #2771.9484210526316

# person with highest balance
def max_person(value):
    bal = [x['balance'] for x in dc]
    bal_user = max(bal)
    user = [x['name'] for x in dc if x['balance'] == bal_user ]
    return user
print(max_person(dc))
    # fay hammond 

# person with the lowest balance 
def min_person(value):
    bal = [x['balance'] for x in dc]
    bal_user = min(bal)
    user = [x['name'] for x in dc if x['balance'] == bal_user ]
    return user
print(min_person(dc))
    # Avery Flynn

# most common fruits
def fruit_count(value):
    common_fruit = [x['favoriteFruit'] for x in dc]
    fruit_counts = {}
    for x in common_fruit:
        if x not in fruit_counts.keys():
            fruit_counts[x] = 1
        else:
            fruit_counts[x] += 1
    return fruit_counts
print(fruit_count(dc))

print(max(fruit_count(dc)))

    # max is strawberry

#least favorite fruit
print(min(fruit_count(dc)))

    # min is apple


# find the amount of unread messages people have
msg_list = []
for x in dc:
    digs = []
    for x in x['greeting']:
        if x.isdigit():
            digs.append(x)
    digstr = ''.join(digs)
    digint = int(digstr)
    msg_list.append(digint)
print(msg_list)

