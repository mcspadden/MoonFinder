# RedPlanetLabs
# McSpadden


print('MoonFinder by McSpadden')
print('Please wait while exceed the escape velocity of Earth...')
import time
time.sleep(1)

# Supported currencies
answers = {"BTC": "\n BTC selected as default currency.", \
           "ETH": "\n ETH selected as default currency.", \
           "LTC": "\n LTC selected as default currency.", \
           "USD": "\n USD selected as default currency.", \
           "GBP": "\n GBP selected as default currency.", \
           }

# Let user input their currency
ans = True
while ans:
    print('''\n
    BTC | ETH | LTC | USD | GBP
    ''')
    ans=input('What currency would you like to use?').upper() #setting ans and .upper() makes input all uppercase
    if ans in answers:
        print(answers[ans])

        coinNames = []
        print('\n\nSeat Selector(Coin Selector)')
        while True:
            print('\n Enter the name of a coin' + \
                  ' (Or press Enter once you have added all you desire.):')
            name = input()
            if name == '':
                break
            coinNames = coinNames + [name]  # list concatenation
        print('The coin names are:')
        for name in coinNames:
            print(' ' + name)
        break
    else:
        print('Not a supported currency at this time. Please verify the case matches and try again.')
