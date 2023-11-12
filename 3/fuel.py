# define new function for
def gas():
    while True:
        try:
            # get the input
            gas_fraction_input = input('Fraction: ')
            # split fraction to different variables
            x, y = gas_fraction_input.split('/')
            # divide the numbers
            gas_fraction = float(x) / float(y)
            # infinite loop to output % or E or F

            if gas_fraction > 0.99:
                return "F"
            elif gas_fraction < 0.01:
                return 'E'
            else:
                return f'{round(gas_fraction * 100)}%'
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
print(gas())
