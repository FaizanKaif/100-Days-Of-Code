def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations = {"+" : add,
"-" : sub,
"*" : mul,
"/" : div
}

def calculator():
    should_accumulate = True
    n1 = int(input("what is your first number\n"))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        n2 = int(input("what is your second nummber\n"))
        answer = operations[operation_symbol](n1,n2)
        print (f"{n1} {operation_symbol} {n2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to stop calculator")

        if choice == "y":
            n1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()