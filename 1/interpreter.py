# get input
expression = input("expression: ")
# convert into variables
x, y, z = expression.split(" ")
# change type of variables to float
float_x = float(x)
float_z = float(z)
# calculate result
if y == "+":
    result = float_x + float_z
if y == "-":
    result = float_x - float_z
if y == "*":
    result = float_x * float_z
if y == "/":
    result = float_x / float_z
print(result)
