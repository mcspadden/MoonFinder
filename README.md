# MoonFinder
Reserves a first-class seat to the moon

The name MoonFinder comes from the popular ideology that BTC and/or cryptos as a whole will take the crypto community to the moon. While some cryptos may be literally building a rocket to take us there, most are using the term moon as the cash out point. MoonFinder pulls user chosen data from CoinCap.io (limited to them as of now) and selects the best (numerical) coin to purchase. This is solely based off the coins gains (or losses) in the last 365 days and does **not** indicate a profit and/or loss will be made. See the MIT license below for the state of which MoonFinder is provided. 
# APIs

**Coincap.io**

Coincap.io is where the historical and current price of each crypto is pulled from. It is also where the acceptable cryptos list comes from. You can find their API [here](https://github.com/CoinCapDev/CoinCap.io "Coincap's API").

**CryptoCompare**

Cryptocompare is the API used for exchange rates. They have a ton of information and it can be found [here](https://min-api.cryptocompare.com/ "Cryptocompare's API").

# Calculations
MoonFinder uses this formula:
```((Price Sold - Purchase Price) ÷ (Purchase Price)) * 100```

**Price sold** is the price for coin `x` today.  
**Purchase Price** is the price of coin `x` 365 days ago.  
Then it is multiplied by **100** to turn it into a percentage.  

That formula is used for each coin you select and the results are compared to each other to select the mooncoin.   

**For example**:  
You select BTC, ETH, and LTC as your three coins and BTC as your default currency. The below is performed in _USD_:  
BTC:  
```((9000 - 4000) ÷ (4000)) * 100 = 125%```  
`9000` is the price today. `4000` is the price 365 days ago. BTC is now set to 125.   
ETH:  
```((800 - 65) ÷ (65)) * 100 = 1130.769231%```  
`800` is the price today. `65` is the price 365 days ago. ETH is now set to 1130.769231.  
LTC:  
```((195 - 24) ÷ (24)) * 100 = 684%```  
`195` is the price today. `24` is the price 365 days ago. LTC is now set to 684.  

BTC, ETH, and LTC are now compared and whichever coin has the greatest number is selected as your mooncoin. In this case, ETH is your mooncoin. From here, the USD prices above will be exchanged into your selected default currency. For this example, BTC was selected as the default currency. Say the exchange rate from 1 USD to 1 BTC is 0.00008802.

ETH:  
```800 * 0.00008802 = 0.070416 BTC``` The price today for ETH is 0.070416 BTC.  
```65 * 0.00008802 = 0.0057213 BTC``` The price 365 days ago for ETH was 0.0057213 BTC.  
```((0.070416 - 0.0057213) ÷ (0.0057213) * 100 = 1130.769231%``` The percentage will stay the same between all currencies so within the program, the percentage is technically calculated in USD, which does not really matter. 

# Notes 

**Rounding**  
Only the printed answer is rounded. In the above example, **1131%** would be printed for **ETH**. Say you choose coin _ABC_ and _XYZ_. _ABC_ has a percentage of **834.52** and _XYZ_ has a percentage of **834.78**. If both got printed, they would look identical at **835%**. _XYZ_ would be selected as your mooncoin although because the mooncoin is selected _**before**_ the number is rounded. See function `winner()` to see exactly how this occurs. 

**Exchange Rates**  
Always take into consideration the real time exchange rate. Since cryptos are consistently fluctuating in very high values, the cost 365 days ago in `x` crypto is almost guaranteed to be inaccurate. Using BTC as an example, the exchange rate from USD to BTC was not **0.00008802** 365 days ago. Therefore, the ETH price of **65** 365 days ago is not equal to **0.0057213** BTC 365 days ago. The ETH price of **65** 365 days ago is equal to **0.0057213** BTC today. I may resolve this later but it could cause confusion.  

# License

I'm inspired by the world; so anything **I did** here, I want the world to be freely inspired by as well. For anything I did not create here, refer to their respective license for use.

# MIT License

Copyright (c) 2018 McSpadden

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
