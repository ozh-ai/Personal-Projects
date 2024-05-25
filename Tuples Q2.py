def sum_difference(n1,n2):
    add = float(n1) + float(n2)
    minus = float(n1) - float(n2)
    return (add,minus)

def main():
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")


    add,minus = sum_difference(num1,num2)
    print(add)
    print(minus)

main()
