# MoonFinder by McSpadden
# Copyright (c) 2018 McSpadden
# View https://github.com/mcspadden/MoonFinder/blob/master/README.md for license details

import requests

print('MoonFinder by McSpadden')
print('Please wait while your lambo exceeds the escape velocity of Earth...')

cryptos = requests.get("http://coincap.io/coins") # getting current cryptos from coincap
cryptos = cryptos.json() # making the request.get python format

# Supported currencies
answers = {"BTC": "\n BTC selected as default currency.", \
           "ETH": "\n ETH selected as default currency.", \
           "EUR": "\n EUR selected as default currency.", \
           "USD": "\n USD selected as default currency.", \
           "LTC": "\n LTC selected as default currency.", \
           "ZEC": "\n ZEC selected as default currency.", \
           }

# Let user input their crypto aka Seat Selector
ans = True
while ans: # line below print's the symbol for default currencies
    print('''\n
    BTC | ETH | EUR | USD | LTC | ZEC
    ''')
    ans = input('What currency would you like to view the results in?').upper() # setting ans and .upper() makes input all uppercase
    if ans in answers: # if input was a supported currency, continue below
        print(answers[ans])

        # start of seat selector
        coinNames = []
        print('\n\nSeat Selector(Crypto Selector)')
        while True:
            print('\n Enter the symbol of a crypto' + \
                  ' (Or press Enter once you have added all you desire.):')
            name = input().upper()
            if name in cryptos: # verifying it is a real crypto
                coinNames = coinNames + [name] # list concatenation
                continue
            elif name == '': # If user hits enter then it stops the input session
                break
            else: # in case it is not a crypto or coincap does not support it yet
                print("Sorry, that seat(crypto) does not exist.")
        print('The selected cryptos are:')
        for name in coinNames:
            print(' ' + name)
        break
    else: # if input was not a supported currency
        print('Not a supported currency at this time. Please try another currency.')
