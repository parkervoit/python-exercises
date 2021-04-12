#1.
#a
curday = input("what day of the week is it?:")
if curday == 'monday' or 'Monday':
    print("It is Monday! :)")
else:
    print("It's not Monday :(")
#b
curday = input("what day of the week is it?:")
if curday == 'saturday' or curday == 'sunday':
    print("It's the weekend!'")
else:
    print("It's not the weekend")
#c
hrs = 45
pay_rate = 10
paycheck = hrs * pay_rate

if hrs > 40:
    pay_rate2 = 1.5 * 10
    paycheck2 = ((hrs - 40) * pay_rate2) + (hrs * pay_rate)
    print(paycheck2)
else: 
    paycheck = hrs * pay_rate
    print(paycheck)
#2
#a.1-3
i = 5
while i <= 15 :
    print(i)
    i += 1
#a.4
i = 0
while i <= 100 :
    print(i)
    i += 1
#a.5
i = 100
while i >= -10 :
    print(i)
    i -= 5
#a.6
i = 2
while i < 1000000 :
    print(i)
    i = i ** 2
#a.7
i = 100
while i >= 5 :
    print(i)
    i -= 5
#b.1
x=int(input("choose a number:"))
i = 1
for i in range(11):
    print(x, 'x', i, '=', x * i)
#b.2
i = 1
for i in range(10) :
    print(str(i)*i)
    i += 1
#c
num = False
while num == False:
    n = input("Enter an odd number between 0 and 50:")
    if n.isdigit():
        n = int(n)
        if n > 0 and n < 50 and n % 2 != 0:
            break
        else:
            print("Invalid number")
    else:
        print("Invalid number")
        
print("The number to skip is:", n)
i = 1
for i in range(50):
    if i == n:
        print("Yikes, skipping this number", n)
        continue
    elif i % 2 != 0:
        print("Here is an odd number:", i)
#3
i = 1
for i in range(101):
    if i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz")
        i += 1
        continue
    elif i % 3 == 0 :
        print("fizz")
        i += 1 
    elif i % 5 == 0 :
        print("buzz")
        i =+ 1
    else :
        print(i)
        i += 1
#4
n = int(input("Input a number:"))
for i in range(1, n + 1):
    print (i, i ** 2, i ** 3)
con = input("continue?(y/n):")
while con == "y":
    n += 1
    print (n, n ** 2, n ** 3)
    con = input("continue?(y/n):")
#5
grade = int(input("What's your grade?:"))
if 100 >= grade >= 88:
    print(f"A {grade} is an A")
elif 87 >= grade >= 80:
    print(f"A {grade} is a B")
elif 79 >= grade >= 67:
    print(f"A {grade} is a C")
elif 66 >= grade >= 60:
    print(f"A {grade} is a D")
else:
    print(f"A {grade} is an F")
#6
books = [
    {'title' : 'GRE Prep', 
     'author' : 'kaplan', 
     'genre' : 'reference'},
    {'title' : 'Cloud Atlas'
     'author' : 'David Mitchell'
     'genre' : 'fantasy'},
    {'title' : 'The World\'s Religions'
     'author' : 'Huston Smith'
     'genre' : 'nonfiction'}
]
for x in books:
    [print(key, ': ', x[key]) for key in x)]
input_genre = input("What genre?:")
for x in books:
    if x['genre'] == input_genre:
        print(x['title'])