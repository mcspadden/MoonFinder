# MoonFinder by McSpadden
# Copyright (c) 2018 McSpadden
# View https://github.com/mcspadden/MoonFinder/blob/master/README.md for license details

import requests

print('MoonFinder by McSpadden')
print('Please wait while your lambo exceeds the escape velocity of Earth...')

cryptos = requests.get("http://coincap.io/coins")  # getting current cryptos from coincap.io
cryptos = cryptos.json()  # making the request.get in python var

# every fiat currency, this is needed because cryptocompare does not have fiats within their all coinlist
fiat = ["AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND",
        "BOB","BRL","BSD","BTN","BWP","BYN","BZD","CAD","CDF","CHF","CLP","CNY","COP","CRC","CUC","CUP","CVE","CZK",
        "DJF","DKK","DOP","DZD","EGP","ERN","ETB","EUR","FJD","FKP","GBP","GEL","GGP","GHS","GIP","GMD","GNF","GTQ",
        "GYD","HKD","HNL","HRK","HTG","HUF","IDR","ILS","IMP","INR","IQD","IRR","ISK","JEP","JMD","JOD","JPY","KES",
        "KGS","KHR","KMF","KPW","KRW","KWD","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LYD","MAD","MDL","MGA","MKD",
        "MMK","MNT","MOP","MRU","MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","OMR","PAB",
        "PEN","PGK","PHP","PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF","SAR","SBD","SCR","SDG","SEK","SGD","SHP",
        "SLL","SOS","SPL","SRD","STN","SVC","SYP","SZL","THB","TJS","TMT","TND","TOP","TRY","TTD","TVD","TWD","TZS",
        "UAH","UGX","USD","UYU","UZS","VEF","VND","VUV","WST","XAF","XCD","XDR","XOF","XPF","YER","ZAR","ZMW","ZWD"]

cryptocurrencies = requests.get("https://min-api.cryptocompare.com/data/all/coinlist")  # list of exchangeable currency
cryptocurrencies = cryptocurrencies.json() # making the request.get in python var
cryptocurrencies = list(cryptocurrencies["Data"])  # selecting the data header which has the currency + making it a list
currencies = cryptocurrencies + fiat # adding in fiat list to supported cryptos

# line below sets the default currency
default = input('What currency would you like to view the results in? (Type the symbol like BTC or USD) ').upper()
# Let user input their crypto aka Seat Selector
if default in currencies:  # if input was a supported currency, continue below
    print(str(default) + " selected as default currency.")
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

    currency = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms={default}")  # conversion
    currency = currency.json()  # making the request.get python format
    currency = currency[f"{default}"] # selecting the exchange rate

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
            return ("\n" + str(coinNames[0]) + ' is your mooncoin.' + "\n" +
                    "Price Today in " + default + ": " + str(
                        A2 * currency) + "\n" +  # Creates var for Coin A's difference in a %
                    "Price 365 Days Ago in " + default + ": " + str(A1 * currency) +  # remove after testing is finished
                    "\n" + str(coinNames[0]) + " gains: " + str(
                        round(AD * int("100"))) + '%')  # Prints the % for Coin A
        if BD > AD and BD > CD:  # Coin B is mooncoin
            return ("\n" + str(coinNames[1]) + ' is your mooncoin.' + "\n" +
                    "Price Today in " + default + ": " + str(
                        B2 * currency) + "\n" +  # Creates var for Coin B's difference in a %
                    "Price 365 Days Ago in " + default + ": " + str(B1 * currency) +  # remove after testing is finished
                    "\n" + str(coinNames[1]) + " gains: " + str(
                        round(BD * int("100"))) + '%')  # Prints the % for Coin B
        if CD > AD and CD > BD:  # Coin C is mooncoin
            return ("\n" + str(coinNames[2]) + ' is your mooncoin.' + "\n" +
                    "Price Today in " + default + ": " + str(
                        C2 * currency) + "\n" +  # Creates var for Coin C's difference in a %
                    "Price 365 Days Ago in " + default + ": " + str(C1 * currency) +  # remove after testing is finished
                    "\n" + str(coinNames[2]) + " gains: " + str(
                        round(CD * int("100"))) + '%')  # Prints the % for Coin C

    print(winner())
else:  # if input was not a supported currency
    print('Not a supported currency at this time. Please try another currency.')