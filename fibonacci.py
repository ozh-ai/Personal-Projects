n = eval(input("Input term:"))
if n < 1:
    print("Invalid input")
    n = eval(input("Input term:"))

fiblist = [0,1]
count = 2
if n == 1:
    print(fiblist[0])
elif n == 2:
    print(fiblist[1])
else:
    while count < n:
        fiblist.append(fiblist[-1]+fiblist[-2])
        fiblist.pop(0)
        count += 1
    print(fiblist[-1])
