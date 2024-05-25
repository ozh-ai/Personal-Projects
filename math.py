def math():
    print("")
    level = input("Choose the level of difficulty (1,2,3,4):")
    import random
    if level == "1":
        num1 = random.randint(2,20)
        num2 = random.randint(2,20)
        ans = num1*num2
        reply = eval(input("What is {} x {} ?".format(num1,num2)))
        if reply == ans:
            print("CORRECT!")
        else:
            print("INCORRECT! Answer is ", ans)
    elif level == "2":
        num1 = random.randint(11,99)
        num2 = random.randint(2,20)
        ans = num1*num2
        reply = eval(input("What is {} x {} ?".format(num1,num2)))
        if reply == ans:
            print("CORRECT!")
        else:
            print("INCORRECT! Answer is ", ans)
    elif level == "3":
        num1 = random.randint(11,99)
        num2 = random.randint(11,99)
        ans = num1*num2
        reply = eval(input("What is {} x {} ?".format(num1,num2)))
        if reply == ans:
            print("CORRECT!")
        else:
            print("INCORRECT! Answer is ", ans)
    elif level == "4":
        ans = random.randint(11,99)
        num1 = ans*ans
        reply = eval(input("What is the square root of {} ?".format(num1,)))
        if reply == ans:
            print("CORRECT!")
        else:
            print("INCORRECT! Answer is ", ans)

    else:
        print("INVALID DIFFICULTY")
    math()

print("MATH GAME :)")
math()
    
    
