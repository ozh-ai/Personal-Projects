def findDivisors(n1,n2):
    divisorlist = []
    smaller = min(n1,n2)
    for i in range(1, smaller + 1):
        if n1%i==0 and n2%i==0:
            divisorlist.append(i)
    return divisorlist
    

def main():
    num1 = eval(input("Type in first number:"))
    num2 = eval(input("Type in second number"))
    divisors = findDivisors(num1,num2)
    print(divisors)

main()
    
