import requests


class Currency:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class USD(Currency):
    def __init__(self):
        super().__init__("US Dollar", "USD")


class ILS(Currency):
    def __init__(self):
        super().__init__("Israeli New Shekel", "ILS")


class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = None

    def get_exchange_rates(self):
        # API endpoint to get the latest exchange rates
        endpoint = "https://api.exchangerate-api.com/v4/latest/USD"

        try:
            # Make a GET request to the API endpoint
            response = requests.get(endpoint)

            # Parse the response as JSON
            data = response.json()

            # Extract the exchange rates
            self.exchange_rates = data["rates"]

        except requests.exceptions.RequestException as e:
            # Handle any errors that occur during the request
            print("An error occurred:", str(e))
            return None

    def convert_currency(self, amount, from_currency, to_currency):
        if not self.exchange_rates:
            print("Exchange rates not available. Please try again later.")
            return None

        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            print("Invalid currency code(s).")
            return None

        from_rate = self.exchange_rates[from_currency]
        to_rate = self.exchange_rates[to_currency]

        converted_amount = amount * (to_rate / from_rate)
        return converted_amount


if __name__ == "__main__":
    converter = CurrencyConverter()
    converter.get_exchange_rates()

    while True:
        print("Currency Converter")
        print("1.Convert from USD to ILS")
        print("2.Convert from ILS to USD")

        choice = int(input("Enter your choice (1 or 2): "))
        if choice == 1:
            from_currency = "USD"
            to_currency = "ILS"
        elif choice == 2:
            from_currency = "ILS"
            to_currency = "USD"
        else:
            print("Invalid choice!")
            choice = int(input("Enter your choice (1 or 2): "))

        amount = float(input(f"Enter the amount in {from_currency}: "))

        converted_amount = converter.convert_currency(amount, from_currency, to_currency)

        if converted_amount is not None:
            print(f"{amount} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}.")

        restart = input("Do you want to convert again? (yes/no): ")
        if restart.lower() != "yes":
            break