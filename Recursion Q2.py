def read_add():
    number = input("Enter a real number(Blank to quit):")
    if number == "":
        return 0.0
    else:
        return float(number) + read_add()

def read_add_ite():
    total = 0.0
    while number != "":
        number = eval(input("Enter a real number(Blank to quit):"))
        total = total + float(number)
    print(total)
