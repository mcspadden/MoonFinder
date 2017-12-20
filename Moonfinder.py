print('MoonFinder by RTL Technologies')
print('Please wait while exceed the escape velocity of Earth...')
import time
time.sleep(5)

ans=True
while ans:
    print('''
    BTC | ETH | LTC | USD | GBP
    ''')
    ans=input('What currency would you like to use?')
    if ans=='BTC':
        print('\n BTC selected as default currency.')
        ans = None
    elif ans=='ETH':
        print('\n ETH selected as default currency.')
        ans = None
    elif ans=='LTC':
        print('\n LTC selected as default currency.')
        ans = None
    elif ans=='USD':
        print('\n USD selected as default currency.')
        ans = None
    elif ans=='GBP':
        print('\n GBP selected as default currency.')
        ans = None
    else:
        print('Not a supported currency at this time. Please verify the case matches and try again.'
              )

coinNames = []
while True:
    print('\n Enter the name of a coin' + \
          ' (Or press Enter once you have added all you desire.):')
    name = input()
    if name == '':
        break
    coinNames = coinNames + [name] # list concatenation
print('The coin names are:')
for name in coinNames:
    print(' ' + name)
