import sys
import requests

def main():
    try:
        # Get the number of Bitcoins from the command-line argument
        bitcoin = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Invalid command-line argument")

    #CoinCap API key
    api_key = "fd455bf18472c61c0e78bab6b617af10a94536d616d14bc95beebeaefeb662cb"
    url = f"https://rest.coincap.io/v3/assets/bitcoin"

    try:
        # Make the API request with headers
        response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()

        # Extract the current price of Bitcoin
        price = float(data["data"]["priceUsd"])

        # Calculate total cost
        total_cost = bitcoin * price

        # Print the result formatted with commas and 4 decimal places
        print(f"${total_cost:,.4f}")

    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")

if __name__ == "__main__":
    main()
