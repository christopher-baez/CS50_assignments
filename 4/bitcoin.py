import sys
import requests

# import the data from http
r_updated = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

def bit():
    while True:
        try:
            # turned json to dictionary
            r = r_updated.json()
            # turned us price into float
            cost = float(r['bpi']['USD']['rate'].replace(',', ''))
            # return current cost
            return cost
        except requests.RequestException:
            continue


def main():
    # Check if the command line argument is provided
    if len(sys.argv) != 2:
        sys.exit('missing command-line argument')

    try:
        # Convert the argument to float
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit('Command-line argument is not a valid number')

    # Get the current Bitcoin price
    current_price = bit()

    # Calculate total cost
    total_cost = num_bitcoins * current_price

    # Format and output the total cost
    print(f"${total_cost:,.4f} USD")


if __name__ == "__main__":
    main()