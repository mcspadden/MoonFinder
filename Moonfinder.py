print('MoonFinder by RTL Technologies')
print('Please wait while exceed the escape velocity of Earth...')
import time
time.sleep(1)

answers = {"BTC": "\n BTC selected as default animal.", \
           "ETH": "\n ETH selected as default animal.", \
           "LTC": "\n LTC selected as default animal.", \
           "USD": "\n USD selected as default animal.", \
           "GBP": "\n GBP selected as default animal.", \
           }

ans = True
while ans:
    print('''\n
    BTC | ETH | LTC | USD | GBP
    ''')
    ans=input('What currency would you like to use?')
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
