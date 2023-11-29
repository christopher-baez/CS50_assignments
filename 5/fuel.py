def convert(fraction):
    try:
        x, y = map(float, fraction.split('/'))
        return x / y
    except ZeroDivisionError:
        return None
    except ValueError:
        return None

def gauge(percentage):
    if percentage is None:
        return None
    elif percentage > 0.99:
        return "F"
    elif percentage < 0.01:
        return "E"
    else:
        return f'{round(percentage * 100)}%'

def main():
    while True:
        gas_fraction_input = input('Fraction: ')
        percentage = convert(gas_fraction_input)
        result = gauge(percentage)
        if result is not None:
            print(result)
            break

if __name__ == "__main__":
    main()
