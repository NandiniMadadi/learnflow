import requests

# Define the API URL and your API key (replace 'YOUR_API_KEY' with your actual API key)
EXCHANGE_RATE_API_URL = "https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/"

def fetch_exchange_rate(base_currency, target_currency):
    response = requests.get(EXCHANGE_RATE_API_URL + base_currency)
    if response.status_code != 200:
        raise Exception("Error fetching exchange rates. Please check the API URL and your API key.")
    
    try:
        data = response.json()
    except ValueError:
        raise Exception("Invalid response format.")
    
    if 'conversion_rates' not in data:
        raise Exception("Invalid response from API. Please check the API URL and your API key.")
    
    conversion_rates = data['conversion_rates']
    if target_currency not in conversion_rates:
        raise Exception(f"Conversion rate for {target_currency} not found.")
    
    return conversion_rates[target_currency]

def convert_currency():
    print("Welcome to the Currency Converter!")

    try:
        amount_to_convert = float(input("Enter the amount: "))
        base_currency = input("Enter the source currency (e.g., USD, EUR): ").upper()
        target_currency = input("Enter the target currency (e.g., USD, EUR): ").upper()
        
        exchange_rate = fetch_exchange_rate(base_currency, target_currency)
        converted_amount = amount_to_convert * exchange_rate
        
        print(f"{amount_to_convert} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
    
    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    convert_currency()
