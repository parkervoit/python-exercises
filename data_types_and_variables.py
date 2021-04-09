# You ahve rented movies for your kids: little mermaid(3 days), brother bear(5 days), and hercules(1 day) at 3 dollars per day.
# how much is the total rental cost
print('Question 1')
lmd = 3
bbd = 5
hd = 1
total = (lmd*3) + (bbd*3) + (hd*3)
print(total)
## here's with list comprehension
movies = [3,5,1]
total2 = sum([n * 3 for n in movies])
print(total2)

# 2. companies pay you different rates per hour. Company A pays you 400/hr, B 380/hr, and C 350/hr.
# you worked 10 hrs for A, 6 for B, 4 for C. Whats your total paycheck?
print('Question 2')
ar = 400
br = 380 
cr = 350
at = 10
bt = 6
ct = 4
paycheck = (ar * at) + (br * bt) + (cr * ct)
print(paycheck)

#3.A student can be enrolled to a class only if the calss is not full and the schedule does not conflict with her current schedule
print('Question 3')
class_has_space = True  
schedule_clear = True
enroll_in_class = schedule_clear == True and class_has_space == True
print(enroll_in_class)

#4. a product offer can only be applied if people buy more than two items and offer has not expired.
print("Question 4")
print('Number of items in cart:')
quantity = int(input())
itemq = quantity > 2
print('is offer expired?(y/n):')
ovalid = input()
print('are you a member?(y/n):')
memb = input()
membchk = memb == 'y'
prodoff = (itemq == True or membchk == True) and ovalid != 'y' 
print(prodoff)

#5. create a variable that holds booleans to check to see if  a password is at least 5 chars and doesnt start/end in whitespace
# checks to see if the username is less than 20 chars and doest start or end with whitespace
# makes sure username and password are not the same
print('Question 5')
username = 'codeup'
password = 'notastrongpassword'
minpass = len(password) >= 5 # password must be longer than 5 chars
maxuse = len(username) <= 20 # username must be less than 20 chars
usepasscheck = username.lower() != password.lower() #checks to see if thyere equivalent
whtuse = username[0] != ' ' and username[-1] != ' ' # these lines check for whitespaces in user and pass
whtpass = password[0] != ' ' and password[-1] != ' '
wscheck = whtuse == True and whtpass == True
pswd = minpass == True and maxuse == True and usepasscheck == True and wscheck == True # 
print(pswd)
userpassvalid = {
    'passlen': minpass,
    'userlen': maxuse,
    'user_pass': usepasscheck,
    'whitespacechk': wscheck
}
print("Bool vals stored: " + userpassvalid)