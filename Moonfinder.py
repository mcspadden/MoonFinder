# Moonfinder by McSpadden
print('MoonFinder by McSpadden')
print('Please wait while exceed the escape velocity of Earth...')
import time # import time to make a mini delay
time.sleep(1) # changes delay speed

# Supported default Currencies
answers = {"BTC": "\n BTC selected as default currency.", \
           "ETH": "\n ETH selected as default currency.", \
           "LTC": "\n LTC selected as default currency.", \
           "USD": "\n USD selected as default currency.", \
           "GBP": "\n GBP selected as default currency.", \
           }

# Seat selector
ans = True
while ans:
    # print's the symbol for default currencies
    print('''\n
    BTC | ETH | LTC | USD | GBP
    ''') 
    ans=input('What currency would you like to use?')
    if ans in answers: # if input was a supported currency, continue below
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
    else: # if input was not a supported currency
        print('Not a supported currency at this time. Please verify the case matches and try again.')
