# MoonFinder by McSpadden
# Copyright (c) 2018 McSpadden
# View https://github.com/mcspadden/MoonFinder/blob/master/README.md for license details

import requests

print('MoonFinder by McSpadden')
print('Please wait while your lambo exceeds the escape velocity of Earth...')

cryptos = requests.get("http://coincap.io/coins")  # getting current cryptos from coincap.io
cryptos = cryptos.json()  # making the request.get in python var

currencies  = requests.get("https://min-api.cryptocompare.com/data/all/coinlist")  # list of exchangable currencies
currencies = currencies.json() # making the request.get in python var
currencies = currencies["Data"]  # selecting the data header which has the currency list

# Let user input their crypto aka Seat Selector
ans = True
while ans:  # line below print's the symbol for default currencies
    ans = input('What currency would you like to view the results in?'
                '\n(Type the symbol)'
                '\nNote: To select bitcoin you would type btc or '
                'to select the US dollar you would type usd (case does not matter)').upper()  # setting default currency
    if ans in currencies:  # if input was a supported currency, continue below
        print(str(ans) + " selected as default currency.")
        # start of seat selector
        coinNames = []
        print('\n\nSeat Selector(Crypto Selector)')
        while True:
            print('\n Enter a crypto symbol')
            name = input().upper()
            if name in cryptos:  # verifying it is a real crypto
                coinNames = coinNames + [name] # list connotation
                break
            else:  # in case it is not a crypto or coincap does not support it yet
                print("Sorry, that seat(crypto) does not exist.")
        while True:
            print('\n Enter your second crypto symbol')
            name = input().upper()
            if name in cryptos:  # verifying it is a real crypto
                coinNames = coinNames + [name]  # list connotation
                break
            else:  # in case it is not a crypto or coincap does not support it yet
                print("Sorry, that seat(crypto) does not exist.")
        while True:
            print('\n Enter your last crypto symbol')
            name = input().upper()
            if name in cryptos:  # verifying it is a real crypto
                coinNames = coinNames + [name]  # list connotation
                break
            else:  # in case it is not a crypto or coincap does not support it yet
                print("Sorry, that seat(crypto) does not exist.")
            break
        print('Please wait while your first class seat is being prepared.')

        currency = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms={ans}")  # conversion
        currency = currency.json()  # making the request.get python format
        currency = currency[f"{ans}"] # selecting the exchange rate

        # Start of data requests
        # First crypto inputted = A1
        A1 = requests.get(f"http://coincap.io/history/{coinNames[0]}")  # Request to get coin's history
        A1 = A1.json()  # Place JSON data as python var
        A1 = (A1["price"][0][1]) # Select the coins price on day 365
        A2 = requests.get(f"http://coincap.io/page/{coinNames[0]}")  # Coin A still: Request to get coins data for today
        A2 = A2.json()  # Place JSON data as python var
        A2 = (A2["price_usd"])  # Select the coins price in USD for today
        AD = ((A2 - A1) / A1)  # Formula: ((Price Today - Price 365 days ago) ÷ (Price 365 days ago))

        # Second crypto inputted = B1
        B1 = requests.get(f"http://coincap.io/history/{coinNames[1]}")  # Request to get coin's history
        B1 = B1.json()  # Place JSON data as python var
        B1 = (B1["price"][0][1])  # Select the coins price on day 365
        B2 = requests.get(f"http://coincap.io/page/{coinNames[1]}")  # Coin A still: Request to get coins data for today
        B2 = B2.json()  # Place JSON data as python var
        B2 = (B2["price_usd"])  # Select the coins price in USD for today
        BD = ((B2 - B1) / B1)  # Formula: ((Price Today - Price 365 days ago) ÷ (Price 365 days ago))

        # Third crypto inputted = C1
        C1 = requests.get(f"http://coincap.io/history/{coinNames[2]}")  # Request to get coin's history
        C1 = C1.json()  # Place JSON data as python var
        C1 = (C1["price"][0][1])  # Select the coins price on day 365
        C2 = requests.get(f"http://coincap.io/page/{coinNames[2]}")  # Coin c still: Request to get coins data for today
        C2 = C2.json()  # Place JSON data as python var
        C2 = (C2["price_usd"])  # Select the coins price in USD for today
        CD = ((C2 - C1) / C1)  # Formula: ((Price Today - Price 365 days ago) ÷ (Price 365 days ago))


        def winner():
            if AD > BD and AD > CD:  # Coin A is mooncoin
                return (str(coinNames[0]) + ' is your mooncoin.' + "\n" +
                        "Price Today in " + ans + ": " + str(
                            A2 * currency) + "\n" +  # Creates var for Coin A's difference in a %
                        "Price 365 Days Ago in " + ans + ": " + str(A1 * currency) +  # remove after testing is finished
                        "\n" + str(coinNames[0]) + " gains: " + str(
                            round(AD * int("100"))) + '%')  # Prints the % for Coin A
            if BD > AD and BD > CD:  # Coin B is mooncoin
                return (str(coinNames[1]) + ' is your mooncoin.' + "\n" +
                        "Price Today in " + ans + ": " + str(
                            B2 * currency) + "\n" +  # Creates var for Coin B's difference in a %
                        "Price 365 Days Ago in " + ans + ": " + str(B1 * currency) +  # remove after testing is finished
                        "\n" + str(coinNames[1]) + " gains: " + str(
                            round(BD * int("100"))) + '%')  # Prints the % for Coin B
            if CD > AD and CD > BD:  # Coin C is mooncoin
                return (str(coinNames[2]) + ' is your mooncoin.' + "\n" +
                        "Price Today in " + ans + ": " + str(
                            C2 * currency) + "\n" +  # Creates var for Coin C's difference in a %
                        "Price 365 Days Ago in " + ans + ": " + str(C1 * currency) +  # remove after testing is finished
                        "\n" + str(coinNames[2]) + " gains: " + str(
                            round(CD * int("100"))) + '%')  # Prints the % for Coin C

        print(winner())
        break  # stops the loop
else:  # if input was not a supported currency
    print('Not a supported currency at this time. Please try another currency.')
