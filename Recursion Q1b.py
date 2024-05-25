def itfibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    n0 = 0
    n1 = 1
    for i in range(2,n+1):
        n2 = n0 + n1 #solve n2 = 0+1 = 1
        n0 = n1 #Bring n0 up by 1 placing
        n1 = n2 #bring n1 up by 1 placing
    return n2

def main():
    n = eval(input("What is n?"))
    print(itfibonacci(n))
main()
