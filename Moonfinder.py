# McSpadden
import time, requests

print('MoonFinder by McSpadden')
print('Please wait while exceed the escape velocity of Earth...')
time.sleep(1) # changes delay speed

# Supported currencies
answers = {"BTC": "\n BTC selected as default currency.", \
           "ETH": "\n ETH selected as default currency.", \
           "LTC": "\n LTC selected as default currency.", \
           "USD": "\n USD selected as default currency.", \
           "GBP": "\n GBP selected as default currency.", \
           }

# Let user input their currency aka Seat Selector
ans = True
while ans: # line below print's the symbol for default currencies
    print('''\n
    BTC | ETH | LTC | USD | GBP
    ''')
    ans=input('What currency would you like to use?').upper() # setting ans and .upper() makes input all uppercase
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
        print('Not a supported currency at this time. Please try another currency.')

# Place below code in correct location later on
coinA=input('What coin would you like to select?').upper()
print('Please wait while your first class seat is being prepared.')
# Request to get coin's history
A1_Old = requests.get("http://coincap.io/history/LTC")
# Place JSON data as python var
A1 = A1_Old.json()
# Select the coins price on day 365
A1_365 = (A1["price"][0][1])
# Coin A still: Request to get coins data for today
A2_Now = requests.get("http://coincap.io/page/LTC")
# Place JSON data as python var
A2 = A2_Now.json()
# Select the coins price in USD for today
A2_Today= (A2["price_usd"])
# Creates var for Coin A's price difference in a percentage
print("Today: $" + str(A2_Today))
print("365 Days Ago: $" + str(A1_365))# remove after testing is finished
A_Difference = round((A2_Today - A1_365) / A1_365 * int("100")) # Forumla: Insert the formula here
# Prints the percentage of gains for Coin A
print(str(coinA) + " gains: " + str(A_Difference) + '%')
