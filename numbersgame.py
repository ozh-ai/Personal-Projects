def lower(num):
    subtract = numlist[random.randint(0,9)]
    print("lower", str(subtract))
    num = num - subtract
    return num

def higher(num):
    add = numlist[random.randint(0,9)]
    print("higher", str(add))
    num = num + add
    return num

def traceback(num):
    if choice == 12:
        print("traceback 1")
        num = tblist[-2]
    if choice == 13:
        print("traceback 2")
        num = tblist[-3]        
    if choice == 14:
        print("traceback 3")
        num = tblist[-4]
    return num

def hybrid(num):
    if choice == 15: #lower lower
        num1 = numlist[random.randint(0,9)]
        num2 = numlist[random.randint(0,9)]
        print("lower", str(num1)," lower",str(num2))
        num = (num - num1) - num2    

    if choice == 16: #lower higher
        num1 = numlist[random.randint(0,9)]
        num2 = numlist[random.randint(0,9)]
        priority = random.randint(1,2) #lower or higher is stated first?
        if priority == 1:
            print("lower", str(num1)," higher",str(num2))
            num = (num - num1) + num2
        else:
            print("higher", str(num1)," lower",str(num2))
            num = (num + num1) - num2
    
    if choice == 17: #higher higher
        num1 = numlist[random.randint(0,9)]
        num2 = numlist[random.randint(0,9)]
        print("higher", str(num1)," higher",str(num2))
        num = (num + num1) + num2
    
    if choice == 18: #lower traceback
        option = random.randint(1,3)
        if option == 1:
            print("lower traceback 1")
            num = num - tblist[-2]
        if option == 2:
            print("lower traceback 2")
            num = num - tblist[-3]
        if option == 3:
            print("lower traceback 3")
            num = num - tblist[-4]

    if choice == 19: #higher traceback
        option = random.randint(1,3)
        if option == 1:
            print("higher traceback 1")
            num = num + tblist[-2]
        if option == 2:
            print("higher traceback 2")
            num = num + tblist[-3]
        if option == 3:
            print("higher traceback 3")
            num = num + tblist[-4]

    return num

def flip(num):
    print("flip")
    num = 0 - num
    return num

def multiply(num):
    num1 = random.randint(2,15)
    num2 = random.randint(2,15)
    if choice==20 or choice==21: #lower
        print("lower multiply",num1,num2)
        num = num - (num1*num2)
    if choice==22 or choice==23: #higher
        print("higher multiply",num1,num2)
        num = num + (num1*num2)
    return num

def constant(num,a,b,c):
    if random.randint(1,2) == 1: #lower
        if choice == 24:
            print("lower a")
            num = num - a
        if choice == 25:
            print("lower b")
            num = num - b
        if choice == 26:
            print("lower c")
            num = num - c
    else: #higher
        if choice == 24:
            print("higher a")
            num = num + a
        if choice == 25:
            print("higher b")
            num = num + b
        if choice == 26:
            print("higher c")
            num = num + c
    return num

def prime(num):
    if choice == 27: #lower
        primeNo = random.randint(1,10)
        print("lower prime",primeNo)
        num = num - primelist[primeNo-1]

    if choice == 28: #higher
        primeNo = random.randint(1,10)
        print("higher prime",primeNo)
        num = num + primelist[primeNo-1]
    return num

def fibonacci(num):
    if choice == 29: #lower
        fibNo = random.randint(1,12)
        print("lower fibonacci",fibNo)
        num = num - fiblist[fibNo-1]

    if choice == 30: #higher
        fibNo = random.randint(1,12)
        print("higher fibonacci",fibNo)
        num = num + fiblist[fibNo-1]
    return num

def power(num):
    if choice == 31: #lower
        num1 = random.randint(0,10)
        print("lower 2 power",num1)
        num = num - (2**num1)

    if choice == 32: #higher
        num1 = random.randint(0,10)
        print("higher 2 power",num1)
        num = num + (2**num1)
    return num

def square(num):
    if choice == 33: #lower
        num1 = random.randint(1,20)
        print("lower",num1,"square")
        num = num - (num1**2)

    if choice == 34: #higher
        num1 = random.randint(1,20)
        print("higher",num1,"square")
        num = num + (num1**2)
    return num
    
