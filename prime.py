n = eval(input("Input term:"))
if n < 1:
    print("Invalid term")
    n = eval(input("Input term:"))
    
if n == 1:
    print(2)
else:
    num = 2 #1 and 0 are not prime
    count = 1
    while count < n:
        num += 1
        isprime = True
        for i in range(2,num):
            if (float(num/i)).is_integer() == True:
                isprime = False
                break
        if isprime == True:
            count += 1
            print(count, num)
    print(num)
            

