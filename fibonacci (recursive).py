def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = eval(input("Input term:"))
if n < 1:
    print("Invalid term")
    n = eval(input("Input term:"))
print(fibonacci(n))