import random
from datetime import datetime
num = random.randint(200,800)
numlist = [1,2,3,4,5,6,7,8,9,10]
tblist = []
tblist.append(num)
primelist = [2,3,5,7,11,13,17,19,23,29]
fiblist = [0,1,1,2,3,5,8,13,21,34,55,89]
count = 0
ending = 0

input("Press enter to start:")
print()
start = datetime.now()
print(num)
end = False
while end == False:
    guess = int(input())
    if guess!=num:
        ending = 1
        end = True
    else:
        count += 1

        if count == 30:
            a = random.randint(1,99)
            b = random.randint(1,99)            
            c = random.randint(1,99)
            print("a =",a)
            print("b =",b)
            print("c =",c)
        elif count>30:
            if random.randint(1,10)==1:
                a = random.randint(1,99)
                print("a =",a)
            if random.randint(1,10)==1:
                b = random.randint(1,99)
                print("b =",b)
            if random.randint(1,10)==1:
                c = random.randint(1,99)
                print("c =",c)

        if count>50: #verify
            if random.randint(1,10)==1:
                if num >= 0:
                    num1 = random.randint(0,num)
                else:
                    num1 = random.randint(num,-1)
                num2 = num - num1

                if random.randint(1,2)==1: #True
                    print("=",num1,"+",num2,"? (T/F)")
                    guess = input()
                    if guess == 'T':
                        count += 1
                    else:
                        ending = 2
                        end = True
                        break
                else: #False
                    if random.randint(1,2)==1: #change the 1st digit placing
                        if random.randint(1,2)==1: #minus
                            num2 -= 1
                        else: #plus
                            num2 += 1
                    else: #change the 10th digit placing
                        if random.randint(1,2)==1: #minus
                            num2 -= 10
                        else: #plus
                            num2 += 10
                    print("=",num1,"+",num2,"? (T/F)")
                    guess = input()
                    if guess == 'F':
                        count += 1
                    else:
                        ending = 3
                        end = True
                        break

        if count > 70:
            choice = random.randint(14,34)
        elif count > 50:
            choice = random.randint(0,34)
        elif count > 40:
            choice = random.randint(0,30)
        elif count > 30:
            choice = random.randint(0,26)
        elif count > 25:
            choice = random.randint(0,23)
        elif count > 20:
            choice = random.randint(0,19)
        elif count > 15:
            choice = random.randint(0,16)
        elif count > 10:
            choice = random.randint(1,16)
        elif count > 5:
            choice = random.randint(1,14)
        else:
            choice = random.randint(1,11)

        if choice == 0:
            num = flip(num)
        if choice == 6:
            print("stay")
        if (choice < 6) and (choice > 0):
            num = lower(num)
        if (choice > 6) and (choice < 12):
            num = higher(num)
        if (choice > 11) and (choice < 15):
            num = traceback(num)
        if (choice > 14) and (choice < 20):
            num = hybrid(num)
        if (choice > 19) and (choice < 24):
            num = multiply(num)
        if (choice > 23) and (choice < 27):
            num = constant(num,a,b,c)
        if (choice==27) or (choice==28):
            num = prime(num)
        if (choice==29) or (choice==30):
            num = fibonacci(num)
        if (choice==31) or (choice==32):
            num = power(num)
        if (choice==33) or (choice==34):
            num = square(num)
            
    tblist.append(num)

    time = datetime.now() - start
    time = str(time)
    seconds = int(time[5:7])
    mins = int(time[2:4])
    hrs = int(time[0])
    mins = mins + (60*hrs)
    seconds = seconds + (60*mins)
    if seconds > 180: #time limit is 3 mins
        end = True
    
print()
print("game ended")
if ending==1:
    print("Correct answer is", num)
elif ending==2:
    print("Correct answer is True")
elif ending==3:
    print("Correct answer is False")
print("Points earned:",str(count))

##  round 1-5: lower higher stay
##  round 6-10: + traceback
##  round 11-15: + hybrid(lower higher)
##  round 16-20: + flip
##  round 21-25: + hybrid(lower higher traceback)
##  round 26-30: + multiply
##  round 31-40: + constants (a b c)
##  round 40-50: + prime fibonacci
##  round >50: + 2power square verify

##  HS: 65

            
        
