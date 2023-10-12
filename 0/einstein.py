#weight input
def mass():
    input_number = int(input("how much mass should i convert?"))
    joules = input_number * (300000000 ** 2)
    print(joules)
mass()