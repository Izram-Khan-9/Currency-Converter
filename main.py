import requests

def currency_converter():
            print('\n--Currency-Converter--')

            try:
                # base_currency: string like 'USD'
                # target_currency: string like 'EUR'
                # amount = total amount you want to exchange
                base_currency = input('\nEnter the base currency: ').upper()
                target_currency = input('Enter the target currency: ').upper()
                amount = float(input('Enter the amount: '))
                
                # Request live exchange rate from API
                url = f"https://open.er-api.com/v6/latest/{base_currency}"
                # Getting the URL using requests module
                response = requests.get(url)
                # Saving the data present in URL in a json file.
                data = response.json()
                
                # Check if API worked. status_code: 200 = success, 404 = network error and there are many more
                if response.status_code != 200 or data.get("result") != "success":
                    return "\nError: Unable to fetch exchange rates."

                # Check if target currency exists in data
                if target_currency not in data['rates']:
                    return f"\nInvalid currency code: {target_currency}"
                
                # Get the exchange rates
                rate = data['rates'][target_currency]

                # Calculate the converted amount
                converted_amount = amount * rate

                # Format and return the result
                print('\n')
                result = f"{amount} {base_currency} = {round(converted_amount, 2)} {target_currency}"
                return result

            # If user enters an invalid amount
            except ValueError:
                return "\nError: Please enter a valid numeric amount."

            # If status_code == 404
            except requests.exceptions.RequestException:
                return "\nNetwork error: Unable to fetch live data."

            # Handling all possible error
            except Exception as e:
                return f"\nError: {str(e)}"
            
print(currency_converter())

#____________________________________________________________________________________________________
# Created by: Izram Khan
# Date created: 9-Nov-2025 (Sunday) (3:28 pm)
