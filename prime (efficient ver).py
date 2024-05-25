n = eval(input("Input term:"))
while n < 1:
    print("Invalid term")
    n = eval(input("Input term:"))

primelist = [2]
if n > 1:
    num = 3 #1st term is 2
    while len(primelist) < n:
        isprime = True
        for i in range(len(primelist)):
            if (float(num/primelist[i])).is_integer() == True:
                isprime = False
                break
        if isprime == True:
            primelist.append(num)
            ## print(len(primelist), primelist[-1])
        num += 1
print(primelist[-1])
